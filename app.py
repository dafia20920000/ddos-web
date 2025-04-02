from flask import Flask, request, render_template

app = Flask(__name__)

# Simulasi penyimpanan data perangkat yang diterima
devices_info = []

@app.route('/submit_info', methods=['GET'])
def submit_info():
    # Menerima parameter 'device' dan 'ip' yang dikirim melalui URL
    device_info = request.args.get('device')
    ip_info = request.args.get('ip')

    if device_info and ip_info:
        # Menyimpan informasi perangkat ke dalam daftar
        devices_info.append({'device': device_info, 'ip': ip_info, 'status': 'Terkirim'})
        print(f"Data diterima: Model: {device_info}, IP: {ip_info}")
        return "Info perangkat telah diterima!", 200
    else:
        return "Informasi perangkat tidak ditemukan.", 400

@app.route('/')
def index():
    # Menampilkan halaman utama dengan daftar perangkat yang diterima
    return render_template('index.html', devices_info=devices_info)

if __name__ == "__main__":
    app.run(debug=True)
