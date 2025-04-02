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
    else if (/Android/.test(userAgent)) os = "Android";
    else if (/iPhone|iPad|iPod/.test(userAgent)) os = "iOS";
    document.getElementById('os').innerText = os;
}

function getBatteryStatus() {
    navigator.getBattery().then(function(battery) {
        document.getElementById('battery').innerText = Math.round(battery.level * 100) + "%";
    });
}

function getDeviceModel() {
    let userAgent = navigator.userAgent;
    let model = userAgent.match(/(.*?)/);
    document.getElementById('device').innerText = model ? model[1] : "Tidak Diketahui";
}

function downloadPDF() {
    const { jsPDF } = window.jspdf;
    let doc = new jsPDF();
    doc.text("Admin Panel Report", 10, 10);
    doc.text("IP: " + document.getElementById('ip').innerText, 10, 20);
    doc.text("OS: " + document.getElementById('os').innerText, 10, 30);
    doc.text("Model HP: " + document.getElementById('device').innerText, 10, 40);
    doc.text("Status Baterai: " + document.getElementById('battery').innerText, 10, 50);
    doc.text("Status Web: Online", 10, 60);
    doc.save("admin_report.pdf");
}

fetchIP();
getOS();
getBatteryStatus();
getDeviceModel();
