from flask import Flask, request

app = Flask(__name__)

@app.route('/submit_info', methods=['GET'])
def submit_info():
    # Menerima parameter 'device' dan 'ip' yang dikirim melalui URL
    device_info = request.args.get('device')
    ip_info = request.args.get('ip')

    if device_info and ip_info:
        # Menampilkan informasi perangkat yang diterima
        print(f"Received Device Info: {device_info}, IP: {ip_info}")
        return "Info perangkat telah diterima!", 200
    else:
        return "Informasi perangkat tidak ditemukan.", 400

if __name__ == "__main__":
    app.run(debug=True)
