function downloadVideo() {
    const videoUrl = document.getElementById('video-url').value;
    const videoDisplay = document.getElementById('video-display');
    videoDisplay.style.display = 'none';  // Hide video display initially

    if (videoUrl) {
        // Send the video URL to the backend for processing
        fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: videoUrl })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Show the video after successful download
                const videoElement = document.createElement('video');
                videoElement.src = data.video_url;
                videoElement.controls = true;
                videoDisplay.innerHTML = '';
                videoDisplay.appendChild(videoElement);
                videoDisplay.style.display = 'block';
            } else {
                alert('Error downloading video.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error. Please try again.');
        });
    } else {
        alert('Please enter a valid TikTok video URL.');
    }
}

function contactUs() {
    const phoneNumber = '+6288802110544'; // Replace with your actual phone number
    window.open(`https://wa.me/${phoneNumber}`, '_blank');
}
