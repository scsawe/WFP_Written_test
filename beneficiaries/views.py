from django.shortcuts import render, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')   
# return render(request, 'Home/index.html')

def beneficiary_list_view(request):
     return render(request, 'beneficiaries/beneficiary_list.html')
 
def beneficiary_detail_view(request):
     return render(request, 'beneficiaries/beneficiary_detail.html')

def beneficiary_create_view(request):
     return render(request, 'beneficiaries/beneficiary_create.html')
 
def beneficiary_update_view(request):
     return render(request, 'beneficiaries/beneficiary_update.html')

def beneficiary_delete_view(request):
     return render(request, 'beneficiaries/beneficiary_delete.html')
     
