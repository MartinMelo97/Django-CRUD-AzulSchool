from django.urls import path
from .views import GetUsersView, GetUserView, CreateUserView, UpdateUserView, DeleteUserView

app_name = 'main'
urlpatterns = [
    path('', GetUsersView.as_view(), name='list'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('update/<int:id>/', UpdateUserView.as_view(), name='update'),
    path('delete/<int:id>/', DeleteUserView, name='delete'),
    path('<int:id>/', GetUserView, name='detail')
]
