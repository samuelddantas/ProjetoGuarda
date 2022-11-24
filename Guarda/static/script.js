ScrollReveal({ 
    //reset: true,
    distance: '30px',
    duration: 1000,
    delay: 300
});

ScrollReveal().reveal('#first' , { delay: 100, origin: 'top' });

$(document).ready( function () {
    $( ".scroll_contant" ).mouseover (function () {
        $( this ).removeClass( "ellipsis" );
        var maxscroll =$( ".scroll_contant" ).width();
        var speed = maxscroll * 15;
        $( this ).animate( {
            scrollLeft: speed
        }, 20000, "linear" );
    } );

    $( ".scroll_contant" ).mouseout( function () {
        $( this ).stop();
        $( this ).addClass( "ellipsis" );
        $( this ).animate( {
            scrollLeft: 0
        }, 'fast' );
    } );
} );

$(document).ready(function() {
    $("#subir").hide();
    
    $('a#subir').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 250);
        return false;
});
    
$(window).scroll(function () {
    if ($(this).scrollTop() > 650) {
        $('#subir').fadeIn();
        } else {
        $('#subir').fadeOut();
        }
    });
});