import os
import random
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import JsonResponse
import base64
from mysite import settings  # Replace 'myapp' with your actual Django app name
from django.urls import reverse
from mysite import settings
from mysite.settings import BASE_DIR
from .models import SignupModel, ValueModel,  Profile, Post
from .forms import LoginForm, SignupForm, NoValueForm, ValueForm
from django.contrib.auth import authenticate, login, logout
from .custom_auth_backend import Backend


def Page0View(request):
    return render(request, 'index.html')

def Page1View(request, signup_id):
    # Retrieve the SignupModel instance using the provided signup_id
    signup_instance = SignupModel.objects.get(id=signup_id)
    
    # You can add additional logic or processing here if needed
    
    context = {
        'signup_instance': signup_instance,  # Pass the SignupModel instance to the template context
    }
    
    return render(request, 'value.html', context)
  


def Page2View(request, signup_id):
    # Retrieve the SignupModel instance using the provided signup_id
    signup_instance = SignupModel.objects.get(id=signup_id)
    
    # You can add additional logic or processing here if needed
    
    context = {
        'signup_instance': signup_instance,  # Pass the SignupModel instance to the template context
    }
    
    return render(request, 'novalue.html', context)
def Page3View(request):
    return render(request, 'base.html')

def Page4View(request):
    return render(request, 'page.html')

def Page5View(request):
    return render(request, 'signup.html')

def Page6View(request):
    return render(request, 'save.html')


def page1_view(request, signup_id):
    signup_instance = SignupModel.objects.get(id=signup_id)
    context = {
        'signup_instance': signup_instance,
    }
    return render(request, 'page1.html', context)

def page2_view(request, signup_id):
    signup_instance = SignupModel.objects.get(id=signup_id)
    context = {
        'signup_instance': signup_instance,
    }
    return render(request, 'page2.html', context)

def page3_view(request, signup_id):
    signup_instance = SignupModel.objects.get(id=signup_id)
    context = {
        'signup_instance': signup_instance,
    }
    return render(request, 'page3.html', context)

def page4_view(request, signup_id):
    signup_instance = SignupModel.objects.get(id=signup_id)
    context = {
        'signup_instance': signup_instance,
    }
    return render(request, 'page4.html', context)




from django.contrib.auth.models import User
import random
import string

def save_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['form_username']
            password = form.cleaned_data['form_password']
            confirm_password = form.cleaned_data['form_confirm_password']

            # Perform username validation
            if len(username) != 24 or not username.isalnum():
                form.add_error('form_username', "Username must be 24 alphanumeric characters.")

            # Perform password validation
            if password != confirm_password:
                form.add_error('form_confirm_password', "Passwords do not match.")

            if not form.errors:  # Check if there are no validation errors
                # Check if the username already exists
                while User.objects.filter(username=username).exists():
                    # Append a random string to make the username unique
                    username += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

                user = User.objects.create_user(username=username, password=password)  # Create a new user
                signup_instance = form.save(commit=False)
                signup_instance.user = user  # Associate the signup instance with the created user
                signup_instance.save()
                random_number = random.randint(0, 1)
                if random_number == 0:
                    redirect_url = 'value'
                else:
                    redirect_url = 'novalue'
                return redirect(redirect_url, signup_id=signup_instance.id)
            else:
                print("Form has errors:", form.errors)
        else:
            print("Form is invalid:", form.errors)
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)






from django.http import JsonResponse
from django.shortcuts import redirect

