/*!
    * Start Bootstrap - Creative v6.0.2 (https://startbootstrap.com/themes/creative)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap-creative/blob/master/LICENSE)
    */

$(".favorite-button").on("click", function (e) {
  e.preventDefault();
  $.ajax({
    type: "POST",
    contentType: "application/json; charset=utf-8",
    url: "/question_handler",
    traditional: "true",
    data: JSON.stringify({ user_input_value }),
    dataType: "json"
  }).done(
    function (data) {
      if (data == "ZERO_RESULTS") {
        chat.appendChild(newGrandpyText).innerHTML = getRandomText(no_result);
      } else if (data == "ignore") {
        chat.appendChild(newGrandpyText).innerHTML = ":)";
      } else if (data == "error") {
        chat.appendChild(newGrandpyText).innerHTML = "Une erreur innatendue est survenue. Merci de réessayer ultérieurement.";
      } else {
        chat.appendChild(newGrandpyText).innerHTML = (getRandomText(answer1) + "<br>" + getRandomText(answer2) + data[0] + "<br>" + "<br>" + getRandomText(anecdote) + data[2]);
        myLatLng = data[1];
        initMap();
      }
    }).fail(
      function (jqXHR, textStatus) {
        chat.appendChild(newGrandpyText).innerHTML = "Oups il y a eu une erreur, vérifie ta connexion internet et réessaye.";
      }).then(
        function () {
          updateScroll();
        });

  //  //  //  //  //  //  //  //  //

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

    // Closes responsive menu when a scroll trigger link is clicked
    $('.js-scroll-trigger').click(function () {
      $('.navbar-collapse').collapse('hide');
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
      target: '#mainNav',
      offset: 75
    });

    /*
      // Collapse Navbar
      var navbarCollapse = function() {
        if ($("#mainNav").offset().top > 100) {
          $("#mainNav").addClass("navbar-scrolled");
        } else {
          $("#mainNav").removeClass("navbar-scrolled");
        }
      };
    */

    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);

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
})
