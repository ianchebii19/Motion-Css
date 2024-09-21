from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "papp/index.html")
def about(request):
    return render(request, "papp/about.html")
def contact(request):
    return render(request, "papp/contact.html")
def portfolio(request):
    return render(request, "papp/portfolio.html")
def service(request):
    return render(request, "papp/service.html")
def team(request):
    return render(request, "papp/team.html")
def price(request):
    return render(request, "papp/price.html")
   