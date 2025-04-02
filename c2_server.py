import socket
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Konfigurasi Bot Telegram
TELEGRAM_BOT_TOKEN = "8050641668:AAEytFzgrSClXd5ARv35WFjfMNXGpGA5mr4"

# Fungsi untuk menjalankan server C2
def start_c2_server(host='0.0.0.0', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")
    
    while True:
        client_socket, addr = server.accept()
        print(f"[*] Connection established with {addr}")
        client_socket.send(b"Welcome to C2 Server!\n")
        client_socket.close()

# Fungsi untuk start bot Telegram
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot aktif! Kirim /start_server untuk menjalankan C2 Server.")

# Fungsi untuk menjalankan server C2 dari Telegram
def start_server(update: Update, context: CallbackContext):
    update.message.reply_text("Starting C2 Server...")
    start_c2_server()

# Fungsi utama untuk menjalankan bot Telegram
def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("start_server", start_server))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
