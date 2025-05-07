from django.urls import path

from services.views import ShowServises, ShowServicePrint3d, ShowServiceVisualise3d, ShowServiceModelling3d, \
    ShowServicePainting, ShowServicePostProcessing

app_name = 'services'

urlpatterns = [
    path('', ShowServises.as_view(), name='services'),
    path('print3d/', ShowServicePrint3d.as_view(), name='print3d'),
    path('visualise3d/', ShowServiceVisualise3d.as_view(), name='visualise3d'),
    path('modelling3d/', ShowServiceModelling3d.as_view(), name='modelling3d'),
    path('painting/', ShowServicePainting.as_view(), name='painting'),
    path('postprocessing/', ShowServicePostProcessing.as_view(), name='postprocessing'),
]