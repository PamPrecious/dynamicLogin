$("#toggleSidebar").click(function (e) { 
    e.preventDefault();
    
    $(".sidebar").toggleClass("active");
    $(".content").toggleClass("active");
});

const toggle = document.getElementById('night');
const body = document.querySelector('body');
// const sideMenu = document.querySelector('sidebar-menu');
const sidebar = document.getElementById("sidebar");
const inner_content = document.querySelector(".inner-content");

toggle.addEventListener('click', function(){
    this.classList.toggle('la-moon-o');
    if(this.classList.toggle('la-sun-o')){
        body.style.background = 'white';
        // inner_content.style.background = 'white';
        body.style.color = 'black';
        sidebar.style.background = 'black';
        body.style.transition = '2s';
    }
    else{
        body.style.background = '#2a2a2a';
        body.style.color = 'white';
        sidebar.style.background = '#2a2a2a';
        // inner_content.style.background = '#cccccc';
        body.style.transition = '2s';
    }
})



// Show the overlay
function showOverlay() {
    document.getElementById("overlay").style.display = "block";
}

// Hide the overlay
function hideOverlay() {
    document.getElementById("overlay").style.display = "none";
}

// Add event listeners to show and hide the overlay
document.getElementById("show-overlay-button").addEventListener("click", showOverlay);
document.getElementById("close-overlay-button").addEventListener("click", hideOverlay);
