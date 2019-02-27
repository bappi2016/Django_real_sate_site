from django.shortcuts import render,redirect
from django.contrib import messages,auth # for adding message
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.

def login(request):
    # For login we have to input the username and password which is posted by user in our form
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Now to authenticate we have to check if the username and password are exist in
        # in the database and check that they are matched
        # now create a variable user which refer to the username that comes from the form
        # and with help the auth package we will check if those are matched or not

        user =  auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Login Successfully')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:


        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'Logout Successfully ')
        return redirect('index')

def register(request):
    if request.method == 'POST':
        # Get the values
        first_name = request.POST['first_name'] # names are comes in from the form with the post method
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check Username already exist or not in database
            if User.objects.filter(username=username).exists():
                messages.error(request,'This username is taken')
                return redirect('register')
            else: # Check email is exists or not
             if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is being used')
                return redirect('register')
             else:
                # If all the above validation is ok,user can now create
            # and account. Here we use the default Model api auth.models
                # now create a variable user
                user = User.objects.create_user(username=username,password=password,
                        email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request,'You are registered now and can log in')
                return redirect('login')
        else:
            messages.error(request, 'Password didn\'t match')
            return redirect('register')

    # because we are using the context processor for the messages, out template
    # should be render with a RequestContext to available the messages to our template
    #messages.error(request,'test error messages') # shortcut methods to provide a message-usually represented as HTML classes
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    # for dashboard view at first we have to fetch all the contact
    # and we will fetch all the recent contact first with filter
    #order_by('-contact_date') and then filter them with their user_id
    # here the request.user using that request object which will includes the
    #current logged in user to show in the dashboard
    # and we want id which should match with user_id
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id =request.user.id)

    # Now we want to render the dashboard with the following attribute
    # which we gonna pass with context dictionary which have one key and value
    context = {
        'contacts':user_contacts
    }
    return render(request, 'accounts/dashboard.html',context)