from django.urls import path
from .views import GetShippingAddressView, CreateShippingAddressView, UpdateShippingAddressView, DeleteShippingAddressView

app_name = 'shipping_addresses'
urlpatterns = [
    path('<int:id>/', GetShippingAddressView, name='detail'),
    path('create/<int:user_id>/', CreateShippingAddressView.as_view(), name='create'),
    path('update/<int:id>/', UpdateShippingAddressView.as_view(), name='update'),
    path('delete/<int:id>/', DeleteShippingAddressView, name='delete')
]