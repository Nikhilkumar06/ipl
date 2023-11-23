from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return render(request,'msd.html')
def jaddu(request):
    return HttpResponse('<h1><center>BEST ALLROUNDER</h1></center>')