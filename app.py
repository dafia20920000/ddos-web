from fastapi import FastAPI, Request
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.post("/api/download")
async def download_video(request: Request):
    data = await request.json()
    video_url = data.get('url')

    if not video_url:
        return {"success": False, "message": "No URL provided"}

    try:
        response = requests.get("https://tmate.cc/", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.content, 'html.parser')
        token = soup.find("input", {"name": "token"})["value"]
        
        post_data = {'url': video_url, 'token': token}
        response = requests.post("https://tmate.cc/download", data=post_data, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.content, 'html.parser')

        download_link = soup.find("a")["href"]  # Pastikan link ini benar

        return {"success": True, "video_url": download_link}
    except Exception as e:
        print(e)
        return {"success": False, "message": "Error processing video"}
