from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .SAPrediction import SAPredict

# Create your views here.
def index(request):
    return render(request,'final.html')

def predict(request):
    sent= request.POST['txt']
    print(sent)

    res = SAPredict(sent)
    messages.info(request,res)
    return redirect('/')