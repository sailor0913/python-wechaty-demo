import asyncio
import os

from wechaty import Wechaty

from vars.personal_vars import WECHATY_PUPPET_SERVICE_TOKEN
from vars.public_vars import WECHATY_PUPPET_SERVICE_ENDPOINT
from plugin.life.main import LifePlugin
from plugin.notion.main import NotionPlugin


os.environ["WECHATY_PUPPET_SERVICE_TOKEN"] = WECHATY_PUPPET_SERVICE_TOKEN
os.environ["WECHATY_PUPPET_SERVICE_ENDPOINT"] = WECHATY_PUPPET_SERVICE_ENDPOINT


async def main():
    bot = Wechaty().use([
        LifePlugin(),
        NotionPlugin()
    ])
    await bot.start()


asyncio.run(main())
