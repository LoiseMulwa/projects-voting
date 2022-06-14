function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }

$(document).ready(function(){
    $('form').submit(function(event){
      event.preventDefault()
    }) // End of submit event
  
  }) // End of document ready function