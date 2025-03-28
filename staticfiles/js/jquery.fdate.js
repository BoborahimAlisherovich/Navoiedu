/* 05.04.17 OSG */

;(function( $ ){
  $.fn.fdate = function( options ) {

    var settings = $.extend( {
      locale : 'ru',
	  timout : 500
    }, options);
	var month = {"ru":["Января","Февраля","Марта","Апреля","Мая","Июня","Июля","Августа","Сентября","Октября","Ноября","Декабря"],"uz":["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"],"en":["January","February","March","April","May","June","August","September","October","November","December"]};
	var day = {"ru":["Воскресенье","Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"],"uz":["Якшанба", "Душанба","Сешанба","Чоршанба","Пайшанба","Жума","Шанба"],"en":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]};
	
    return this.each(function() { 
		var $this = $(this);
        getDate($this);
		setInterval(function(){
            getDate($this);
		}, 1000);
		
    });
	function getDate($this){
		var date = new Date(),
			hour = date.getHours(),
			minute = date.getMinutes(),
			second = date.getSeconds();
			week = date.getDay();
			week_day = date.getDate();
			month_d = date.getMonth();
		$($this).html(checkTime(hour)+':'+checkTime(minute)+':'+checkTime(second)+'&nbsp;/&nbsp;'+week_day+'&nbsp;'+month[settings.locale][month_d]+'&nbsp;/&nbsp;'+day[settings.locale][week]);
	}
	function checkTime(i)
	{
		if (i<10)
		{
		i="0" + i;
		}
		return i;
		}
	};
})( jQuery );