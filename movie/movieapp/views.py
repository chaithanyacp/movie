from django.shortcuts import render, redirect
from . models import movietable
from .forms import movieform

# Create your views here.
def home(request):
    tableitems = movietable.objects.all()
    context = {'key1':tableitems}
    return render(request,"home.html",context)
def detail(request,movie_id):
    x = movietable.objects.filter(id=movie_id)
    return render(request,"detail.html",{'key1': x})
def add_movie(request):
    if request.method =='POST':
        name=request.POST.get('name')
        detail = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        m=movietable(name=name,desc=detail,year=year,img=img)
        m.save()
    return render(request,"add.html")
def update(request,id):
    movie=movietable.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=movietable.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
