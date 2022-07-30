from wechaty import Message, Room, Contact
from wechaty.plugin import WechatyPlugin
from typing import Union

from api.notion import query_test_database, create_test_database




class NotionPlugin(WechatyPlugin):
    async def on_message(self, msg: Message) -> None:
        if msg.is_self():
            return
        text = msg.text()
        chat_room = msg.room()
        from_contact: Union[Room, Contact] = msg.talker() if chat_room is None else chat_room

        if text[0:3] == "手机 ":
            res = query_test_database(name=text[3:])
            if len(res["results"]) != 0 and len(res["results"][0]["properties"]["Tel"]["rich_text"]) != 0:
                await from_contact.ready()
                await from_contact.say(res["results"][0]["properties"]["Tel"]["rich_text"][0]["plain_text"])
            else:
                await from_contact.ready()
                await from_contact.say('查询不到此人手机，请联系管理员添加')

        if text[0:3] == "添加 ":
            tel = text[3:14]
            name = text[15:]
            res = create_test_database(name=name, tel=tel)
            if res == 200:
                await from_contact.ready()
                await from_contact.say("增加成功")
            else:
                await from_contact.ready()
                await from_contact.say("增加失败, 未知错误")
