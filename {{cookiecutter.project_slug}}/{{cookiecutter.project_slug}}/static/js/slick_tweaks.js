function slick_reload(selector) {
  $(selector).each(function(index, element) {
    element.slick.refresh();
    // element.slick('setPosition');
    // $(selector).slickSetOption(null, null, true);
    // $(selector)[0].slick.slickSetOption(null, null, true);
  });
  $(selector).slick('setPosition');
}


function slick_price_reload() {
  slick_reload('.slick-price');
  // $('.slick-price').slick('setPosition');
}


function onDoneResizing() {
  slick_reload(".slick");
  // alignSlickArrows();
}

/* 
  this function aligns slick arrows to the middle of the reference DOM object (if provided)

  bind slick events ("init", "reInit", "setPosition") to this function to automatically recalculate arrow position when slick changes its shape and size.
 */
function alignSlickArrows() {
  // auto aligning slick sliders
  $(".slick-slider").each(function(slider_num, slider) {
    var refs = $(slider).find(".slick-reference");
    if (null != refs) {
      var max_height = Math.max.apply(Math, refs.map(function(){return this.height;}));
      var button_top = max_height / 2;

      buttons = $(slider).find("button.slick-arrow");

      buttons.map(function() {
        $(this).css("top", button_top);        
      });

    }  
  });
}


$(document).ready(function() {
  var id;
  $(window).resize(function() {
      clearTimeout(id);
      id = setTimeout(onDoneResizing, 500);
  });
});
