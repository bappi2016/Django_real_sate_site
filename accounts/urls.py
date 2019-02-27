from django.urls import path

from . import views

urlpatterns = [
    # could be access the whole urls by "path('accounts/',include('accounts.urls')),"
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard')
]