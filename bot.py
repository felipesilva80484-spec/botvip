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
    await context.bot.send_video(chat_id=update.effective_chat.id, video=open('video1.mp4', 'rb'), caption=TEXTO, reply_markup=InlineKeyboardMarkup(teclado))
    await context.bot.send_video(chat_id=update.effective_chat.id, video=open('video2.mp4', 'rb'))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
