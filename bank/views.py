from django.shortcuts import render,redirect
from .models import User,TransactionHistory,ContactUs
from django.utils import timezone
# Create your views here.
def homePage(request):
    return render(request,'index.html')

def aboutUs(request):
    return render(request,'about.html')
def contactUs(request):
    if request.method == "POST":
        contact = ContactUs(email=request.POST['email'],about=request.POST['about'],concern=request.POST['concern'])
        contact.save()
    return render(request,'contact.html')
def makeTransaction(request,id):
    users = User.objects.all().exclude(id=id)
    user = User.objects.get(id=id)
    if request.method == "POST":
        receiver = User.objects.get(id=request.POST['receiver'])
        transaction = TransactionHistory(sender=user,receiver=receiver,amount=int(request.POST['amount']),datetime=timezone.now())
        transaction.save()
        user.bank_balance = user.bank_balance - int(request.POST['amount'])
        user.save()
        receiver.bank_balance = receiver.bank_balance + int(request.POST['amount'])
        receiver.save()
        return redirect("/transactionHistory/")
    return render(request,'Make_transaction.html',{'users':users,'user':user})
def transactionHistory(request):
    users = TransactionHistory.objects.all()
    return render(request,'transaction_history.html',{'users':users})
def createUser(request):
    if request.method == "POST":
        user = User(name=request.POST['name'],email=request.POST['email'],bank_balance=request.POST['amount'])
        user.save()
    return render(request, 'Create_Users.html')

def viewUsers(request):
    users = User.objects.all()
    return render(request,'view_users.html',{"users":users})


