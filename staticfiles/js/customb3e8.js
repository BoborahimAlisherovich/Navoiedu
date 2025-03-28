$(function () {
    var url = window.location.pathname,
        urlRegExp = new RegExp(url.replace(/\/$/, '') + "$");
    $('#mainNav a').each(function () {
        if (urlRegExp.test(this.href.replace(/\/$/, ''))) {
            $(this).addClass('active');
        }
    }); 
    /*$('.bxslider').show().bxSlider({
  mode:'fade',
  auto: true,
  pause: 8000,
  adaptiveHeight: true,
  preloadImages: 'all',
  pager: false,
  captions: false
});   
$("#scroller").jCarouselLite({
        vertical: true,
        hoverPause:true,
        visible:3,
        auto: 3000,
        speed:1000,
        scroll: 1
    });*/
     $("a.btn-adaptive").click(function() {
        var a = $(this).attr("href");
        OpenWindow(a, 350, 568, "media");
        return false
    });
      var top_header =$( '.top-header' ).parent().height();
     var containet =$( '.slider' ).height();  
    //window.innerHeight - footer + 178;
      var height_parent=  $( '.slider' ).height();
		$( '#slider' ).sliderPro({
            width: "100%",
        	height: 450,
        	arrows: true,
            buttons: true,
        	waitForLayers: true,
        	autoplay: true,
        	autoScaleLayers: false,
            autoplayDelay:4000,  
            autoplayOnHover: 'none',   
            breakpoints: {
            620:{
                height: 350,
            },
            420:{
                height: 250,
            } 
            }       
		});
        if ($(window).width() < 568){
            
        }
        //var owl = jQuery("#owl-tariff");
        $('#owl-links').owlCarousel({                
            responsiveClass:true,
            items: 1,
            loop:true,
            /* responsive:{
                0:{items:1},
                360:{items:1,  margin: 0,},
                400:{items:1,  margin: 0},
                600:{items:2, margin: 0},
                768:{items:2,  margin: 60,},
                1200:{items:3,  margin: 60,}
            },*/
            autoHeight:true,
            autoWidth:false,       
            dots: true,        
            nav: false,
            autoplay:true,
            autoplayTimeout:5000,
    autoplayHoverPause:true
        });
        
        $('#owl-advert').owlCarousel({                
            responsiveClass:true,
            items: 1,
            singleItem: true,
            loop:true,
            /* responsive:{
                0:{items:1},
                360:{items:1,  margin: 0,},
                400:{items:1,  margin: 0},
                600:{items:2, margin: 0},
                768:{items:2,  margin: 60,},
                1200:{items:3,  margin: 60,}
            },*/
            autoHeight:false,
            autoWidth:false,       
            dots: true,        
            nav: false,
            autoplay:true,
            autoplayTimeout:5000,
    autoplayHoverPause:true
        });

});

        
           function validate(evt) {
    var theEvent = evt || window.event;
    var key = theEvent.keyCode || theEvent.which;
   // console.log(key);
    key = String.fromCharCode( key );
    var regex = /[0-9\+\()]|\./;
    if( !regex.test(key)) {
      theEvent.returnValue = false;
      if(theEvent.preventDefault) theEvent.preventDefault();
    }
  }
  $(document).ready(function() {
    $("[id^=edit]").keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
             // Allow: Ctrl/cmd+A
            (e.keyCode == 65 && (e.ctrlKey === true || e.metaKey === true)) ||
             // Allow: Ctrl/cmd+C
            (e.keyCode == 67 && (e.ctrlKey === true || e.metaKey === true)) ||
             // Allow: Ctrl/cmd+X
            (e.keyCode == 88 && (e.ctrlKey === true || e.metaKey === true)) ||
             // Allow: home, end, left, right
            (e.keyCode >= 35 && e.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });
});
function OpenWindow(b, d, a, c) {
    if (!c) {
        c = window
    }
    if (!d) {
        d = 800
    }
    if (!a) {
        a = 600
    }
    var f = (screen.width - d) / 2;
    var e = window.open(b, c, "left=" + f + ",top=100,width=" + d + ",height=" + a + ",directories=no,menubar=no,status=yes,resizable=yes,scrollbars=yes,toolbar=no");
    if (e.opener == null) {
        e.opener = self
    }
    e.focus()
}
jQuery( document ).ready( function( $ ) {
    'use strict';
	//// ---> Check issue element
	jQuery.fn.exists = function() {
	  return jQuery(this).length;
	}
	/* Animations for blocks */	
	window.sr = ScrollReveal();
	if($('.js-uni-animated').exists()){
		sr.reveal( '.js-uni-animated', {
			origin: 'bottom',
			duration: 800,
			delay: 0,
			distance: '100px',
			easing: 'ease',
			scale: 1
		});	
	}
	if($('.js-uni-animated-first').exists()){
		sr.reveal( '.js-uni-animated-first', {
			origin: 'top',
			duration: 800,
			delay: 0,
			distance: '80px',
			easing: 'ease',
			scale: 1
		});
	}
	if($('.js-uni-animated-second').exists()){
		sr.reveal( '.js-uni-animated-second', {
			origin: 'bottom',
			duration: 800,
			delay: 200,
			distance: '80px',
			easing: 'ease',
			scale: 1
		});
	}
    if($('.js-animated-bottom').exists()){
		sr.reveal( '.js-animated-bottom', {
			origin: 'bottom',
			duration: 800,
			delay: 300,
			distance: '80px',
			easing: 'ease',
			scale: 1
		});	
	}
	if($('.js-uni-animated-third').exists()){
		sr.reveal( '.js-uni-animated-third', {
			origin: 'left',
			duration: 800,
			delay: 300,
			distance: '80px',
			easing: 'ease',
			scale: 1
		});	
	}
});
var region = ["Қорақалпоғистон", "Андижон", "Бухоро", "Жиззах", "Қашқадарё", "Навоий", "Наманган", "Самарқанд", "Сурхондарё", "Сирдарё", "Тошкент в.", "Фарғона", "Хоразм"],
factories_list = [
        {
                "id": 0,
                "factories": [{"id": 170, "name": "Юлдуз пахта тозалаш АЖ"}, {"id": 171, "name": "Ходжейли таласы пахта тозалаш АЖ"}, {"id": 174, "name": "Беруний пахта тозалаш АЖ"}, {"id": 176, "name": "Турткуль ок олтин пахта тозалаш АЖ"}, {"id": 177, "name": "Халкабад мамыгы пахта тозалаш АЖ"}, {"id": 180, "name": "Элликкала олтин толаси пахта тозалаш АЖ"}] 
        },
        {
                "id": 1,
                "factories": [{"id": 61, "name": "Андижон-1 пахта тозалаш АЖ"}, {"id": 62, "name": "Андижон-3 пахта тозалаш АЖ"}, {"id": 66, "name": "Асака-2 пахта тозалаш АЖ"}, {"id": 454, "name": "Укчи пахта тозалаш МЧЖ"}, {"id": 67, "name": "Шахрихон пахта тозалаш АЖ"}, {"id": 68, "name": "Пайтуг пахта тозалаш АЖ"}, {"id": 69, "name": "Суфикишлок пахта тозалаш АЖ"}, {"id": 70, "name": "Буз пахта тозалаш АЖ"}, {"id": 59, "name": "Чинобод пахта тозалаш АЖ"}, {"id": 53, "name": "Хужаобод пахта тозалаш АЖ"}] 
        },
        {
                "id": 2,
                "factories": [{"id": 101, "name": "Когон Олтин тола пахта тозалаш АЖ"}, {"id": 102, "name": "Бухоро пахта тозалаш АЖ"}, {"id": 104, "name": "Коракул пахта тозалаш АЖ"}, {"id": 105, "name": "Гиждувон пахта тозалаш АЖ"}, {"id": 110, "name": "Пешку пахта тозалаш АЖ"}, {"id": 111, "name": "Шофиркон пахта тозалаш АЖ"}, {"id": 112, "name": "Ромитан пахта тозалаш АЖ"}, {"id": 115, "name": "Жондор пахта тозалаш АЖ"},{"id": 100, "name": "Олот пахта тозалаш МЧЖ"}] 
        },
        {
                "id": 3,
                "factories": [{"id": 79, "name": "Дустлик пахта тозалаш АЖ"}, {"id": 58, "name": "Уч-тепа пахта тозалаш АЖ"}, {"id": 57, "name": "Пахтакор пахта тозалаш АЖ"}, {"id": 55, "name": "Даштабод пахта тозалаш АЖ"}, {"id": 56, "name": "Зафаробод пахта тозалаш АЖ"}, {"id": 366, "name": "Зарбдор пахта тозалаш АЖ"}] 
        },
        {
                "id": 4,
                "factories": [{"id": 121, "name": "Шахрисабз пахта тозалаш АЖ"}, {"id": 137, "name": "Яккабог пахта тозалаш АЖ"}, {"id": 125, "name": "Косон пахта тозалаш АЖ"}, {"id": 127, "name": "Камаши пахта тозалаш АЖ"}, {"id": 128, "name": "Чирокчи пахта тозалаш АЖ"}, {"id": 124, "name": "Касби пахта тозалаш АЖ"}, {"id": 129, "name": "Бешкент пахта тозалаш АЖ"}, {"id": 120, "name": "Нишон пахта тозалаш АЖ"}, {"id": 119, "name": "Жейнов пахта тозалаш АЖ"}, {"id": 118, "name": "Муборак пахта тозалаш АЖ"}] 
        },
        {
            //{"id": 57, "name": "Косон пахта тозалаш АЖ"}
                "id": 5,
                "factories": [{"id": 108, "name": "Кизил-тепа пахта тозалаш АЖ"}, {"id": 80, "name": "Хатирчи пахта тозалаш АЖ"}, {"id": 211, "name": "Навбахор пахта тозалаш МЧЖ"}] 
        },
        {
                "id": 6,
                "factories": [{"id": 42, "name": "Тўрақўрғон пахта тозалаш АЖ"}, {"id": 44, "name": "Норин пахта толаси АЖ"}, {"id": 45, "name": "Учқўрғон пахта тозалаш АЖ"}, {"id": 46, "name": "Чуст пахта толаси АЖ"}, {"id": 48, "name": "Мингбулоқ пахта тозалаш АЖ"}, {"id": 28, "name": "Поп пахта толаси АЖ"}, {"id": 50, "name": "Косонсой пахта толаси АЖ"}, {"id": 41, "name": "Уйчи пахта тозалаш АЖ"}] 
        },
        {
                "id": 7,
                "factories": [{"id": 84, "name": "Каттакургон пахта тозалаш АЖ"}, {"id": 86, "name": "Зирабулок пахта тозалаш АЖ"}, {"id": 88, "name": "Жума пахта тозалаш АЖ"}, {"id": 90, "name": "Челак пахта тозалаш АЖ"}, {"id": 82, "name": "Зиёвуддин пахта тозалаш АЖ"}, {"id": 91, "name": "Янгикургон пахта тозалаш АЖ"}, {"id": 92, "name": "Митан пахта тозалаш АЖ"}] 
        },
        {
                "id": 8,
                "factories": [{"id": 133, "name": "Шеробод пахта тозалаш АЖ"}, {"id": 134, "name": "Хайрабод пахта тозалаш АЖ"}, {"id": 135, "name": "Узун пахта тозалаш АЖ"}, {"id": 136, "name": "Шурчи пахта тозалаш АЖ"}, {"id": 140, "name": "Жаркургон пахта тозалаш АЖ"}, {"id": 139, "name": "Музрабод пахта тозалаш АЖ"}, {"id": 130, "name": "Кизирик пахта тозалаш АЖ"},{"id": 605, "name": "Кумкургон пахта тозалаш АЖ"},{"id": 138, "name": "Ангор пахта пахта тозалаш АЖ"},{"id": 142, "name": "Сариосиё пахта тозалаш АЖ"}] 
        },
        {
                "id": 9,
                "factories": [{"id": 4, "name": "Гулистон пахта тозалаш АЖ"}, {"id": 7, "name": "Боёвут пахта тозалаш АЖ"}, {"id": 252, "name": "Бахт пахта тозалаш АЖ"}, {"id": 17, "name": "Пахтаобод пахта тозалаш АЖ"}, {"id": 15, "name": "Сайхунобод пахта тозалаш АЖ"}, {"id": 14, "name": "Сардоба пахта тозалаш АЖ"}] 
        },
        {
                "id": 10,
                "factories": [{"id": 2, "name": "Алимкент пахта тозалаш АЖ"}, {"id": 5, "name": "Чиноз пахта тозалаш АЖ"}, {"id": 11, "name": "Пискент пахта тозалаш АЖ"}, {"id": 12, "name": "Бўка пахта тозалаш АЖ"}, {"id": 13, "name": "Мустакиллик пахта тозалаш АЖ"}, {"id": 1, "name": "Ўзбекистон пахта тозалаш АЖ"}, {"id": 10, "name": "Корасув пахта тозалаш АЖ"},{"id": 8, "name": "Далварзин пахта тозалаш АЖ"}] 
        },
        {
                "id": 11,
                "factories": [{"id": 23, "name": "Кува пахта тозалаш АЖ"}, {"id": 24, "name": "Тошлок пахта тозалаш АЖ"}, {"id": 26, "name": "Кукон пахта тозалаш АЖ"}, {"id": 27, "name": "Ўзбекистон пахта тозалаш АЖ"}, {"id": 30, "name": "Бешариқ  пахта тозалаш АЖ"}, {"id": 31, "name": "Багдод пахта тозалаш АЖ"}, {"id": 393, "name": "Риштон пахта тозалаш АЖ"}] 
        },
        {
                "id": 12,
                "factories": [{"id": 152, "name": "Гурлан пахта тозалаш АЖ"}, {"id": 154, "name": "Хонка пахта тозалаш АЖ"}, {"id": 156, "name": "Хозарасп пахта тозалаш АЖ"}, {"id": 153, "name": "Шовот пахта тозалаш АЖ"}, {"id": 157, "name": "Янгиариқ пахта тозалаш АЖ"}, {"id": 158, "name": "Янгибозор пахта тозалаш АЖ"}, {"id": 159, "name": "Богот пахта тозалаш АЖ"}, {"id": 160, "name": "Қўшкўпир пахта тозалаш АЖ"}] 
        },

]
function loadFactorie(index){
    $('.plant').empty();
    for (var i=0; i<factories_list[index]["factories"].length; i++){
       var cur_elem =factories_list[index]["factories"], elem = "<option data-id="+cur_elem[i]["id"]+">"+cur_elem[i]["name"]+"</option>";
       $('.plant').append(elem);
    }
}
loadFactorie(0);
for (var i=0; i<region.length; i++){
    var elem = "<option data-id="+i+">"+region[i]+"</option>";
    $('.region').append(elem);
}
$('.region').on("change", function(){
    var id = $('.region option:selected').attr('data-id'); 
    loadFactorie(id);
    
});
$('.calculator').on("submit", function(ev){
    var plant = $('.plant option:selected').attr("data-id"), prod = $('.prod option:selected').attr("data-id"), 
    gen = $('.gen option:selected').attr("data-id"), sort = $('.sort option:selected').attr("data-id"), 
    sinf = $('.sinf option:selected').attr("data-id"), harvest = $('.harvest').val(), r1 = $('.r1').val(), r2 = $('.r2').val(), wt = $('.wt option:selected').attr("data-id"),
    data = {"act": "calc", "name": base_url, "plant": plant, "prod": prod, "gen": gen, "sort": sort, "sinf": sinf, "harvest": harvest, "r1": r1, "r2": r2, "wt": wt};
    $('#fountainG').css('display', 'block');

    $.ajax({
        url: calc_serivce,
        type: "GET",       
        dataType: "json",       
        data: data,       
        success: function(response) {          
            $('.zharvest').html(response.zharvest);
            $('.dsum').html(response.dsum);
            $('.drsum').html(response.drsum);
            $('.msum').html(response.msum);
            $('.usum').html(response.usum);
            $('.tsum').html(response.tsum);
            $('.zsum90').html(response.zsum90);
            $('.zsum100').html(response.zsum100);
            $('.result').fadeIn(200);
        $('#calculator').modal('hide');
        $('#success-result').modal('show');
        $('#fountainG').css('display', 'none');
            return true;
        }
        //error: function(){alert(data);}

    });
    ev.preventDefault();
});