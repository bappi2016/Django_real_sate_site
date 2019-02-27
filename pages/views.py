from django.shortcuts import render
# In home page we will show some of our listing, so we need to fetch our database listing model, so lets import it here
from listings.models import Listing
# for the about page where we will showed our realtor, we need to fetch date from the realtors model,
# that's why we need to import it
from realtors.models import Realtor
from listings.choices import price_choices,bedroom_choices,state_choices

# Create your views here.
# Here we want to render a template for out home page ..

# When a user requests a page, Django runs through each path, in order, and stops at the first one that matches the requested URL. (


def index(request): # Here the index function will inherit the request method as a parameter
    # get [:3] listing
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
    }
    return render(request,'pages/index.html',context)

def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # get the realtor of the month
    realtor_mvp = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors':realtors,
        'realtor_mvp':realtor_mvp
    }
    return render(request, 'pages/about.html',context)