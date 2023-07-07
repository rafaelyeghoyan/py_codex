from django.shortcuts import render

def home(request):
    return render(request, "./header/index.html")
def about(request):
    return render(request, "./header/about.html")