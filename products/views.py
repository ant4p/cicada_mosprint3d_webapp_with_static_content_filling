from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ShowCatalog(TemplateView):
    template_name = 'products/catalog.html'

class ShowProduct_1(TemplateView):
    template_name = 'products/list/product_1(axolotl).html'

class ShowProduct_2(TemplateView):
    template_name = 'products/list/product_2(yeti).html'

class ShowProduct_3(TemplateView):
    template_name = 'products/list/product_3(big).html'

class ShowProduct_4(TemplateView):
    template_name = 'products/list/product_4(bug_1).html'

class ShowProduct_5(TemplateView):
    template_name = 'products/list/product_5(bug_2).html'

class ShowProduct_6(TemplateView):
    template_name = 'products/list/product_6(chess).html'

class ShowProduct_7(TemplateView):
    template_name = 'products/list/product_7(dog).html'

class ShowProduct_8(TemplateView):
    template_name = 'products/list/product_8(doll).html'

class ShowProduct_9(TemplateView):
    template_name = 'products/list/product_9(dominate).html'

class ShowProduct_10(TemplateView):
    template_name = 'products/list/product_10(goat).html'

class ShowProduct_11(TemplateView):
    template_name = 'products/list/product_11(ikran).html'

class ShowProduct_12(TemplateView):
    template_name = 'products/list/product_12(mask_1).html'

class ShowProduct_13(TemplateView):
    template_name = 'products/list/product_13(mask_2).html'


class ShowProduct_14(TemplateView):
    template_name = 'products/list/product_14(owl).html'


class ShowProduct_15(TemplateView):
    template_name = 'products/list/product_15(pokemon).html'


class ShowProduct_16(TemplateView):
    template_name = 'products/list/product_16(seahorse).html'


class ShowProduct_17(TemplateView):
    template_name = 'products/list/product_17(shark).html'

class ShowProduct_18(TemplateView):
    template_name = 'products/list/product_18(tiger).html'


class ShowProduct_19(TemplateView):
    template_name = 'products/list/product_19(voodoo).html'

class ShowProduct_20(TemplateView):
    template_name = 'products/list/product_20(robot).html'


