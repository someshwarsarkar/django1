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
document.getElementById("myBtn").addEventListener("click", openNav);

var menuState = 0 // close
function openNav() {
  if(menuState === 0){
     menuState = 1;
     document.getElementById("mySidebar").style.width = "250px";
     //document.getElementById("main").style.marginLeft = "250px";
     //document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  }
  else {
     menuState = 0;
     document.getElementById("mySidenav").style.width = "0";
     //document.getElementById("main").style.marginLeft = "0";
     //document.body.style.backgroundColor = "white";
  }
  console.log(menuState);
} 