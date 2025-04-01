from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    video_url = data.get('url')

    if not video_url:
        return jsonify({'success': False, 'message': 'No URL provided'})

    try:
        # Logic to fetch and process the TikTok video using requests and BeautifulSoup
        response = requests.get("https://tmate.cc/", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.content, 'html.parser')
        token = soup.find("input", {"name": "token"})["value"]
        
        post_data = {'url': video_url, 'token': token}
        response = requests.post("https://tmate.cc/download", data=post_data, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.content, 'html.parser')

        download_link = soup.find("a")["href"]  # Assuming this is the correct link to the video

        return jsonify({'success': True, 'video_url': download_link})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'message': 'Error processing video'})

if __name__ == '__main__':
    app.run(debug=True)
