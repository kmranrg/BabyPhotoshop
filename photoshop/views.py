from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def privacyPolicy(request):
    return render(request, 'privacy-policy.html')