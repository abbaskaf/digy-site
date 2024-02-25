from django.shortcuts import render, redirect, HttpResponse
from .models import Product
from django.views.generic import DetailView, TemplateView, ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignupForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import gettext_lazy as _


def HomeView(request):
    model = Product.objects.all()
    return render(request, 'home.html', {'model': model})


def AboutView(request):
    return render(request, 'about.html')


class DetaView(DetailView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data()
        posty = Product.objects.all()
        contex['posty'] = posty
        return contex


def LoginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید')
            return redirect('home')
        else:
            messages.error(request, 'کاربر وجود ندارد لطفا مجدد تلاش کنید')
            return redirect('Login')

    else:
        return render(request, 'LOgin.html')


def LogoutUser(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید')
    return redirect('home')


@csrf_exempt
def SignUp(request):
    if request.method == 'GET':
        form = SignupForm
        return render(request, 'LOgin.html', {'form': form})
    if request.method == 'POST':
        forms = SignupForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'ثبت نام شما با موفقیت انجام شد')
            return redirect('home')
        else:
            return HttpResponse(F"{forms.errors}")
