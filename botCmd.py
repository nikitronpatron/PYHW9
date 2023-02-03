## Калькулятор

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from log import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    tmp = msg.split()
    a = float(tmp[1])
    b = float(tmp[3])
    c = tmp[2]
    if c == "+":
        res = a + b
    elif c == "-":
        res = a - b
    elif c == "/":
        res = a / b
    elif c == "*":
        res = a * b
    await update.message.reply_text(f'{a} {c} {b} = {res}')
