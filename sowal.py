from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
import sqlite3
import re
from telegram.ext import ContextTypes , ConversationHandler, CommandHandler, filters, MessageHandler
# from msg import keyboard


sss = None


SOWAL1 = 1
SOWAL2 = 2
SOWAL3 = 3



keyboard = [
    [KeyboardButton('🎮 بازی ها')],
    [KeyboardButton('📩 پیام خصوصی'), KeyboardButton('🚣 چالش'),KeyboardButton('🌐 پیام همگانی')],
    [KeyboardButton('🎰 کازینو'), KeyboardButton('🏎 مسابقه'), KeyboardButton('🎲 جایزه روزانه')],
    [KeyboardButton('🪪 پروفایل'), KeyboardButton('🎁 دعوت دوستان'), KeyboardButton('🗂 تسک')],
    [KeyboardButton('👨‍💻 پیام به ادمین'), KeyboardButton('📚 راهنما')]]





conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()

async def sowal1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    await update.message.reply_text('''🚣 در قسمت چالش شما یک سوال طرح میکنید و جوابش رو به ربات میگویید و بعد تعیین میکنید که میخواهید به کسی که جواب درست به سوالتون داد چند سکه جایزه بدید. 
سوال شما به صورت خودکار در کانال @dohat_nime فرستاده میشه و کسی که به اون سوال جواب درست داد سکه به پروفایلش اضافه میشه''')
    if sss != None:
        await update.message.reply_text('❌هنوز کسی به سوال قبلی جواب درست نداده است')
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
    uuc = c.execute(f"SELECT etc FROM users WHERE user_id=6364622155")
    uuc = c.fetchone()
    uuc = uuc[0]
    if uuc == 1:
        await context.bot.send_message(chat_id=user_id , text='🔐در حال حاضر این قابلیت قفل است')
        return ConversationHandler.END
    qq = c.execute(f"SELECT admin_block FROM users WHERE user_id={user_id}")
    qq = c.fetchone()
    qq = qq[0]
    if qq == 1:
        await context.bot.send_message(chat_id=user_id , text='❌شما توسط ادمین بن شدید، برای رفع بن به ادمین پیام بدید')
        return ConversationHandler.END
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    await update.message.reply_text('❓سوال مورد نظرت رو بنویس', reply_markup=reply)
    return SOWAL1


async def sowal2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        ff = update.message.text
        context.user_data['ff'] = ff
        await update.message.reply_text('💡جواب سوال چی میشه؟')
        return SOWAL2
    except:
        await update.message.reply_text("""❌ارسال نشد""")


async def sowal3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    xx = update.message.text
    context.user_data['xx'] = xx
    iyt = '💳به کسی که به سوالت پاسخ درست بده میخوای چند سکه جایزه بدی؟'
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    await update.message.reply_text(iyt, reply_markup=reply)
    return SOWAL3





async def sowal4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    username = update.message.from_user.username
    global sss
    bb = update.message.text
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    uii = c.execute(f"SELECT Khas FROM users WHERE user_id={user_id}")
    uii = c.fetchone()
    uii = uii[0]
    uu = c.execute(f"SELECT Lig FROM users WHERE user_id={user_id}")
    uu = c.fetchone()
    uu = uu[0]
    if bb.isdigit():
        if float(bb) > vv:
            await update.message.reply_text('''❌موجودی کافی نیست

چی جوری سکه بگیرم؟👇
/getcoin''')
            return
        if float(bb) < 0.5:
            await update.message.reply_text('حداقل 0.5 سکه')
            return
        if float(bb) > 15:
            await update.message.reply_text('❌ حداکثر 15 سکه است')
            return
    if sss != None:
        await update.message.reply_text('❌یک نفر قبل شما سوال جدید ثبت کرده است', reply_markup=reply_markup)
        return ConversationHandler.END
    vv = c.execute(f"SELECT coin FROM users WHERE user_id={user_id}")
    vv = c.fetchone()
    vv = vv[0]
    if vv == None:
        vv = 0
    yy = float(vv) - int(bb)
    c.execute(f"UPDATE users SET coin={yy} WHERE user_id={user_id}")
    conn.commit()
        
    xx = context.user_data['xx'] 
    sss = f'{xx} {bb}'
    ff = context.user_data['ff'] 
    response = ""
    for word in xx.split():
        response += "➖" * len(word) + "   "
    await context.bot.send_message(chat_id="-1002221581695", text=f"""❓سوال: {ff}

💡جواب: {response.strip()}

💰جایزه: {bb} سکه

🥸سوال از: {uu}{uii}

🎁تو قسمت پیام همگانی میتونید به این سوال پاسخ بدید
درصورتی که پاسخ درست دادید سکه به پروفایل شما اضافه میشه

🤖 @sahere_bmola_bot""")
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('✅سوال در کانال فرستاده شد\n\nمشاهده سوال 👈 @dohat_nime', reply_markup=reply_markup)
    return ConversationHandler.END


async def cancsowal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("🏠صفحه اصلی", reply_markup=reply_markup)
    return ConversationHandler.END





conv_handler28 = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex(re.compile(r'^🚣 چالش$')), sowal1)],
    states={
        SOWAL1: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$') , sowal2),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), cancsowal)],
        SOWAL2: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$') , sowal3),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), cancsowal)],
        SOWAL3: [MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'^❌بازگشت$') , sowal4),
            MessageHandler(filters.Regex(r'^❌بازگشت$'), cancsowal)],
        ConversationHandler.TIMEOUT:[MessageHandler(filters.TEXT, cancsowal)]
    },
    fallbacks=[CommandHandler('cancel', cancsowal)],
    conversation_timeout= 120
)


