from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ShowServises(TemplateView):
    template_name = 'services/services.html'


class ShowServicePrint3d(TemplateView):
    template_name = 'services/list/service_print3d.html'

class ShowServiceVisualise3d(TemplateView):
    template_name = 'services/list/service_visualise3d.html'

class ShowServiceModelling3d(TemplateView):
    template_name = 'services/list/service_modelling3d.html'

class ShowServicePainting(TemplateView):
    template_name = 'services/list/service_painting.html'

class ShowServicePostProcessing(TemplateView):
    template_name = 'services/list/service_postprocessing.html'