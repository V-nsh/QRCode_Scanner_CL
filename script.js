document.addEventListener('DOMContentLoaded', function () {
    const video = document.getElementById('scanner');
    const scanner = new Instascan.Scanner({ video });

    scanner.addListener('scan', function (content) {
        // Send the QR code data to the Python server
        sendQRCodeData(content);
    });

    Instascan.Camera.getCameras().then(function (cameras) {
        if (cameras.length > 0) {
            scanner.start(cameras[0]);
        } else {
            console.error('No cameras found.');
        }
    }).catch(function (error) {
        console.error(error);
    });

    function sendQRCodeData(qrCodeData) {
        // Send the QR code data to the Python server
        fetch('/api/qr-code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ qr_code_data: qrCodeData }),
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the server (if needed)
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
