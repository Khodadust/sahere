from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
import sqlite3
import re
from telegram.ext import ContextTypes , ConversationHandler, CommandHandler, filters, MessageHandler
# from msg import keyboard



keyboard = [
    [KeyboardButton('📩 پیام خصوصی'), KeyboardButton('🚣 چالش'),KeyboardButton('🌐 پیام همگانی')],
    [KeyboardButton('🎰 کازینو'), KeyboardButton('🏎 مسابقه'), KeyboardButton('🎲 جایزه روزانه')],
    [KeyboardButton('🪪 پروفایل'), KeyboardButton('🎁 دعوت دوستان'), KeyboardButton('🗂 تسک')],
    [KeyboardButton('👨‍💻 پیام به ادمین'), KeyboardButton('📚 راهنما')]]





conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()




SENDING_MASSEGE = 1




found_words = []
async def start_q(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    words = update.message.text.lower().split()
    yy = ['🔗', '🧑🏻‍⚖️', '🔫', '📸', '🪖', '👮🏻‍♂️', '🤠', '🧔🏼‍♂️', '👣️', '👀', '💉', '🧑🏻‍🏭', '🧝🏻','👮🏻','💂🏻','🦸🏻','🦸🏻‍♀️']
    global found_words
    for word in yy:
        if word.lower() in words:
            found_words.append(word)
    if found_words:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='''محقق ازت نقطه چه حرف هایی رو میخواد؟

آموزش ویدیویی استفاده از این قابلیت(حتما ببینید)👇
/mohaqeqgif

کد های نقطه دادن به ربات👇
/mohaqeq''')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='''محقق ازت نقطه چه حرف هایی رو میخواد؟

آموزش ویدیویی استفاده از این قابلیت(حتما ببینید)👇
/mohaqeqgif

کد های نقطه دادن به ربات👇
/mohaqeq''')
    return SENDING_MASSEGE



