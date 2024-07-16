from django.shortcuts import render
from ecomapp.models import Contact,Product
from django.contrib import messages
from math import ceil

def index(request):
    allProds= []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1, nSlides),nSlides])

    params={'allProds':allProds}    
    return render(request, "index.html",params)  

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        description=request.POST.get("description")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name,email=email,description=description,phone_number=pnumber)
        myquery.save()
        messages.info(request,"we will get back you soon")
        return render(request, "contact.html")


    return render(request, "contact.html")
def about(request):
    return render(request, "about.html")
def about(request):
    return render(request, "base.html")
