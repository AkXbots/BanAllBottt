import os
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from . import bot 
from Banall import STARTED, FINISH, ERROR, OWN_UNAME


@bot.on_message(filters.group & filters.command("banall"))
def main(_, msg: Message):
    chat = msg.chat
    me = chat.get_member(bot.get_me().id)
    if chat.get_member(msg.from_user.id).can_manage_chat and me.can_restrict_members and me.can_delete_messages:
        try:
            msg.reply(STARTED.format(chat.members_count))
            count_kicks = 0
            for member in chat.iter_members():
                if not member.can_manage_chat:
                    bot.ban_chat_member(chat_id=msg.chat.id, user_id=member.user.id)
                    count_kicks += 1
            msg.reply(FINISH.format(count_kicks))
        except Exception as e:
            msg.reply(ERROR.format(str(e)))
    else:
        msg.reply("ɪ ɴᴇᴇᴅ ᴛᴏ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ !")


@bot.on_message(filters.group & filters.service, group=2)
def service(c, m):
    m.delete()


@bot.on_message(filters.private)
def start(_, msg: Message):
    msg.reply_photo(
                    photo="https://telegra.ph/file/3794971472562ae7c775b.jpg", 
                    caption="ɪᴛ'ꜱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇ & ᴘᴏᴡᴇʀꜰᴜʟ ʙᴀɴ-ᴀʟʟ ʙᴏᴛ ᴡɪᴛʜ ɴᴏ ʟᴀɢ ɪꜱꜱᴜᴇꜱ. ᴛʜɪꜱ ʙᴀɴ-ᴀʟʟ ᴇᴅɪᴛɪᴏɴ ɪꜱ ᴄʀᴇᴀᴛᴇ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ꜰᴏʀ ꜰᴜᴄᴋɪɴɢ ᴛᴏxɪᴄ ᴄᴜᴍᴍɪɴɪᴛʏ'ꜱ.
ᴀᴅᴅ ᴛʜɪꜱ ʙᴀɴᴀʟʟ ᴇᴅɪᴛɪᴏɴ ᴛᴏ ᴇɴᴇᴍʏ'ꜱ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʙᴀɴ ʀɪɢʜᴛꜱ  ᴀɴᴅ ꜰᴜᴄᴋ ʜɪꜱ ᴡʜᴏʟᴇ ᴄʟᴀɴ ᴡɪᴛʜᴏᴜᴛ ꜰᴀᴄɪɴɢ ᴀɴʏ ʙᴜɢꜱ/ᴘʀᴏʙʟᴇᴍꜱ.

❍ ᴛʏᴘᴇ /help ғᴏʀ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs!! 
❍  ᴘᴏᴡᴇʀᴇᴅ ʙʏ » @Bonten_Destroyers", 

                    reply_markup=InlineKeyboardMarkup(
                                                      [
                                                       [
                                                        InlineKeyboardButton("sᴏᴜʀᴄᴇ", url="https://www.github.com/itz-mst-boy/BanAllBot"), 
                                                        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/worldwide_friend_zone")                                      
                                                       ], 
                                                       [
                                                     )
)


bot.run()
idle()

print("ᴅᴏɴᴇ ʙᴀɴᴀʟʟ  sᴛᴀʀᴛᴇᴅ ...") 
print("ᴊᴏɪɴ  @bonten_mainchats || @bonten_destroyers For Help") 
