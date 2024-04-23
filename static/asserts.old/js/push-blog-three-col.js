jQuery(document).ready(function($) {
    "use strict";
    
 
    $("#postForm").submit(function(event) {
        event.preventDefault(); // Prevent the default form submission

        var formData = new FormData($("#postForm")[0]); // Serialize form data
        $.ajax({
            type: "POST",
            url: "https://8efa-117-5-225-221.ngrok-free.app/blog.html", // Thay đổi URL tại đây
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                // Send success message to parent window
                parent.postMessage({ success: true }, "*");
            },
            error: function(xhr, status, error) {
                // Send failure message to parent window
                parent.postMessage({ success: false }, "*");
            }
        });
    });

    window.addEventListener("message", function(event) {
        if (event.origin === "https://8efa-117-5-225-221.ngrok-free.app") {
            if (event.data && event.data.success) { // Check if event.data.success exists before accessing it
                // Success: Show success message
                alert("Đăng ký thành công!");
            } else {
                // Failure: Show error message
                alert("Đăng ký thất bại!");
            }
        }
    });
});
