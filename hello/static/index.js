/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
/*function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
/*function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}
/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar 
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}*/
 // SideNav Button Initialization
    $(".button-showSide").sideNav();
    // SideNav Scrollbar Initialization
    var sideNavScrollbar = document.querySelector('.custom-scrollbar');
    Ps.initialize(sideNavScrollbar);

$('.button-showSide').click( function() {
    $('#openSideBar').hide();
    $('#closeSideBar').show();
});

$('.button-hideSide').click( function() {
    // Check to make sure the side nav wasn't closed by clicking off the menu
    // If it was clicked off, the #closeSideBar div is still showing
    if ( $('#sidenav-overlay').length ) {
        // It's open and we need to close it
        $('#sidenav-overlay').remove();
        $('#slide-out').attr('style', 'transform: translateX(-100%); transition: all 200ms cubic-bezier(0.25, 0.46, 0.45, 0.94)');
        $('#closeSideBar').hide();
        $('#openSideBar').show();
    } else {
        // It was most likely clicked off and needs to be re-opened
        $('#openSideBar a').trigger('click');
    }
});