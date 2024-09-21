from django.shortcuts import render, redirect
from .forms import ContactMessageForm

def home(request):
    return render(request, "papp/index.html")
def about(request):
    return render(request, "papp/about.html")
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ContactMessageForm()

    return render(request, 'papp/contact.html', {'form': form})
def portfolio(request):
    return render(request, "papp/portfolio.html")
def service(request):
    return render(request, "papp/service.html")
def team(request):
    return render(request, "papp/team.html")
def price(request):
    return render(request, "papp/price.html")



    