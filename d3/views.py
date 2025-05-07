from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views h
class ShowMain(TemplateView):
    template_name = 'd3/index.html'

class ShowCooperation(TemplateView):
    template_name = 'd3/cooperation.html'

class ShowContacts(TemplateView):
    template_name = 'd3/contacts.html'

class ShowBase(TemplateView):
    template_name = 'base.html'


def handler_404(request, exception):
    return render(request, template_name='/404.html')

def handler_500(request):
    return render(request, template_name='500.html')


