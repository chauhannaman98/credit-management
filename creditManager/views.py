from django.shortcuts import render, HttpResponse
from creditManager.models import User

# Create your views here.
def home(request):
    return render(request, 'index.html')

def transfer_credit(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'transfer.html', context)

def user(request, name):
    if request.method == 'POST':
        recipient = request.POST.get("recipient")
        credit = request.POST.get("credit")
        print('Recipient: '+recipient)
        print('Credit: '+credit)
    users = User.objects.all()
    user = User.objects.filter(name=name).first()
    context = {
        'user':user,
        'users': users
        }
    return render(request, 'user.html', context)

def confirmation(request, name):
    users = User.objects.all()
    context = {
        'name': name,
        'users':users
    }
    return render(request, 'confirmation.html', context)
