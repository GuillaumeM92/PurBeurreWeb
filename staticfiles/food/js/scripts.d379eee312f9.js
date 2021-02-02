// jquery ajax call to add a product to the user favorites
$(".favorite-button").on("click", function (e) {
  e.preventDefault();

  let searched_product_id = this.getAttribute("productID");
  let substitute_id = this.value;
  let is_authenticated = this.getAttribute("isAuthenticated");
  let email = this.getAttribute("user");
  let status = this.getAttribute("name");

  if (is_authenticated == "True") {

    $.ajax({
      data: { searched_product_id, substitute_id, is_authenticated, email, status },
      type: $(this).attr("method"), // GET or POST
      url: "/favorite",
      success: function (response) { },
      error: function (response) {
        alert("an error occured");
      }
    });

    if (status == "add-favorite") {
      this.innerHTML = "<span style='color:teal; margin:5px'> Produit ajouté aux favoris ! </span>";
    } else {
      this.innerHTML = "<span style='color:teal; margin:5px'> Produit retiré des favoris ! </span>";
    }
  }

  else {
    console.log("user is not authenticated")
    this.innerHTML = "<span> Vous devez être connecté pour ajouter un produit aux favoris ! </span>";
  }
});

/*!
    * Start Bootstrap - Creative v6.0.2 (https://startbootstrap.com/themes/creative)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap-creative/blob/master/LICENSE)
    */


(function ($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({

          scrollTop: (target.offset().top - 72)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 75
  });

  // Magnific popup calls
  $('#portfolio').magnificPopup({
    delegate: 'a',
    type: 'image',
    tLoading: 'Loading image #%curr%...',
    mainClass: 'mfp-img-mobile',
    gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1]
    },
    image: {
      tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
    }
  });

})(jQuery);
