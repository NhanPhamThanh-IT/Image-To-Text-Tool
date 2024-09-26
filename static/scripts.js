function previewImage(event) {
    const file = event.target.files[0];
    const preview = document.getElementById('preview');
    const notification = document.getElementById('notification-box');
    const result = document.getElementById('result-box');
    if (notification) notification.style.display = 'none';
    if (result) result.style.display = 'none';
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    } else {
        preview.style.display = 'none';
    }
}

function copyContent() {
    var content = document.getElementById('content').innerText;
    navigator.clipboard.writeText(content).then(function() {
        var notification = document.getElementById('copy-notification');
        notification.style.display = 'block';
        setTimeout(function() {
            notification.style.display = 'none';
        }, 1000);
    }, function(err) {
        alert('An error occurred while copying the content: ' + err);
    });
}
