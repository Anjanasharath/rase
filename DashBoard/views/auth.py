from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from ..forms import SignUpForm


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request=request, template_name="Home/login.html", context={"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect('/dashboard/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.warning(request, "Invalid username or password.")
        return render(request=request, template_name="Home/login.html", context={"form": form})


class LogoutView(View):
    template_name = 'auth/logout.html'

    def get(self, request):
        logout(request)
        return redirect('DashBoard:home')


class RegisterView(View):
    template_name = 'Home/register.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/')
        else:
            for msg in form.error_messages:
                messages.warning(request, f"{msg}: {form.error_messages[msg]}")
            return render(request, 'Home/signup.html', {'form': form})
    

class PasswordChangeView(View):
    template_name = 'auth/password_change.html'

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        return render(request, self.template_name)