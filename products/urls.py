from django.urls import path

from products.views import ShowCatalog, ShowProduct_1, ShowProduct_2, ShowProduct_3, ShowProduct_4, ShowProduct_5, \
    ShowProduct_6, ShowProduct_7, ShowProduct_8, ShowProduct_9, ShowProduct_10, ShowProduct_11, ShowProduct_12, \
    ShowProduct_13, ShowProduct_14, ShowProduct_15, ShowProduct_16, ShowProduct_17, ShowProduct_18, ShowProduct_19, \
    ShowProduct_20

app_name = 'catalog'

urlpatterns = [
    path('', ShowCatalog.as_view(), name='catalog'),
    path('product_1/', ShowProduct_1.as_view(), name='product_1'),
    path('product_2/', ShowProduct_2.as_view(), name='product_2'),
    path('product_3/', ShowProduct_3.as_view(), name='product_3'),
    path('product_4/', ShowProduct_4.as_view(), name='product_4'),
    path('product_5/', ShowProduct_5.as_view(), name='product_5'),
    path('product_6/', ShowProduct_6.as_view(), name='product_6'),
    path('product_7/', ShowProduct_7.as_view(), name='product_7'),
    path('product_8/', ShowProduct_8.as_view(), name='product_8'),
    path('product_9/', ShowProduct_9.as_view(), name='product_9'),
    path('product_10/', ShowProduct_10.as_view(), name='product_10'),
    path('product_11/', ShowProduct_11.as_view(), name='product_11'),
    path('product_12/', ShowProduct_12.as_view(), name='product_12'),
    path('product_13/', ShowProduct_13.as_view(), name='product_13'),
    path('product_14/', ShowProduct_14.as_view(), name='product_14'),
    path('product_15/', ShowProduct_15.as_view(), name='product_15'),
    path('product_16/', ShowProduct_16.as_view(), name='product_16'),
    path('product_17/', ShowProduct_17.as_view(), name='product_17'),
    path('product_18/', ShowProduct_18.as_view(), name='product_18'),
    path('product_19/', ShowProduct_19.as_view(), name='product_19'),
    path('product_20/', ShowProduct_20.as_view(), name='product_20'),
]