from flask import Flask, request

app = Flask(__name__)

@app.route('/submit_info', methods=['GET'])
def submit_info():
    device_info = request.args.get('device')
    # Di sini, kamu bisa menyimpan atau menampilkan informasi perangkat ke panel admin
    print(f"Received Device Info: {device_info}")
    return "Info telah diterima!", 200

if __name__ == "__main__":
    app.run(debug=True)
