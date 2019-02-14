# Now from the main django package and urls module we will import path
from django.urls import path

from . import views

urlpatterns = [

#The code above maps URL paths to Python callback functions (“views”).
# The path strings use parameter tags to “capture” values from the URLs
path('', views.index, name='index'), # Here the second parameter is the method that we want to connect with our desired url is views method ,
    # and the method will call the index , and in third parameter we set a name for our
    # route to easily access the path, Ok now lets create the index function in the views page
path('about', views.about, name='about')
]