def save_novalue(request, signup_id):
    context = {}
    signup_instance = SignupModel.objects.get(id=signup_id)
    if request.method == 'POST':
        # Process the form submission if it's a POST request
        form = NoValueForm(request.POST)
         

        if form.is_valid():
            # Extract cleaned data from the form
            interests = form.cleaned_data.get('interests')
            format_importance = form.cleaned_data.get('format_importance')
            catchphrase = form.cleaned_data.get('catchphrase')
            form_value = form.cleaned_data.get('form_value')
            
            # Print form values for debugging
            print("Interests:", interests)
            print("Value Importance:", format_importance)
            print("Catchphrase:", catchphrase)
            print("Form Value:", form_value)
            
            interests_errors = []
            format_importance_errors = []
            catchphrase_errors = []
            form_value_error = []

            if not form_value:
                form_value_error.append("Please select a value from the list")
                form.add_error('form_value', form_value_error)

            if interests and len(set(interests)) <= 1:
                interests_errors.append("Please provide a more meaningful response")

            if format_importance and len(set(format_importance)) <= 1:
               format_importance_errors.append("Please provide a more meaningful response")

            if catchphrase and len(set(catchphrase)) <= 1:
                catchphrase_errors.append("Please provide a more meaningful response")

            if len(interests) < 10:
                interests_errors.append("This field must be at least 10 characters long")

            if len(format_importance) < 10:
                format_importance_errors.append("This field must be at least 10 characters long")

            if len(catchphrase) < 10:
                catchphrase_errors.append("This field must be at least 10 characters long")

            if interests_errors or format_importance_errors or catchphrase_errors or form_value_error:
                # If there are errors in the form, return a JSON response with errors
                return JsonResponse({'errors': form.errors}, status=400)

            # Form is valid, so save it along with the associated SignupModel
            form_instance = form.save(commit=False)
            form_instance.signup_id = signup_id
            form_instance.save()
            
        else:
            # Handle the case where the form is invalid and return a JSON response with errors
            print("Form is invalid:", form.errors)
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        # If it's not a POST request, create an empty form and retrieve the SignupModel instance
        form = NoValueForm()
        signup_instance = SignupModel.objects.get(id=signup_id)
    
    # Prepare the context for rendering the template
    context = {
        'form': form,
        'signup_instance': signup_instance,
    }
    
    # Render the 'novalue.html' template with the context
    return render(request, 'novalue.html', context)




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ValueModel, Profile  # Import the ValueModel and Profile models
from django.contrib.auth.models import User


def save_value(request, signup_id):
    context = {}
    signup_instance = SignupModel.objects.get(id=signup_id)
    if request.method == 'POST':
        form = ValueForm(request.POST)
        
        if form.is_valid():
            interests = form.cleaned_data.get('interests')
            value_importance = form.cleaned_data.get('value_importance')
            catchphrase = form.cleaned_data.get('catchphrase')
            form_value = form.cleaned_data.get('form_value')
            
            # Perform the additional form validation checks as you've done

            

            # Form is valid, so save it along with the associated SignupModel
            form_instance = form.save(commit=False)
            form_instance.signup_id = signup_id
            form_instance.save()

            # Create or update the user's profile with relevant information
            user = User.objects.get(id=signup_instance.user_id)  # Get the associated user
            profile, created = Profile.objects.get_or_create(user=user)
            profile.interests = interests
            profile.value = value_importance
            profile.catchphrase = catchphrase
            profile.save()

            # Redirect to a success page or another appropriate action
            return render(request, 'failure.html', context)

        else:
            print("Form is invalid:", form.errors)
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ValueForm()
    
    context = {
        'form': form,
        'signup_instance': signup_instance,
    }
    return render(request, 'value.html', context)


from django.shortcuts import render
from .models import ValueModel  # Import your ValueModel here

