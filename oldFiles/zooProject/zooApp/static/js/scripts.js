$(document).ready(function() {
    // using the button tag hide and show the p tags
    $('#hide').click(function(){
        $('p').hide();
    })
    $('#show').click(function(){
        $('p').show();
    })

    // using the octocat class create an alert that states the user clicked on an octocat
    $('.octocat').click(function(){
        alert('You hovered over an Octocat!')
    })

    // add a color class to the h1 tag
    $('h1').click(function() {
        $('h1').css('color', 'purple');
    })

    // Fade in nav links
    $('#topics').click(function(){
        $('a').fadeIn();
    })
    
    // Face in and out an img
    $('.bee').hover(function(){
        $('.bee').fadeOut();
    })
    $('#fadeInImg').hover(function(){
        $('.bee').fadeIn();
    })

    // Adding in text with out an event
    $('#append').append('We are adding text using jQuery!')

    // add more text to the h3 tag using an event
    $('#append').prepend("What's up?")


    // Bonus after class magic
    $('.magic').click(function(){
        $('img').animate( {
            width: 'toggle'
        })
    })
})
/*
1. declare a function
2. give instructions - hide just p tags

*/