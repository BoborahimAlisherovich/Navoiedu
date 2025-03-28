	function setFontSize(fontSize) {
		saveSettings('fontSize', fontSize);
		$('html').removeClass('fs-small fs-normal fs-big').addClass(fontSize);
	}
	
	function setColorSite(color) {
		saveSettings('color', color);
		$('html').removeClass('color1 color2 color3 color4 color5').addClass(color);
	}
	
	function setFontFamily(fontFamily) {
		saveSettings('fontFamily', fontFamily);
		$('html').removeClass('serif sans-serif').addClass(fontFamily);
	}
	
	function setSpacing(letterSpace) {
		saveSettings('letterSpace', letterSpace);
		$('html').removeClass('spacing-normal spacing-big spacing-small').addClass(letterSpace);
	}
	
	function setImageVisible(showImgs) {
		saveSettings('showImgs', showImgs);
		$('html').removeClass('imagesoff imageson').addClass(showImgs);
		$('.a-images a').attr('rel', (showImgs=='imagesoff')?'imageson':'imagesoff');
	}

	function setNormal(normalVer) {
		saveSettings('normalVer', normalVer);
		$('html').removeClass('specialversion normalversion').addClass(normalVer);
	}
	
	function setDefSpecialSettings() {
		setColorSite('color1');
		setFontFamily('sans-serif');
		setFontSize('fs-normal');
		setSpacing('spacing-small');
		setNormal('specialversion');
		setImageVisible('imageson');
	}

	function setNormalMode() {
		setColorSite(def_settings.color);
		setFontFamily(def_settings.fontFamily);
		setFontSize(def_settings.fontSize);
		setSpacing(def_settings.letterSpace);
		setNormal(def_settings.normalVer);
		setImageVisible(def_settings.showImgs);
	}
	
	function setUserSettings() {
		var getSettings = { 
			color:			$.cookie('color') || window.def_settings.color,
			fontFamily:		$.cookie('fontFamily') || window.def_settings.fontFamily,
			fontSize:		$.cookie('fontSize') || window.def_settings.fontSize,
			letterSpace:	$.cookie('letterSpace') || window.def_settings.letterSpace,
			normalVer:		$.cookie('normalVer') || window.def_settings.normalVer,
			showImgs:		$.cookie('showImgs') || window.def_settings.showImgs
		};
		setColorSite(getSettings.color);
		setFontFamily(getSettings.fontFamily);
		setFontSize(getSettings.fontSize);
		setSpacing(getSettings.letterSpace);
		setNormal(getSettings.normalVer);
		setImageVisible(getSettings.showImgs);
	}
	
	function saveSettings(name, value) {
		$.cookie(name, value, { expires: 2*365, path: '/', secure: false });
	}
	
	
