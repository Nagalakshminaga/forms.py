from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm




def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def image(request):
    return render(request,'image.html') 
    
    
def contact(request): 
    form=ContactForm()
    if request.method =="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
          form=ContactForm()
    return render(request,'contact.html',{'form_data':form})

    


  