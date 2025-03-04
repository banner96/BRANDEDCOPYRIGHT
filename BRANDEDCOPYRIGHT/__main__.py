import asyncio
import importlib
from pyrogram import idle
from BRANDEDCOPYRIGHT import BRANDEDCOPYRIGHT
from BRANDEDCOPYRIGHT.modules import ALL_MODULES

LOGGER_ID =    -1002107679944

loop = asyncio.get_event_loop()

async def brandedpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("BRANDEDCOPYRIGHT.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await idle()
    print("lawda")
    await BRANDEDCOPYRIGHT.send_message(LOGGER_ID, "***")

if __name__ == "__main__":
    loop.run_until_complete(brandedpapa_boot())
    
