from django.urls import path
from .views import register_flutter, login_flutter, logout_flutter

app_name = 'authentication'

urlpatterns = [
    path('register/', register_flutter, name='register_flutter'),
    path('login/', login_flutter, name='login_flutter'),
    path('logout/', logout_flutter, name='logout_flutter'),
]