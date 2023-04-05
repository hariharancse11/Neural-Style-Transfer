from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from .bank_predict import bankChurnPrediction

# Create your views here.
def index(request):
    return render(request,'final.html')

def predict(request):
    CreditScore= int(request.POST['CreditScore'])
    Geography= request.POST['Geography']
    Gender= request.POST['Gender']

    Age= int(request.POST['Age'])
    Tenure= int(request.POST['Tenure'])
    Balance= float(request.POST['Balance'])

    NumOfProducts= int(request.POST['NumOfProducts'])
    HasCrCard= int(request.POST['HasCrCard'])
    IsActiveMember= int(request.POST['IsActiveMember']	)
    EstimatedSalary= float(request.POST['EstimatedSalary'])
    print(NumOfProducts)

    res = bankChurnPrediction(CreditScore,	Geography,	Gender,	Age,	Tenure,	Balance,	NumOfProducts,	HasCrCard,	IsActiveMember,	EstimatedSalary)
    messages.info(request,res)
    return redirect('/')