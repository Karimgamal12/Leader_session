from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("⩩ بدء استخراج الجلسة ☆.", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="⩩ الصفحة الرئيسية ☆.", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "𝐒𝐎𝐔𝐑𝐂𝐄 𝗟𝗘𝗮𝗗𝗲𝗥", url="https://t.me/V_P_N_8"
            )
        ],
        [
            InlineKeyboardButton("طريقة استخدام البوت ☆", callback_data="help"),
            InlineKeyboardButton("حول ⩩", callback_data="about"),
        ],
        [InlineKeyboardButton("َժٍᥱُ᥎", url="https://t.me/Z_X_Z_B")],
    ]

    START = """
أهلًا {} ♦
ومرحبًا بك عزيزي في {}
البوت متخصص في استخراج الجلسات
مثل: - البايروجرام ، التيرمكس
من خلال إرسال الأيبي ايدي والأيبي هاش ورقم هاتفك والكود والتحقق بخطوتين إذا كنت مفعله
َժٍᥱُ᥎ :- @Z_X_Z_B
    """

    HELP = """
 **الأوامر المتاحة**

/about - لحول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ريبو البوت
/generate - لاستخراج الجلسات 
/cancel - لإلغاء الاستخراج 
/restart - لترسيت البوت
"""

    # About Message
    ABOUT = """
**حول البوت** 
╔━━━━━𓌹 ↱ 𝐒𝐎𝐔𝐑𝐂𝐄 𝗟𝗘𝗮𝗗𝗲𝗥 ↲ 𓌺━━━━━━╗  
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
⩩ انا بوت استخراج جلسات من سورس افاتار
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
قناة السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/V_P_N_8)
لغة البرمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
َժٍᥱُ᥎ : Z_X_Z_B
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
╚━━━━━𓌹 ↱ 𝐒𝐎𝐔𝐑𝐂𝐄 𝗟𝗘𝗮𝗗𝗲𝗥 ↲ 𓌺━━━━━━╝
    """

    # Repo Message
    REPO = """
⋖━━❲𖣂❳━━𖠙𝐒𝐎𝐔𝐑𝐂𝐄 𝗟𝗘𝗮𝗗𝗲𝗥𖠙━━❲𖣂❳━━⋗
⩩ انا بوت استخراج جلسات خاص بسورس 𝗟𝗘𝗮𝗗𝗲𝗥
╔━━━━━𓌹 ↱ 𝐒𝐎𝐔𝐑𝐂𝐄 𝗟𝗘𝗮𝗗𝗲𝗥 ↲ 𓌺━━━━━━╗  

⩩ السورس [𝐒𝐎𝐔𝐑𝐂𝐄 𝗟𝗘𝗮𝗗𝗲𝗥](https://t.me/V_P_N_8)

╚━━━━━𓌹 ↱ 𝐒𝐎𝐔𝐑𝐂𝐄 𝗟𝗘𝗮𝗗𝗲𝗥 ↲ 𓌺━━━━━━╝
إذا كان لديك أي سؤال ، فراسل » المطور » [َժٍᥱُ᥎] Z_X_Z_B
⋖━━❲𖣂❳━━𖠙𝐒𝐎𝐔𝐑𝐂𝐄 𝗟𝗘𝗮𝗗𝗲𝗥𖠙━━❲𖣂❳━━⋗
   """
