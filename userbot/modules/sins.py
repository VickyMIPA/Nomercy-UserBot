from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sins(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama Sins itu Ganteng😎`")
    sleep(2)
    await typew.edit("`Kedua Sins Manis`")
    sleep(1)
    await typew.edit("`Yang Ketiga Love U Smwaa😚`")

CMD_HELP.update({
    "animasi2":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.piki`\
    \n↳ : Biasalah sadboy hikss\.
)
 }
