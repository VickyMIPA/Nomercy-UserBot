from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sins(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`1.Sins Ganteng😎`")
    sleep(2)
    await typew.edit("`2.Sins Imutt Kyaaaa>_<`")
    sleep(1)
    await typew.edit("`3.Love u Smwaaa😚`")
    sleep(2)
    await typew.edit("`Hehe😁`")


CMD_HELP.update({
    "kontol":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sins`\
    \n↳ : Biasalah sadboy hikss"
    }
)
