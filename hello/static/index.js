
window.onload=function(){

var sidebar = document.getElementById("mySidebar")
var btn = document.getElementById("doom")
var main = document.getElementById("main")

btn.addEventListener("click",fur);


function fur() {
  
  if(sidebar.style.width == "0px"){

    sidebar.style.width = "250px";
    main.style.marginLeft = "250px";

  }
   
  else {
  
  sidebar.style.width = "0";
  main.style.marginLeft = "0";
  
}
}
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
