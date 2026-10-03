import os
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN", "8877927147:AAGiIXJ_IbyVDpdTdpGa4WZSCsvNNyjQ6Y8").strip()

VIDEO1_URL = "https://files.catbox.moe/42eic1.mp4"
VIDEO2_URL = "https://files.catbox.moe/qqzape.mp4"

TEXTO = "🚨 Somente AGORA Adquirindo acesso em nosso VIP 🌟 Você vai liberar 👇\n\n🤩 Novinhas gostosas BAIXA RENDA⁺ ¹⁸\n💀 Calu na N3t⁺¹⁸ & AmadOres⁺¹⁸\n🌸 Novinhas perdeno o cab4c0⁺¹⁸\n\n—————————99—————————\n🚀 Acesso imediato!\n🔞 CLIQUE AQUI E GARANTA SEU ACESSO 👇"

def baixar(url, nome):
    r = requests.get(url, timeout=60)
    open(nome, "wb").write(r.content)
    return nome

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("🔞 GARANTIR MEU ACESSO VIP AGORA", url="https://zypher.global/pay/7oopEubn")]]
    markup = InlineKeyboardMarkup(kb)

    try:
        v1 = baixar(VIDEO1_URL, "/tmp/v1.mp4")
        await update.message.reply_video(video=open(v1, "rb"), supports_streaming=True, width=720, height=1280)
    except Exception as e:
        print(f"erro v1 {e}")
        await update.message.reply_video(video=VIDEO1_URL)

    try:
        v2 = baixar(VIDEO2_URL, "/tmp/v2.mp4")
        await update.message.reply_video(video=open(v2, "rb"), supports_streaming=True, width=720, height=1280)
    except Exception as e:
        print(f"erro v2 {e}")
        await update.message.reply_video(video=VIDEO2_URL)

    await update.message.reply_text(TEXTO, reply_markup=markup)

async def post_init(app):
    await app.bot.delete_webhook(drop_pending_updates=True)

app = ApplicationBuilder().token(TOKEN).post_init(post_init).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
