from flask import Flask, request
import random
import string
import requests

app = Flask(__name__)

# Ganti dengan token bot Telegram Anda
TELEGRAM_TOKEN = '8050641668:AAEytFzgrSClXd5ARv35WFjfMNXGpGA5mr4'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received message:", data)
    
    # Ambil ID chat dan pesan
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    # Jika perintah /buat link diberikan, buat link acak
    if text.lower().startswith("/buat link"):
        random_link = generate_random_link()
        send_message(chat_id, f"Link acak Anda: {random_link}")
        
    return 'OK', 200

def generate_random_link(length=10):
    """Generate random alphanumeric link"""
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return f'https://yourdomain.com/{random_string}'

def send_message(chat_id, text):
    """Send a message to Telegram"""
    requests.post(f'{TELEGRAM_API_URL}sendMessage', data={
        'chat_id': chat_id,
        'text': text
    })

if __name__ == '__main__':
    app.run(debug=True)
