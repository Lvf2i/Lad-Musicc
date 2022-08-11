import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://freenetcom.herokuapp.com/dl/1063/AgADvL8xG1U4qEs.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@Hamouddi"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("القناة", "https://t.me/meeddu")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
