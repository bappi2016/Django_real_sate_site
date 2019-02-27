from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    # for any form request at first we have to check if the request method has a post method
    if request.method == 'POST':
        # store the listing id
        listing_id = request.POST['listing_id'] # for every post there is a listing id for the corresponding listing
        # store the listing which is user wants to inquiry
        listing = request.POST['listing'] # for  the reference listing
        name = request.POST['name'] # store the name of the person who wants to contact
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email'] # for the contact we need the realtor email
        
    # Check user already send an inquiry 
    if request.user.is_authenticated: # if user is logged in
        user_id = request.user.id # assign users id with his id
        # Now check if an user is in the contact table with a particular listing id or not
        has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id) 
        if has_contacted:
            messages.error(request,'You have already made an inquiry for this listing')
            return redirect('/listings/' + listing_id)
    
       # Now create an object contact of the Contact model class with those above attribute
        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,
                          phone=phone,message=message,user_id=user_id)
        contact.save()
        
    # Send email
    send_mail(
        'Property Listing Inquiry', # subject
        'There has been an inquiry for ' + listing + '. Sign into the'
        ' admin panel for more info ', # message
        'bappi.ajmalaamir@gmail.com', # from
        [realtor_email,'bappi013@gmail.com'], # to
        fail_silently=False,

    )

    messages.success(request,'Your request has been submitted, a realtor'
                             ' will get back to you soon')
    return redirect('/listings/'+listing_id)


