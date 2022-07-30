from wechaty import Message, Room, Contact
from wechaty.plugin import WechatyPlugin
from typing import Union

from api.life import get_province_oil


class LifePlugin(WechatyPlugin):
    async def on_message(self, msg: Message) -> None:
        if msg.is_self():
            return
        text = msg.text()
        chat_room = msg.room()
        from_contact: Union[Room, Contact] = msg.talker() if chat_room is None else chat_room

        if text[0:3] == "油价 " or text == "油价":
            res = get_province_oil(province=text[3:] if text[3:] else "河南")
            await from_contact.ready()
            await from_contact.say(res)
