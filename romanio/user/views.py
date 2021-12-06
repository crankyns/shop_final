from .models import CustomUser
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import View
from  django.views.generic.edit import UpdateView
from .forms import LoginForm, PassResForm, UserRegForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView


def logout_view(request):
    logout(request)
    return redirect('home')

class UserSignIn(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'user/signin.html', {'form':UserRegForm()})
        else:
            return redirect('home')


    def post(self, request, *args, **kwargs):   
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        return render(request, 'user/signin.html', {'form':form})



class UserLogin(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'user/login.html', {'form':LoginForm()})
        else:
            return redirect('home')

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Ошибка входа. Проверьте вводимые данные.')
                return redirect('login')
        return render(request, 'user/login.html', {'form':form})
            

class PassResView(PasswordResetView):
    form_class = PassResForm



class UpdateProfile(UpdateView):
    model = CustomUser
    fields = ['username', 'first_name', 'last_name', 'phone_number', 'email',] # Keep listing whatever fields 
    # the combined UserProfile and User exposes.
    template_name = 'profile/profile_update.html'
    template_name_suffix = ''
    

    def get_success_url(self):
  
        return reverse_lazy('profile')

