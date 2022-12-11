from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User


from .forms import LoginForm


class LoginView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return HttpResponse("login not valid")

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


class RegisterView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check that the two passwords match
        if password == password2:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username is already taken'})

            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Authenticate the user and login
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

    def get(self, request):
        return render(request, 'register.html')
