from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
        **━━━━━━━━━━━━━━━**
**💞 {MUSIC_BOT_NAME} ᴍᴜsɪᴄ ʟᴏɢs **
**━━━━━━━━━━━━━━━**
**🌹️ 𝐂ԋα𝐓 𝐍αɱ𝐄 : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**🥀 𝐍αɱ𝐄 : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**🌸 𝐔ʂҽɾɳαɱ𝐄 : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**🌷 𝐈ԃ  : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**🌿 𝐂ԋα𝐓 𝐥ιɳ𝐊: >** {chatusername}
**━━━━━━━━━━━━━━━**
**🌻 𝐒ҽαɾƈԋҽ𝐃 𝐅σ𝐑:** {message.text}
**━━━━━━━━━━━━━━━**
**💐 𝐒ƚɾҽα𝐌 𝐓ყρ𝐄:** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
