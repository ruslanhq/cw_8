from django.urls import path

from webapp.views import IndexView, ProductView, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
    path('product/create/', ProductCreate.as_view(), name='prod_create'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='prod_update'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='prod_delete')
]

app_name = 'webapp'
