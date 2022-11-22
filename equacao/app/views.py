from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    if request.method == 'GET':
        form = UserForm()
        context = {
            'form' : form
        }
        return render(request, 'user/index.html', context=context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():

            a =  form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            
            delta = (b ** 2) + (- 4 * a * c)
      
            raiz1 = (-b + delta**0.5) / (2 * a)

            raiz2 = (-b - delta**0.5) / (2 * a)

            context = {
                'form' : form,
                'raiz1': raiz1,
                'raiz2': raiz2,
                
            }
        return render(request, 'user/index.html', context=context)
