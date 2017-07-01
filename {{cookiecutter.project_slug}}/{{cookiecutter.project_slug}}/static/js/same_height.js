var sameHeight = function() {
    $('.row-same-height').each(function(i, elem) {
        $(elem)
            .find('.same-height')   // Only children of this row
            // .find('.col-height')   // Only children of this row
            .matchHeight({byRow: false}); // Row detection gets confused so disable it
    });
};

$(document).ready(function() {
  sameHeight();

  $(window).load(function() {
    sameHeight();
  });

  $(window).resize(function() {
    sameHeight();
  });
  $(window).on("orientationchange",function(){
    sameHeight();
  });
});
