from django.shortcuts import render
def home(request):
    title="home"
    name="MAGIC PEN"
    return render(request,'home.html', locals())
def aboutus(request):
    title="About"
    return render(request,'aboutus.html', locals())
def contactus(request):
    title="contact"
    name="MAGICA"
    phone="9874561230"
    email="magica@gmail.com"
    return render(request,'contactus.html', locals())