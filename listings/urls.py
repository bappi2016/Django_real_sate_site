# Now from the main django package and urls module we will import path
from django.urls import path

from . import views

# we can also import all our views function below ways
#from listings.views import index,listing,search


# for listing we gonna have to have some urls that we need to connect,
# so that's  we need the urls.py file here and change accordingly

urlpatterns = [

#The code above maps URL paths to Python callback functions (“views”).
# The path strings use parameter tags to “capture” values from the URLs
# '' means /listings so we don't need any / here , it implicitly include in '' or by default
path('', views.index, name='listings'),# view will call the index function for the whole listing view
    # Here the second parameter is the method that we want to connect with our desired url is views method ,
    # and the method will call the index , and in third parameter we set a name for our
    # route to easily access the path, Ok now lets create the index function in the views page
path('<int:listing_id>', views.listing, name='listing'), # For viewing the single listing or listing/id
path('search', views.search, name='search'), # here name belongs to html page name the file we wanna render
]