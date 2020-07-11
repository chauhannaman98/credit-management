from django.shortcuts import render, HttpResponse
from creditManager.models import User

# Create your views here.
def home(request):
    return render(request, 'index.html')

def transfer_credit(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'transfer.html', context)