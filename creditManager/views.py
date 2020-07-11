from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def transfer_credit(request):
    return render(request, 'transfer.html')