from django.urls import path
from .views import GetUsersView, GetUserView, CreateUserView, UpdateUserView, DeleteUserView

urlpatterns = [
    path('', GetUsersView.as_view()),
    path('create/', CreateUserView.as_view()),
    path('update/<int:id>/', UpdateUserView.as_view()),
    path('delete/<int:id>/', DeleteUserView),
    path('<int:id>/', GetUserView)
]
