from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Define a function view called login_view that takes a request from user
def login_view(request):
    error_message = None
    form = AuthenticationForm()

    # When user hits "login" button, POST request is generated
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        # Check if form is valid
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Validate the user using Django authenticate
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes:recipes_list')
        else:
            error_message = 'Invalid username or password.'

    context = {
        'form': form,
        'error_message': error_message
    }

    # Load login page text using 'context' information
    return render(request, 'auth/login.html', context)

# Define function-based logout_view that takes a request from user
def logout_view(request):
    logout(request)
    return redirect('login')