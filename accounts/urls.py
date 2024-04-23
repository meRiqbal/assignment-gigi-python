from django.urls import path
from .views import login_view, signup_view, home_view, dashboard_view
urlpatterns = [
    path('signup/', signup_view ,name = 'signup'),
    path('login/', login_view, name = 'login'),
    path('home/',home_view, name= 'home'),
    path('dashboard/', dashboard_view, name = 'dashboard'),
]
