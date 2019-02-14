from django.shortcuts import get_object_or_404,render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
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
    return render(request , 'listings/search.html')