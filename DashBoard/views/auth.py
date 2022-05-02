from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from ..forms import SignUpForm, StudentForm, AlumniForm


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
    def get(self, request):
        try:
            if request.GET['user'] == 'student':
                form = SignUpForm()
                profileform = StudentForm()
                return render(request, 'Home/registerstudent.html', {'form': form, 'profileform': profileform})
            elif request.GET['user'] == 'alumni':
                form = SignUpForm()
                profileform = AlumniForm()
                return render(request, 'Home/registeralumni.html', {'form': form, 'profileform': profileform})
        except KeyError:
            return render(request, 'Home/register.html')

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            data = request.POST.copy()
            data['user'] = user.id
            if 'student' in request.build_absolute_uri():
                profileform = StudentForm(data)
                template = 'Home/registerstudent.html'
            elif 'alumni' in request.build_absolute_uri():
                profileform = AlumniForm(data)
                template = 'Home/registeralumni.html'
            print(profileform.is_valid(), user.id)
            if profileform.is_valid():
                profileform.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect('/')
            else:
                user.delete()
                for msg in form.error_messages:
                    messages.warning(request, f"{msg}: {form.error_messages[msg]}")
        else:
            for msg in form.error_messages:
                messages.warning(request, f"{msg}: {form.error_messages[msg]}")
        return render(request, template, {'form': form, 'profileform': profileform})
    

class PasswordChangeView(View):
    template_name = 'auth/password_change.html'

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        return render(request, self.template_name)