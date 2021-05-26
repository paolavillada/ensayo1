/*global $ */
//Almacenando slider en una variable 
var slider = $('#slider');

//Almacenar botones
var siguiente = $('#btn-next');
var anterior = $('#btn-prev');

//Mover ultima imagen al primer lugar
$('#slider section:last').insertBefore('#slider section:first');
// Mostrar la primera imagen con un margen de -100%
slider.css('margin-left', '-'+100+'%');

function moverD() {
    slider.animate({
        marginLeft:'-'+200+'%'
    }  ,700, function(){
        $('#slider section:first').insertAfter('#slider section:last');
        slider.css('margin-left', '-'+100+'%');       
    });    
}

function moverI() {
    slider.animate({
        marginLeft:0
    }  ,700, function(){
        $('#slider section:last').insertBefore('#slider section:first');
        slider.css('margin-left', '-'+100+'%');    
        
    });    
}

siguiente.on('click',function () {
    moverD();
});

anterior.on('click',function () {
    moverI();
});

function autoplay() {
    interval = setInterval(function(){
        moverD();
    }, 5000);
}

autoplay();
