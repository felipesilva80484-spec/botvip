import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN", "8877927147:AAGiIXJ_IbyVDpdTdpGa4WZSCsvNNyjQ6Y8").strip()

TEXTO = "🚨 Somente AGORA Adquirindo acesso em nosso VIP 🌟 Você vai liberar 👇\n\n🤩 Novinhas gostosas BAIXA RENDA⁺ ¹⁸\n💀 Calu na N3t⁺¹⁸ & AmadOres⁺¹⁸\n🌸 Novinhas perdeno o cab4c0⁺¹⁸\n\n—————————99—————————\n🚀 Acesso imediato!\n🔞 CLIQUE AQUI E GARANTA SEU ACESSO 👇"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [[InlineKeyboardButton("🔞 GARANTIR MEU ACESSO VIP AGORA", url="https://zypher.global/pay/7oopEubn")]]
    markup = InlineKeyboardMarkup(teclado)
    
    try:
        await update.message.reply_video(video=open("video1.mp4", "rb"))
    except Exception as e:
        print(f"erro v1: {e}")
    try:
        await update.message.reply_video(video=open("video2.mp4", "rb"))
    except Exception as e:
        print(f"erro v2: {e}")

    await update.message.reply_text(TEXTO, reply_markup=markup)

async def post_init(app):
    await app.bot.delete_webhook(drop_pending_updates=True)

app = ApplicationBuilder().token(TOKEN).post_init(post_init).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