@login_required
def generate_wordle_view(request, signup_id):
    try:
        value_model = ValueModel.objects.get(signup_id=signup_id)
        form_value = value_model.form_value
        print(f"BASE_DIR: {BASE_DIR}")
        # Construct the relative image path using MEDIA_ROOT
        
        wordle_image_path = os.path.join(settings.BASE_DIR, 'mysite', 'static', 'images', f'{form_value}.png')

        print("wordle_image_path:", wordle_image_path)  # Add this line for debugging

        # Check if the image files exist
        if os.path.exists(wordle_image_path):
            print("Wordle image exists:", wordle_image_path)
            with open(wordle_image_path, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
                print("image_data:", image_data)
        else:
            image_data = None

        

        context = {
            'form_value': form_value,
            'image_data': image_data,
        #    'keyboard_colors': keyboard_colors.get(keyboard_id, []),
        }
        return render(request, 'page5.html', context)  # Replace 'page5.html' with your actual template name
    except ValueModel.DoesNotExist:
        return render(request, 'error.html', {'message': 'No ValueModel found for the provided signup ID.'})


from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile 
@login_required
def base_action(request, signup_id):
    if request.method == "POST":
        form = forms.Form(request.POST)
        text = request.POST.get('text', '')
        if not text:
            messages.error(request, 'You cannot post nothing.')
        else:
            new_post = Post(text=text, user=request.user)
            new_post.save()
    else:
        form = forms.Form()

    user = request.user
    # Get or create the UserProfile for the logged-in user
    profile, created = Profile.objects.get_or_create(user=user)
    posts = Post.objects.filter(user=user)

    context = {'posts': posts, 'profile': profile, 'form': form}
    return render(request, 'page.html', context)

@login_required
def display_action(request, signup_id):
    if request.method == "POST":
        form = forms.Form(request.POST)
        text = request.POST.get('text', '')
        if not text:
            messages.error(request, 'You cannot post nothing.')
        else:
            new_post = Post(text=text, user=request.user)
            new_post.save()
    else:
        form = forms.Form()

    user = request.user
    # Get or create the UserProfile for the logged-in user
    profile, created = Profile.objects.get_or_create(user=user)
    posts = Post.objects.filter(user=user)
    context = {'posts': posts, 'profile': profile, 'form': form}
    return render(request, 'valuedisplay.html', context)

@login_required
def selection_action(request, signup_id):
    if request.method == "POST":
        form = forms.Form(request.POST)
        text = request.POST.get('text', '')
        if not text:
            messages.error(request, 'You cannot post nothing.')
        else:
            new_post = Post(text=text, user=request.user)
            new_post.save()
    else:
        form = forms.Form()

    user = request.user
    # Get or create the UserProfile for the logged-in user
    profile, created = Profile.objects.get_or_create(user=user)
    posts = Post.objects.filter(user=user)
    context = {'posts': posts, 'profile': profile, 'form': form}
    return render(request, 'usernameselection.html', context)


from django.views.decorators.http import require_POST

""" @require_POST
def save_wordle_entry(request):
    if request.method == 'POST':
        form = WordleEntryForm(request.POST)
        if form.is_valid():
            signup_id = form.cleaned_data['signup_id']  # Retrieve signup_id from the form
            signup_instance = SignupModel.objects.get(pk=signup_id)  # Retrieve the SignupModel instance
            
            wordle_entry = form.save(commit=False)
            wordle_entry.signup = signup_instance  # Associate the SignupModel instance
            wordle_entry.save()
            
            return JsonResponse({'message': 'Wordle entry saved successfully.'})
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405) """




def logout_action(request):
    logout(request)
    return redirect(reverse('login'))



from .models import SignupModel
from django.shortcuts import get_object_or_404

def login_action(request):
    context = {}

    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, 'registration/login.html', context)

    form = LoginForm(request.POST)
    context['form'] = form

    if not form.is_valid():
        return render(request, 'registration/login.html', context)

    username = form.cleaned_data['username']

    # Authenticate the user based on the username (without checking the password)
    user = authenticate(request, username=username)

    if user is not None:
        # Log in the user
        login(request, user)

        # Retrieve the associated SignupModel for the user
        signup_model = get_object_or_404(SignupModel, user=user)

        # Perform any necessary actions with the signup_model
        # For example, you can access signup_model.signup_id to get the ID.

        return redirect('generate_wordle', signup_id=signup_model.id)
    else:
        # Handle the case where the user is not found or authentication fails
        return render(request, 'registration/login.html', context)