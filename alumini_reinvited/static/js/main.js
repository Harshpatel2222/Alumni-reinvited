// Sticky Navbar
$(window).scroll(function() {
    if ($(this).scrollTop() > 0) {
        $('.navbar').addClass('nav-sticky');
    } else {
        $('.navbar').removeClass('nav-sticky');
    }
});

// jQuery counterUp
$('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 2000
});