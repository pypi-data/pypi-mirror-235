import json
import base64
from ..gadgets import methods, thumbnail

class Struct:
    def __str__(self) -> str:
        """Convert the object to a JSON string with an optional indentation.

        Args:
            indent (int, optional): Number of spaces for indentation. Defaults to 2.

        Returns:
            str: JSON representation of the object.
        """
        return self.jsonify(indent=2)

    def __getattr__(self, name):
        return self.find_keys(keys=name)

    def __setitem__(self, key, value):
        self.original_update[key] = value

    def __getitem__(self, key):
        return self.original_update[key]

    def __lts__(self, update: list, *args, **kwargs):
        for index, element in enumerate(update):
            if isinstance(element, list):
                update[index] = self.__lts__(update=element)
            elif isinstance(element, dict):
                update[index] = Struct(update=element)
            else:
                update[index] = element
        return update

    def __init__(self, update: dict, *args, **kwargs) -> None:
        self.original_update = update

    def to_dict(self):
        return self.original_update

    def jsonify(self, indent=None, *args, **kwargs) -> str:
        result = self.original_update.copy()
        result['original_update'] = 'dict{...}'
        return json.dumps(result, indent=indent, ensure_ascii=False, default=lambda value: str(value))

    def find_keys(self, keys, original_update=None, *args, **kwargs):
        if original_update is None:
            original_update = self.original_update

        if not isinstance(keys, list):
            keys = [keys]

        if isinstance(original_update, dict):
            for key in keys:
                try:
                    update = original_update[key]
                    if isinstance(update, dict):
                        update = Struct(update=update)
                    elif isinstance(update, list):
                        update = self.__lts__(update=update)
                    return update
                except KeyError:
                    pass

        for value in original_update:
            if isinstance(value, (dict, list)):
                try:
                    return self.find_keys(keys=keys, original_update=value)
                except AttributeError:
                    pass

        raise AttributeError(f'Struct object has no attribute {keys}')

    def guid_type(self, guid: str, *args, **kwargs) -> str:
        if isinstance(guid, str):
            if guid.startswith('u'):
                return 'User'
            elif guid.startswith('g'):
                return 'Group'
            elif guid.startswith('c'):
                return 'Channel'

    @property
    def type(self):
        try:
            return self.find_keys(keys=['type', 'author_type'])
        except AttributeError:
            pass

    @property
    def raw_text(self):
        try:
            return self.find_keys(keys='text')
        except AttributeError:
            pass

    @property
    def message_id(self):
        try:
            return self.find_keys(keys=['message_id', 'pinned_message_id'])
        except AttributeError:
            pass

    @property
    def reply_message_id(self):
        try:
            return self.find_keys(keys='reply_to_message_id')
        except AttributeError:
            pass

    @property
    def is_group(self):
        return self.type == 'Group'

    @property
    def is_channel(self):
        return self.type == 'Channel'

    @property
    def is_private(self):
        return self.type == 'User'

    @property
    def object_guid(self):
        try:
            return self.find_keys(keys=['group_guid', 'object_guid', 'channel_guid'])
        except AttributeError:
            pass

    @property
    def author_guid(self):
        try:
            return self.author_object_guid
        except AttributeError:
            pass

    async def pin(self, object_guid: str = None, message_id: str = None, action: str = methods.messages.Pin, *args, **kwargs):
        """Pin or unpin a message.

        Args:
            object_guid (str, optional): Custom object guid. Defaults to update.object_guid.
            message_id (str, optional): Custom message id. Defaults to update.message_id.
            action (bool, optional): Pin or unpin. Defaults to methods.messages.Pin (methods.messages.Pin, methods.messages.Unpin).

        Returns:
            BaseResults: Result of the pin action.
        """
        if object_guid is None:
            object_guid = self.object_guid
        if message_id is None:
            message_id = self.message_id
        return await self._client(
            methods.messages.SetPinMessage(
                object_guid=object_guid,
                message_id=message_id,
                action=action))

    async def edit(self, text: str, object_guid: str = None, message_id: str = None, *args, **kwargs):
        """Edit a message.

        Args:
            text (str): New message text.
            object_guid (str, optional): Custom object guid. Defaults to update.object_guid.
            message_id (str, optional): Custom message id. Defaults to update.message_id.
        """
        if object_guid is None:
            object_guid = self.object_guid
        if message_id is None:
            message_id = self.message_id
        return await self._client(
            methods.messages.EditMessage(
                object_guid=object_guid,
                message_id=message_id,
                text=text))

    async def copy(self, to_object_guid: str, from_object_guid: str = None, message_ids=None, *args, **kwargs):
        """Copy messages to another object.

        Args:
            to_object_guid (str): Destination object guid.
            from_object_guid (str, optional): Source object guid. Defaults to update.object_guid.
            message_ids (typing.Union[str, int, typing.List[str]], optional): Message ids. Defaults to update.message_id.

        Returns:
            Struct: Status and messages after copying.
        """
        if from_object_guid is None:
            from_object_guid = self.object_guid
        if message_ids is None:
            message_ids = self.message_id
        result = await self.get_messages(from_object_guid, message_ids)
        messages = []
        if result.messages:
            for message in result.messages:
                try:
                    file_inline = message.file_inline
                    kwargs.update(file_inline.to_dict())
                except AttributeError:
                    file_inline = None
                try:
                    thumb = thumbnail.Thumbnail(base64.b64decode(message.thumb_inline), *args, **kwargs)
                except AttributeError:
                    thumb = kwargs.get('thumb', True)
                try:
                    message = message.sticker
                except AttributeError:
                    message = message.raw_text
                if file_inline is not None:
                    if file_inline.type not in [methods.messages.Gif, methods.messages.Sticker]:
                        file_inline = await self.download(file_inline)
                        messages.append(await self._client.send_message(
                            thumb=thumb,
                            message=message,
                            file_inline=file_inline,
                            object_guid=to_object_guid, *args, **kwargs))
                        continue
                messages.append(await self._client.send_message(
                    message=message,
                    object_guid=to_object_guid,
                    file_inline=file_inline, *args, **kwargs))
        return Struct({'status': 'OK', 'messages': messages})

    async def seen(self, seen_list: dict = None, *args, **kwargs):
        """Update seen status of chats.

        Args:
            seen_list (dict, optional): A dictionary of object_guid and message_id pairs. Defaults to {update.object_guid: update.message_id}.
        """
        if seen_list is None:
            seen_list = {self.object_guid: self.message_id}
        return await self._client(methods.chats.SeenChats(seen_list=seen_list))

    async def reply(self, message=None, object_guid: str = None, reply_to_message_id: str = None, file_inline: str = None, *args, **kwargs):
        """Reply to a message.

        Args:
            message (Any, optional): Message, caption, or sticker. Defaults to None.
            object_guid (str, optional): Custom object guid. Defaults to update.object_guid.
            reply_to_message_id (str, optional): Message to reply to. Defaults to None.
            file_inline (typing.Union[pathlib.Path, bytes], optional): File to send. Defaults to None.
        """
        if object_guid is None:
            object_guid = self.object_guid
        if reply_to_message_id is None:
            reply_to_message_id = self.message_id
        return await self._client.send_message(
            message=message,
            object_guid=object_guid,
            file_inline=file_inline,
            reply_to_message_id=reply_to_message_id, *args, **kwargs)

    async def forwards(self, to_object_guid: str, from_object_guid: str = None, message_ids=None, *args, **kwargs):
        """Forward messages to another object.

        Args:
            to_object_guid (str): Destination object guid.
            from_object_guid (str, optional): Source object guid. Defaults to update.object_guid.
            message_ids (typing.Union[str, int, typing.List[str]], optional): Message ids. Defaults to update.message_id.

        Returns:
            BaseResults: Result of the forward action.
        """
        if from_object_guid is None:
            from_object_guid = self.object_guid
        if message_ids is None:
            message_ids = self.message_id
        return await self._client(
            methods.messages.ForwardMessages(
                from_object_guid=from_object_guid,
                to_object_guid=to_object_guid,
                message_ids=message_ids))

    async def download(self, file_inline=None, file=None, *args, **kwargs):
        """Download a file.

        Args:
            file_inline (BaseInline): Inline file object. Defaults to self.file_inline.
            file (str, optional): File path or name. Defaults to None.

        Returns:
            bytes: File content.
        """
        return await self._client.download_file_inline(
            file_inline or self.file_inline,
            file=file, *args, **kwargs)

    async def get_author(self, author_guid: str = None, *args, **kwargs):
        """Get user or author information.

        Args:
            author_guid (str, optional): Custom author guid. Defaults to update.author_guid.

        Returns:
            BaseResults: User or author information.
        """
        if author_guid is None:
            author_guid = self.author_guid
        return await self.get_object(object_guid=author_guid, *args, **kwargs)

    async def get_object(self, object_guid: str = None, *args, **kwargs):
        """Get object information (User, Group, or Channel).

        Args:
            object_guid (str, optional): Custom object guid. Defaults to update.object_guid.

        Returns:
            BaseResults: Object information.
        """
        if object_guid is None:
            object_guid = self.object_guid
        if self.guid_type(object_guid) == 'User':
            return await self._client(
                methods.users.GetUserInfo(
                    user_guid=object_guid))
        elif self.guid_type(object_guid) == 'Group':
            return await self._client(
                methods.groups.GetGroupInfo(
                    object_guid=object_guid))
        elif self.guid_type(object_guid) == 'Channel':
            return await self._client(
                methods.channels.GetChannelInfo(
                    object_guid=object_guid))

    async def get_messages(self, object_guid: str = None, message_ids=None, *args, **kwargs):
        """Get messages by message_ids.

        Args:
            object_guid (str, optional): Custom object guid. Defaults to update.object_guid.
            message_ids (str, int, typing.List[str]], optional): Message ids. Defaults to update.message_id.

        Returns:
            BaseResults: Messages information.
        """
        if object_guid is None:
            object_guid = self.object_guid
        if message_ids is None:
            message_ids = self.message_id
        return await self._client(
            methods.messages.GetMessagesByID(
                object_guid=object_guid, message_ids=message_ids))

    async def delete_messages(self, object_guid: str = None, message_ids=None, *args, **kwargs):
        """Delete messages by message_ids.

        Args:
            object_guid (str, optional): Custom object guid. Defaults to update.object_guid.
            message_ids (str, list, optional): Custom message ids. Defaults to update.message_id.
            type (str, optional): Type of message deletion (Local or Global). Defaults to methods.messages.Global (methods.messages.Local, methods.messages.Global).

        Returns:
            BaseResults: Result of the delete action.
        """
        if object_guid is None:
            object_guid = self.object_guid
        if message_ids is None:
            message_ids = self.message_id
        return await self._client(
            methods.messages.DeleteMessages(
                object_guid=object_guid,
                message_ids=message_ids, *args, **kwargs))
