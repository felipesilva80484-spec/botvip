import os
from threading import Thread
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8877927147:AAGiIXJ_IbyVDpdTdpGa4WZSCsvNNyjQ6Y8"

TEXTO = """🚨 Somente AGORA Adquirindo acesso em nosso VIP 🌟 Você vai liberar 👇

🤩 Novinhas gostosas BAIXA RENDA⁺ ¹⁸
💀 Calu na N3t⁺¹⁸ & AmadOres⁺¹⁸
🌸 Novinhas perdeno o cab4c0⁺¹⁸

—————————99—————————
🚀 Acesso imediato!
🔞 CLIQUE AQUI E GARANTA SEU ACESSO 👇"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [[InlineKeyboardButton("🔞 GARANTIR MEU ACESSO VIP AGORA", url="https://zypher.global/pay/7oopEubn")]]
    try:
        await context.bot.send_video(chat_id=update.effective_chat.id, video=open('video1.mp4', 'rb'), caption=TEXTO, reply_markup=InlineKeyboardMarkup(teclado))
        await context.bot.send_video(chat_id=update.effective_chat.id, video=open('video2.mp4', 'rb'))
    except:
        await update.message.reply_text(TEXTO, reply_markup=InlineKeyboardMarkup(teclado))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return "Bot Online"

def run_flask():
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

if __name__ == "__main__":
    Thread(target=run_flask).start()
    app.run_polling()
