var shortContent = function() {    
  if($(window).height() > $('#wrapper').height() + $('footer').height()) {
      $('footer').addClass('short-content');
  } else {
      $('footer').removeClass('short-content');
  }
};


$(document).ready(function() {
  shortContent();

  $(window).load(function() {
    shortContent();
  });

  $(window).resize(function() {
    shortContent();
  });
  $(window).on("orientationchange",function(){
    shortContent();
  });
});
