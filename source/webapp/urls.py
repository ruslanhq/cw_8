from django.urls import path

from webapp.views import IndexView, ProductView, ProductCreate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
    path('product/create/', ProductCreate.as_view(), name='prod_create')
]

app_name = 'webapp'
