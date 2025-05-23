from django.shortcuts import render,redirect

# Create your views here.

from item.models import category,Item
from .forms import SignupForm
def index(request):
    items=Item.objects.filter(isSold=False)[0:6]
    categories= category.objects.all()
    return render(request,'core/index.html',{
        'categories':categories,
        'items':items,
        
    })

def contact(request):
    return render(request,'core/contact.html')


def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form=SignupForm()
        
    
    return render(request,'core/signup.html',{
        'form':form
    })