async def javab_qeq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global found_words
    user_id = update.effective_user.id
    words = update.message.text
    if words == '3e':
        num1 = 500
        num2 = 500
        num3 = 500
    elif words == '2e':
        num1 = 550
        num2 = 550
        num3 = 550 
    elif words == 'بالا':
        num1 = 300
        num2 = 300
        num3 = 300
    elif words == 'پایین':
        num1 = 400
        num2 = 400
        num3 = 400
    elif words == 'بدون':
        num1 = 700
        num2 = 700
        num3 = 700
    elif words == 'کل':
        num1 = 800
        num2 = 800
        num3 = 800
    else:
        try:
            num11 = words.split()[0]
            num22 = words.split()[1]
            try:
                num33 = words.split()[2]
                if num33 == 'e':
                    num33 = 3001
            except:
                num33 = str(1001)

            num1 = int(num11)
            num2 = int(num22)
            num3 = int(num33)
            num1 = num1 - 1
            num2 = num2 - 1
            num3 = num3 - 1
        except:
            await update.message.reply_text('محقق به چند حالت میتونه نقطه بپرسه\n\nاگه گفت مثل جمع نقطه سوم و چهارم باید عدد انگلیسی همراه با فاصله بینش بنویسی👇\n\n3 4\n\nاگه گفت جمع سه حرف👇\n\n1 2 3\n\nاگه گفت جمع کل👇\n\nکل\n\nاگه گفت نقطه های بالا👇\n\nبالا\n\nاگه گفت نقطه های پایین👇\n\nپایین\n\nاگه گفت تعداد حروف بدون نقطه👇\n\nبدون\n\nاگه گفت جمع نقطه های سه حرف آخر👇\n\n3e\n\nاگه گفت جمع نقطه های دو حرف آخر👇\n\n2e\n\nبا تشکر')
            await update.message.reply_text('دوستان آموزش متنی بالای کامله و مطمئنم همتون متوجه میشید ولی حالا آموزش تصویری هم درست کردم👇\n\nhttps://t.me/saherehrobot')
            await update.message.reply_text('اشتباه وارد کردید🛑\nلطفا بعد از دیدن آموزش دوباره تلاش کنید')
            return
    m88 = 'خب اول حساب کنیم که جمع نقطه های حرف هایی که گفتی در هر نقش به چه صورته:'
    # await update.message.reply_text(f'{num1}{type(num1)}')
    # await update.message.reply_text(f'{num2}{type(num2)}')
    # await update.message.reply_text(f'{num3}{type(num3)}')
    khabar = [1, 1, 0, 1, 0, 0, 0] 
    bazpors = [1, 0, 1, 3, 0, 0] 
    esna = [0, 0, 1, 0, 2, 3, 0]
    tofang = [2, 1, 1, 0, 0, 0, 0]
    police = [3, 0, 2, 0]
    kalantar = [0, 0, 0, 1, 2, 0]
    qazi = [2, 0, 1, 0]
    rish = [0, 2, 3, 0, 1, 2, 0]
    rad = [0, 0, 0, 2, 0]
    did = [0, 2, 0, 1, 0, 1]
    doctor = [0, 0, 2, 0]
    badi = [1, 0, 0, 2, 0, 0, 0, 0]
    hero = [2, 0, 0, 0, 0, 1]
    zere = [1, 0, 0, 0, 0, 1]
    sah = [0, 0, 0, 0, 0]
    try:
        if '📸' in found_words or '👣️' in found_words or '👀' in found_words:
            gg_khabar = "Index out of range"
        elif num3 == 1000:
            gg_khabar = khabar[num1] + khabar[num2]
        elif num3 == 500:
            gg_khabar = khabar[-1] + khabar[-2] + khabar[-3]
        elif num3 == 550:
            gg_khabar = khabar[-1] + khabar[-2]
        elif num3 == 300:
            gg_khabar = 2
        elif num3 == 400:
            gg_khabar = 1
        elif num3 == 700:
            gg_khabar = 4
        elif num3 == 800:
            gg_khabar = 3
        elif num3 == 3000:
            gg_khabar = khabar[num1] + khabar[num2] + khabar[-1]
        else:
            gg_khabar = khabar[num1] + khabar[num2] + khabar[num3]
    except IndexError:
        gg_khabar = "Index out of range"


    try:
        if '🔗' in found_words:
            gg_bazpors = "Index out of range"
        elif num3 == 1000:
            gg_bazpors = bazpors[num1] + bazpors[num2]
        elif num3 == 500:
            gg_bazpors = bazpors[-1] + bazpors[-2] + bazpors[-3]
        elif num3 == 550:
            gg_bazpors = bazpors[-1] + bazpors[-2]
        elif num3 == 300:
            gg_bazpors = 1
        elif num3 == 400:
            gg_bazpors = 4
        elif num3 == 700:
            gg_bazpors = 3
        elif num3 == 800:
            gg_bazpors = 5
        elif num3 == 3000:
            gg_bazpors = bazpors[num1] + bazpors[num2] + bazpors[-1]
        else:
            gg_bazpors = bazpors[num1] + bazpors[num2] + bazpors[num3]
    except IndexError:
        gg_bazpors = "Index out of range"

    try:
        if '🔫' in found_words or '🪖' in found_words or '👮🏻‍♂️' in found_words:
            gg_esna = "Index out of range"
        elif num3 == 1000:
            gg_esna = esna[num1] + esna[num2]
        elif num3 == 500:
            gg_esna = esna[-1] + esna[-2] + esna[-3]
        elif num3 == 550:
            gg_esna = esna[-1] + esna[-2]
        elif num3 == 300:
            gg_esna = 1
        elif num3 == 400:
            gg_esna = 5
        elif num3 == 700:
            gg_esna = 4
        elif num3 == 800:
            gg_esna = 6
        elif num3 == 3000:
            gg_esna = esna[num1] + esna[num2] + esna[-1]
        else:
            gg_esna = esna[num1] + esna[num2] + esna[num3]
    except IndexError:
        gg_esna = "Index out of range"

    try:
        if '🔫' in found_words or '🪖' in found_words or '👮🏻‍♂️' in found_words:
            gg_tofang = "Index out of range"
        elif num3 == 1000:
            gg_tofang = tofang[num1] + tofang[num2]
        elif num3 == 500:
            gg_tofang = tofang[-1] + tofang[-2] + tofang[-3]
        elif num3 == 550:
            gg_tofang = tofang[-1] + tofang[-2]
        elif num3 == 300:
            gg_tofang = 4
        elif num3 == 400:
            gg_tofang = 0
        elif num3 == 700:
            gg_tofang = 4
        elif num3 == 800:
            gg_tofang = 4
        elif num3 == 3000:
            gg_tofang = tofang[num1] + tofang[num2] + tofang[-1]
        else:
            gg_tofang = tofang[num1] + tofang[num2] + tofang[num3]
    except IndexError:
        gg_tofang = "Index out of range"

    try:
        if '🔫' in found_words or '🪖' in found_words or '👮🏻‍♂️' in found_words:
            gg_police = "Index out of range"
        elif num3 == 1000:
            gg_police = police[num1] + police[num2]
        elif num3 == 500:
            gg_police = police[-1] + police[-2] + police[-3]
        elif num3 == 550:
            gg_police = police[-1] + police[-2]
        elif num3 == 300:
            gg_police = 0
        elif num3 == 400:
            gg_police = 5
        elif num3 == 700:
            gg_police = 1
        elif num3 == 800:
            gg_police = 5
        elif num3 == 3000:
            gg_police = police[num1] + police[num2] + police[-1]
        else:
            gg_police = police[num1] + police[num2] + police[num3]
    except IndexError:
        gg_police = "Index out of range"

    try:
        if '🤠' in found_words or '🧔🏼\u200d♂️' in found_words or '🧑🏻\u200d⚖️' in found_words:
            gg_kalantar = "Index out of range"
        elif num3 == 1000:
            gg_kalantar = kalantar[num1] + kalantar[num2]
        elif num3 == 500:
            gg_kalantar = kalantar[-1] + kalantar[-2] + kalantar[-3]
        elif num3 == 550:
            gg_kalantar = kalantar[-1] + kalantar[-2]
        elif num3 == 300:
            gg_kalantar = 3
        elif num3 == 400:
            gg_kalantar = 0
        elif num3 == 700:
            gg_kalantar = 4
        elif num3 == 800:
            gg_kalantar = 3
        elif num3 == 3000:
            gg_kalantar = kalantar[num1] + kalantar[num2] + kalantar[-1]
        else:
            gg_kalantar = kalantar[num1] + kalantar[num2] + kalantar[num3]
    except IndexError:
        gg_kalantar = "Index out of range"

    try:
        if '🤠' in found_words or '🧔🏼\u200d♂️' in found_words or '🧑🏻\u200d⚖️' in found_words:
            gg_qazi = "Index out of range"
        elif num3 == 1000:
            gg_qazi = qazi[num1] + qazi[num2]
        elif num3 == 500:
            gg_qazi = qazi[-1] + qazi[-2] + qazi[-3]
        elif num3 == 550:
            gg_qazi = qazi[-1] + qazi[-2]
        elif num3 == 300:
            gg_qazi = 3
        elif num3 == 400:
            gg_qazi = 0
        elif num3 == 700:
            gg_qazi = 2
        elif num3 == 800:
            gg_qazi = 3
        elif num3 == 3000:
            gg_qazi = qazi[num1] + qazi[num2] + qazi[-1]
        else:
            gg_qazi = qazi[num1] + qazi[num2] + qazi[num3]
    except IndexError:
        gg_qazi = "Index out of range"

    try:
        if '🤠' in found_words or '🧔🏼\u200d♂️' in found_words or '🧑🏻\u200d⚖️' in found_words:
            gg_rish = "Index out of range"
        elif num3 == 1000:
            gg_rish = rish[num1] + rish[num2]
        elif num3 == 500:
            gg_rish = rish[-1] + rish[-2] + rish[-3]
        elif num3 == 550:
            gg_rish = rish[-1] + rish[-2]
        elif num3 == 300:
            gg_rish = 4
        elif num3 == 400:
            gg_rish = 4
        elif num3 == 700:
            gg_rish = 3
        elif num3 == 800:
            gg_rish = 8
        elif num3 == 3000:
            gg_rish = rish[num1] + rish[num2] + rish[-1]
        else:
            gg_rish = rish[num1] + rish[num2] + rish[num3]
    except IndexError:
        gg_rish = "Index out of range"

    try:
        if '📸' in found_words or '👣️' in found_words or '👀' in found_words:
            gg_rad = "Index out of range"
        elif num3 == 1000:
            gg_rad = rad[num1] + rad[num2]
        elif num3 == 500:
            gg_rad = rad[-1] + rad[-2] + rad[-3]
        elif num3 == 550:
            gg_rad = rad[-1] + rad[-2]
        elif num3 == 300:
            gg_rad = 0
        elif num3 == 400:
            gg_rad = 2
        elif num3 == 700:
            gg_rad = 4
        elif num3 == 800:
            gg_rad = 2
        elif num3 == 3000:
            gg_rad = rad[num1] + rad[num2] + rad[-1]
        else:
            gg_rad = rad[num1] + rad[num2] + rad[num3]
    except IndexError:
        gg_rad = "Index out of range"

    try:
        if '📸' in found_words or '👣️' in found_words or '👀' in found_words:
            gg_did = "Index out of range"
        elif num3 == 1000:
            gg_did = did[num1] + did[num2]
        elif num3 == 500:
            gg_did = did[-1] + did[-2] + did[-3]
        elif num3 == 550:
            gg_did = did[-1] + did[-2]
        elif num3 == 300:
            gg_did = 1
        elif num3 == 400:
            gg_did = 3
        elif num3 == 700:
            gg_did = 3
        elif num3 == 800:
            gg_did = 4
        elif num3 == 3000:
            gg_did = did[num1] + did[num2] + did[-1]
        else:
            gg_did = did[num1] + did[num2] + did[num3]
    except IndexError:
        gg_did = "Index out of range"

    try:
        if '💉' in found_words or '💂🏻' in found_words or '🦸🏻' in found_words or '🧑🏻\u200d🏭' in found_words:
            gg_doctor = "Index out of range"
        elif num3 == 1000:
            gg_doctor = doctor[num1] + doctor[num2]
        elif num3 == 500:
            gg_doctor = doctor[-1] + doctor[-2] + doctor[-3]
        elif num3 == 550:
            gg_doctor = doctor[-1] + doctor[-2]
        elif num3 == 300:
            gg_doctor = 2
        elif num3 == 400:
            gg_doctor = 0
        elif num3 == 700:
            gg_doctor = 3
        elif num3 == 800:
            gg_doctor = 2
        elif num3 == 3000:
            gg_doctor = doctor[num1] + doctor[num2] + doctor[-1]
        else:
            gg_doctor = doctor[num1] + doctor[num2] + doctor[num3]
    except IndexError:
        gg_doctor = "Index out of range"

    try:
        if '💉' in found_words or '💂🏻' in found_words or '🦸🏻' in found_words or '🧑🏻\u200d🏭' in found_words:
            gg_badi = "Index out of range"
        elif num3 == 1000:
            gg_badi = badi[num1] + badi[num2]
        elif num3 == 500:
            gg_badi = badi[-1] + badi[-2] + badi[-3]
        elif num3 == 550:
            gg_badi = badi[-1] + badi[-2]
        elif num3 == 300:
            gg_badi = 0
        elif num3 == 400:
            gg_badi = 3
        elif num3 == 700:
            gg_badi = 6
        elif num3 == 800:
            gg_badi = 3
        elif num3 == 3000:
            gg_badi = badi[num1] + badi[num2] + badi[-1]
        else:
            gg_badi = badi[num1] + badi[num2] + badi[num3]
    except IndexError:
        gg_badi = "Index out of range"

    try:
        if '💉' in found_words or '💂🏻' in found_words or '🦸🏻' in found_words or '🧑🏻\u200d🏭' in found_words:
            gg_hero = "Index out of range"
        elif num3 == 1000:
            gg_hero = hero[num1] + hero[num2]
        elif num3 == 500:
            gg_hero = hero[-1] + hero[-2] + hero[-3]
        elif num3 == 550:
            gg_hero = hero[-1] + hero[-2]
        elif num3 == 300:
            gg_hero = 3
        elif num3 == 400:
            gg_hero = 0
        elif num3 == 700:
            gg_hero = 4
        elif num3 == 800:
            gg_hero = 3
        elif num3 == 3000:
            gg_hero = hero[num1] + hero[num2] + hero[-1]
        else:
            gg_hero = hero[num1] + hero[num2] + hero[num3]
    except IndexError:
        gg_hero = "Index out of range"

    try:
        if '💉' in found_words or '💂🏻' in found_words or '🦸🏻' in found_words or '🧑🏻\u200d🏭' in found_words:
            gg_zere = "Index out of range"
        elif num3 == 1000:
            gg_zere = zere[num1] + zere[num2]
        elif num3 == 500:
            gg_zere = zere[-1] + zere[-2] + zere[-3]
        elif num3 == 550:
            gg_zere = zere[-1] + zere[-2]
        elif num3 == 300:
            gg_zere = 2
        elif num3 == 400:
            gg_zere = 0
        elif num3 == 700:
            gg_zere = 4
        elif num3 == 800:
            gg_zere = 2
        elif num3 == 3000:
            gg_zere = zere[num1] + zere[num2] + zere[-1]
        else:
            gg_zere = zere[num1] + zere[num2] + zere[num3]
    except IndexError:
        gg_zere = "Index out of range"

    try:
        if '🧝🏻' in found_words:
            gg_sah = "Index out of range"
        elif num3 == 1000:
            gg_sah = sah[num1] + sah[num2]
        elif num3 == 500:
            gg_sah = sah[-1] + sah[-2] + sah[-3]
        elif num3 == 550:
            gg_sah = sah[-1] + sah[-2]
        elif num3 == 300:
            gg_sah = 0
        elif num3 == 400:
            gg_sah = 0
        elif num3 == 700:
            gg_sah = 5
        elif num3 == 700:
            gg_sah = 0
        elif num3 == 3000:
            gg_sah = sah[num1] + sah[num2] + sah[-1]
        else:
            gg_sah = sah[num1] + sah[num2] + sah[num3]
    except IndexError:
        gg_sah = "Index out of range"

    # Create a dictionary to store the values and their counts
    values_dict = {}

    # Check each variable and add it to the dictionary
    if gg_khabar != "Index out of range":
        values_dict["📸 خبرنگار"] = gg_khabar
    if gg_bazpors != "Index out of range":
        values_dict["🔗بازپرس"] = gg_bazpors
    if gg_esna != "Index out of range":
        values_dict["🔫اسنایپر"] = gg_esna
    if gg_tofang != "Index out of range":
        values_dict["🪖 تفنگدار"] = gg_tofang
    if gg_police != "Index out of range":
        values_dict["👮🏻‍♂️پلیس"] = gg_police
    if gg_kalantar != "Index out of range":
        values_dict["🤠کلانتر"] = gg_kalantar
    if gg_qazi != "Index out of range":
        values_dict["🧑🏻‍⚖️قاضی"] = gg_qazi
    if gg_rish != "Index out of range":
        values_dict["🧔🏼‍♂️ریش سفید"] = gg_rish
    if gg_rad != "Index out of range":
        values_dict["👣️ردگیر"] = gg_rad
    if gg_did != "Index out of range":
        values_dict["👀دیدبان"] = gg_did
    if gg_doctor != "Index out of range":
        values_dict["💉دکتر"] = gg_doctor
    if gg_badi != "Index out of range":
        values_dict["💂‍♂️بادیگارد"] = gg_badi
    if gg_hero != "Index out of range":
        values_dict["🦸🏻قهرمان"] = gg_hero
    if gg_zere != "Index out of range":
        values_dict["🧑🏻‍🏭زره ساز"] = gg_zere
    if gg_sah != "Index out of range":
        values_dict["🧝‍♀️ساحره"] = gg_sah

    # Sort the dictionary by value
    sorted_values = sorted(values_dict.items(), key=lambda x: len(str(x[1])), reverse=True)

    # Create the message
    message = "\n".join([f"{key}: {value}" for key, value in sorted_values])

    # Send the message
    await update.message.reply_text(f'{m88}\n\n{message}')
    found_words = []







    # Count the occurrences of each result
    results = [gg_khabar, gg_bazpors, gg_esna, gg_tofang, gg_police, gg_kalantar, gg_qazi, gg_rish, gg_rad, gg_did, gg_doctor, gg_badi, gg_hero, gg_zere, gg_sah]
    result_counts = {}
    total_count = 0
    m390 = 'با توجه به جواب ها احتمال درست در اومدن نقطه شما به شرح زیر است:'
    m391 = 'من راهنماییم رو کردم، دیگه خود دانی🤷‍♂'

    for result in results:
        if result in result_counts:
            result_counts[result] += 1
        else:
            result_counts[result] = 1
        total_count += 1

    # Sort the results by count in descending order
    sorted_results = sorted(result_counts.items(), key=lambda x: x[1], reverse=True)

    # Build the response message
    response_message = ""
    for result, count in sorted_results:
        if result != "Index out of range":
            percentage = (count / total_count) * 100
            response_message += f"{result} نقطه ⬅️ {percentage:.2f}% \n"

    # Send the response message
    ioi = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ioi = c.fetchone()
    ioi = ioi[0]
    pop = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    pop = c.fetchone()
    pop = pop[0]
    await update.message.reply_text(f'{m390}\n\n{response_message}\n\n{m391}')
    await context.bot.send_message(chat_id= '5469541693', text= f'{pop}{ioi} از قابلیت محقق استفاده کرد')
    return ConversationHandler.END




async def MS5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global found_words
    await context.bot.send_message(chat_id=update.effective_chat.id, text='زمان برای ارسال به پایان رسید❌')
    found_words = []
    return ConversationHandler.END




conv_handler3 = ConversationHandler(
    entry_points=[MessageHandler(filters.FORWARDED & filters.Regex(r'^\🌞'), start_q)],
    states={
        SENDING_MASSEGE: [MessageHandler(filters.TEXT, javab_qeq)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, MS5)]
    },
    fallbacks=[],
    conversation_timeout= 45
)