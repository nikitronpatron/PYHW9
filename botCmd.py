## Калькулятор

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from log import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Привет {update.effective_user.first_name}.\n\n/calc - калькулятор, который выполняет:\nсложение: /calc a + b;\nвычитание: /calc a - b;\nумножение /calc : a * b;\nделение /calc a / b;\nвозведение в степень: a ** b.\n\n/complex - калькулятор для комплексных чисел:\nсложение: /complex a + b;\nвычитание: /complex a - b;\nумножение /complex : a * b;\nделение /complex a / b;')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    tmp = msg.split()
    a = int(tmp[1])
    b = int(tmp[3])
    c = tmp[2]
    if c == "+":
        res = a + b
    elif c == "-":
        res = a - b
    elif c == "/":
        res = a / b
    elif c == "*":
        res = a * b
    elif c == "**":
        res = a ** b
    await update.message.reply_text(f'{a} {c} {b} = {res}')


async def complexCalc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    tmp = msg.split()
    a = int(tmp[1])
    b = int(tmp[3])
    c = tmp[2]
    if c == "+":
        await update.message.reply_text(f'{a} {c} {b}i')
    elif c == "-":
        await update.message.reply_text(f'{a} {c} {b}i')
    elif c == "/":
        res = a / b
        await update.message.reply_text(f'{a} {c} {b}i = {-res}i')
    elif c == "*":
        res = a * b
        await update.message.reply_text(f'{a} {c} {b}i = {res}i')