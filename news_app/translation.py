from modeltranslation.translator import register, TranslationOptions
from .models import Rahbariyat,BoShIshOrin,ErishilganYutuqlar,MatbuotXizmati,ElonVaTadbirlar,BoshqarmaTarixi

@register(Rahbariyat)
class RahbariyatTranslationOptions(TranslationOptions):
    fields = ('ism','lavozim')

@register(BoShIshOrin)
class BoShIshOrinTranslationOptions(TranslationOptions):
    fields = ('joylashuv','lavozim')



@register(ErishilganYutuqlar)
class ErishilganYutuqlarTranslationOptions(TranslationOptions):
    fields = ('title','content')


@register(MatbuotXizmati)
class MatbuotXizmatiTranslationOptions(TranslationOptions):
    fields = ('title','content')
    

@register(ElonVaTadbirlar)
class ElonVaTadbirlarTranslationOptions(TranslationOptions):
    fields = ('title','content')
    


@register(BoshqarmaTarixi)
class BoshqarmaTarixiTranslationOptions(TranslationOptions):
    fields = ('title','content')
    
