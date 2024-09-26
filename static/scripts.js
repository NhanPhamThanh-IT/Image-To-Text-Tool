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