from django.shortcuts import render
from django.views import View
from .models import movies
from .models import movies_theatre
from .models import movies_hollywood
from .models import movies_surprises
from .forms import *
from django.http import HttpResponse

def home(request):
    return render(request, "Main.html",context={"ctx":movies.objects.all().values(),"ctx_theatre":movies_theatre.objects.all().values(),"ctx_hollywood":movies_hollywood.objects.all().values(),"ctx_surprises":movies_surprises.objects.all().values()})

class review_page(View):
    def get(self,request,n=None):
        return render(request, "Review.html",context=movies.objects.all().values()[int(n)])

class review_page_theatre(View):
    def get(self,request,n=None):
        return render(request, "Review.html",context=movies_theatre.objects.all().values()[int(n)])
    
class review_page_hollywood(View):
    def get(self,request,n=None):
        return render(request, "Review.html",context=movies_hollywood.objects.all().values()[int(n)])
    
class review_page_surprises(View):
    def get(self,request,n=None):
        return render(request, "Review.html",context=movies_surprises.objects.all().values()[int(n)])
    
def signup(request):
    if request.method == "POST":
        form=dump_user_info(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"login.html")
    form=dump_user_info
    return render(request,"signup.html",context={"form":form})

class user_review(View):
    def get(self,request,n=None):
        return render(request, "user_review.html", context=movies.objects.all().values()[int(n)])