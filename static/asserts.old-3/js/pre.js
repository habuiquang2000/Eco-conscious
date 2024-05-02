document.addEventListener("DOMContentLoaded", function() {
    var currentPage = 1;
    var itemsPerPage = 10;
    var galleryItems = document.querySelectorAll('.gallery-img');

    function showPage(page) {
        var startIndex = (page - 1) * itemsPerPage;
        var endIndex = startIndex + itemsPerPage;
        galleryItems.forEach(function(item) {
            item.style.display = 'none';
        });

        for (var i = startIndex; i < endIndex && i < galleryItems.length; i++) {
            galleryItems[i].style.display = 'block';
        }
    }

    document.querySelector(".pagination li.page-item:nth-child(1) a.page-link").addEventListener("click", function(e) {
        e.preventDefault();
        if (currentPage > 1) {
            showPage(--currentPage);
        }
    });

    document.querySelector(".pagination li.page-item:nth-last-child(1) a.page-link").addEventListener("click", function(e) {
        e.preventDefault();
        if (currentPage < Math.ceil(galleryItems.length / itemsPerPage)) {
            showPage(++currentPage);
        }
    });

    showPage(currentPage);


    		
    var contactCount = document.getElementsByClassName("contact1").length;
    console.log("Số lượng phần tử có class 'contact1': " + contactCount);
    var details = document.getElementById("details");
    var detailsButton = document.getElementById("detailsButton");
    
    detailsButton.addEventListener("click", function() {
        if (details.style.display === "block") {
        details.style.display = "none"; 
                } else {
        details.style.display = "block"; 
        }
    });
});

	