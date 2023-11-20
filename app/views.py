from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':1000,'b':100,'c':2000}
    return render(request,'condition.html',d)