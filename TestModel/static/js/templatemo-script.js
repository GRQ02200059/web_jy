/*

TemplateMo 560 Astro Motion

https://templatemo.com/tm-560-astro-motion

*/

var gallery = undefined;

function closeMenu() {
  $(".navbar-collapse").removeClass("show"); 
}

function highlightMenu(no) {
  $(".navbar .navbar-nav > .nav-item").removeClass('selected');
  $(".navbar .navbar-nav > .nav-item > .nav-link[data-no='" + no + "']").parent().addClass('selected');
}





jQuery(function() {
    $('.tm-page-link').on('click', function(){
      var pageNo = $(this).data('page-no');
      highlightMenu(pageNo);
    });

    $(".navbar .navbar-nav > .nav-item > a.nav-link").on('click', function(e){
      var pageNo = $(this).data('no');

      highlightMenu(pageNo);
      closeMenu();     
    });

    $("html").click(function(e) {
      closeMenu();
    });
});