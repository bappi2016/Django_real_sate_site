from django.shortcuts import get_object_or_404,render
from .models import Listing
from .choices import price_choices,bedroom_choices,state_choices
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    # Here the listings variable store all the databases of Listing model and viewed with there list date and filter with published or not
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    #Now create a paginator for the listing page
    paginator = Paginator(listings,3) # Show 3 listings per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # Now create a dictionary named context which we will pass to fetch the data in the front end
    context = {
        'listings': paged_listings

    }
    return render(request , 'listings/listings.html',context)

def listing(request,listing_id):
    listing =  get_object_or_404(Listing,pk=listing_id)

    context = {
        'listing':listing,
    }
    return render(request , 'listings/listing.html',context) # request the browser to go to listings packages and render the html file

def search(request):
    # Now for search option at first we have to fetch all the models of listing and then filter with the users requerments
    # Now set a query set list with the listing model and add filter for the search
    query_set_list = Listing.objects.order_by('-list_date')
    # Now if we pass the 'query_set_list' variable into the context dict , then we can able to get the template of all the listings
    #  And for searching we need all out listing

    # Now for searching with any keyword ,at first we have to check if the keyword exist or not
    # Now if there is any request.GET which is happened everytime with any users request , we will see the keyword in it
    # For keyword search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set_list = query_set_list.filter(description__icontains=keywords)

    # For City field search
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set_list = query_set_list.filter(city__iexact=city)

    # For State field search
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set_list = query_set_list.filter(state__iexact=state)

    # For Bedrooms field search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_set_list = query_set_list.filter(bedrooms__lte=bedrooms)

    # For Price field search
    if 'price' in request.GET: # will looking in the form with the field name price
        price = request.GET['price']
        if price:
            query_set_list = query_set_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings':query_set_list,
        'values':request.GET # by this line the
        # request.keywords should be available to us as values.keyword
        # so when ever we search it will stay in the template just like other option like price_choices

    }
    # To render all the listing in the search.html template we have to set up the page according to the
    # Listing model to fetch all the data
    return render(request , 'listings/search.html',context)