$(document).ready(function(){
	window.def_settings = {
			color:			'',
			fontFamily:		'',
			fontSize:		'',
			letterSpace:	'',
			normalVer:		'normalversion',
			showImgs:		'imageson'
		};
	setUserSettings();
	
	$('.choose-font-family a').click(function(){
		setFontFamily($(this).data('set'));
		return false;
	});
	$('.choose-letter-spacing a').click(function(){
		setSpacing($(this).data('set'));
		return false;
	});
	$('.a-images a').click(function(){
		setImageVisible($(this).data('set'));
		return false;
	});

	$('.a-fontsize a').click(function(){
        //location.reload();
		setFontSize($(this).data('set'));
		return false;
	});
	$('.a-colors a, .choose-colors a').click(function(){
        //location.reload();
		setColorSite($(this).data('set'));
		return false;
	});

	$('.a-settings a,.saveit .closepopped').click(function(){
	$('.popped').slideToggle('fast');
		return false;
	});

	$('.saveit .default, #specialversion').click(function(){
		//console.log("oiu");
		setDefSpecialSettings();
        //location.reload();
		return false;
	});

	$('#normalversion').click(function(){
		setNormalMode($(this).data('set'));
        //location.reload();
		return false;
	});
   var options = {
    body: $('body'),
    inputs: $('body input'),
    selects: $('body select'),
    ul: $('body ul'),
    textarea: $('body textarea'),
    blockquote: $('body blockquote'),
    td: $('body td'),
    newsTitle: $('.news_content .news_title a.l1'), 
    mobile: $('.mobile ul li a'),
      time: $('.bugun'),
       menu: $('.nav ul li a'),
         phone: $('.phone .list .phone .list span'),
      
    newsTitleOriginal: $('.news_content .news_title a.l1').css('fontSize'),
    newsContent: $('.news_content p'),
    newsContentOriginal: 16,
    original: 14,
    large: 16,
    largeTitle: 23,
    largeContent: 24,
    small: 14,
    smallTitle: 17,
    smallContent: 16
    }

    // reset font size - make default
    $(".resetFont").click(function () {
    options.body.css('fontSize', options.original);
    options.inputs.css('fontSize', options.original);
    options.menu.css('fontSize', options.original);
    options.phone.css('fontSize', options.original);
    options.time.css('fontSize', options.original);
    options.selects.css('fontSize', options.original);
    options.blockquote.css('fontSize', options.original);
    options.mobile.css('fontSize', options.original);
    options.ul.css('fontSize', options.original);
    options.textarea.css('fontSize', options.original);
    options.td.css('fontSize', options.original);
    options.newsTitle.css('fontSize', options.newsTitleOriginal);
    options.newsContent.css('fontSize', options.newsContentOriginal);
    
    $('.specialversion').removeClass('fs-normal');
     $('.specialversion').removeClass('fs-bigFont');
    return false;
    });

    // increase font size
    $(".bigFont").click(function () {
    options.body.css('fontSize', options.large);
       options.time.css('fontSize', options.large);
       options.menu.css('fontSize', options.large);
        options.phone.css('fontSize', options.large);
    options.inputs.css('fontSize', options.large);
    options.selects.css('fontSize', options.large);
    options.blockquote.css('fontSize', options.large);
    options.ul.css('fontSize', options.large);
    options.textarea.css('fontSize', options.large);
    options.td.css('fontSize', options.large);
    options.mobile.css('fontSize', options.large);
    var currentTitleSize = options.newsTitle.css('fontSize');
    var currentContentSize = options.newsContent.css('fontSize');
    console.log('currentTitleSize = ' + currentTitleSize);
    options.newsTitle.css('fontSize', options.largeTitle);
    options.newsContent.css('fontSize', options.largeContent);
    // $('.specialversion').removeClass('fs-bigFont');
    /*
    if(currentTitleSize < 25){
    options.newsTitle.css('fontSize', currentTitleSize+2+'!important');
    options.newsContent.css('fontSize', currentContentSize+2+'!important');
    }*/
    return false;
    });

    // decrease font size
    $(".smallFont").click(function () {
    options.body.css('fontSize', options.small);
      options.time.css('fontSize', options.small);
             options.menu.css('fontSize', options.small);
               options.phone.css('fontSize', options.small);
    options.inputs.css('fontSize', options.small);
    options.selects.css('fontSize', options.small);
    options.blockquote.css('fontSize', options.small);
    options.mobile.css('fontSize', options.small);
    options.ul.css('fontSize', options.small);
    options.textarea.css('fontSize', options.small);
    options.td.css('fontSize', options.small);
    var currentTitleSize = options.newsTitle.css('fontSize');
    var currentContentSize = options.newsContent.css('fontSize');
    console.log('currentContentSize = ' + currentContentSize);
    options.newsTitle.css('fontSize', options.smallTitle);
    options.newsContent.css('fontSize', options.smallContent);
   $('.specialversion').removeClass('fs-bigFont');
    /*
    if(currentTitleSize > 15){
    options.newsTitle.css('fontSize', currentTitleSize-2);
    options.newsContent.css('fontSize', currentContentSize-2);
    }*/
    return false;
    });
});