$( document ).ready(function() {
    var searchButton = document.getElementById("search-button");
    searchButton.addEventListener('click', function (event) {
        $("#small-screen-search").slideToggle();
        console.log(css);
    });
});