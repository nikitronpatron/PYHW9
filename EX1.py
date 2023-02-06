from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from botCmd import *

app = ApplicationBuilder().token("6063923731:AAGaYTf6oNnAZ96bIVR7pdXNzrO269--KEQ").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("complex", complexCalc))

app.run_polling()