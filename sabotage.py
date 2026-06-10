from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
import sqlite3
import re
from telegram.ext import ContextTypes , ConversationHandler, CommandHandler, filters, MessageHandler, ApplicationBuilder


keyboard = [
    [KeyboardButton('📩 پیام خصوصی'),KeyboardButton('🌐 پیام همگانی')],
    [KeyboardButton('🎰 کازینو'), KeyboardButton('🏎 مسابقه'), KeyboardButton('🎲 جایزه روزانه')],
    [KeyboardButton('🪪 پروفایل'), KeyboardButton('🗂 تسک')],
    [KeyboardButton('👨‍💻 پیام به ادمین'), KeyboardButton('📚 راهنما')]]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='سلام', reply_markup=reply)




async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply = ReplyKeyboardMarkup([['❌بازگشت']], resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='سلام', reply_markup=reply)




async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='سلام', reply_markup=reply)


app = ApplicationBuilder().token("7216952739:AAEupGEYaqKTspCqNznUwX__GjndwVOvICE").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Regex(re.compile(r'^🌐 پیام همگانی$')), hello))
app.add_handler(MessageHandler(filters.ALL & ~filters.Regex(r'^🌐 پیام همگانی$') , bye))

app.run_polling()