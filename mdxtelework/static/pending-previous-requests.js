document.addEventListener("DOMContentLoaded", function() {
    const pendingButton = document.getElementById("pending-button");
    const previousButton = document.getElementById("previous-button");
    const cardContainer = document.querySelector(".card-container");

    // Function to fetch and display pending requests
    function showPendingRequests() {
        fetch(pendingRequestsUrl)
            .then(response => response.text())
            .then(html => {
                // Extract content within .card-container
                const container = document.createElement("div");
                container.innerHTML = html;
                const newContent = container.querySelector(".card-container").innerHTML;
                cardContainer.innerHTML = newContent;
            });
    }    

    // Function to fetch and display previous requests
    function showPreviousRequests() {
        fetch(previousRequestsUrl)
            .then(response => response.text())
            .then(html => {
                // Extract content within .card-container
                const container = document.createElement("div");
                container.innerHTML = html;
                const newContent = container.querySelector(".card-container").innerHTML;
                cardContainer.innerHTML = newContent;
            });
    }

    // Event listener for pending button click
    pendingButton.addEventListener("click", function() {
        showPendingRequests();
    });

    // Event listener for previous button click
    previousButton.addEventListener("click", function() {
        showPreviousRequests();
    });

    // Initially show pending requests
    showPendingRequests();
});
