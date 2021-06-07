from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies
from .forms import Movieform
# Create your views here.
def example(request):
    movie=Movies.objects.all()
    context={
        'movielist':movie
    }
    return render(request,'index.html',context)


def detailss(request,movieid):
    movie=Movies.objects.get(id=movieid)
    #return HttpResponse("this movie is id number %s" %movieid)
    return render(request,'detailspage.html',{'movie':movie})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        yr = request.POST.get('yr')
        imge = request.FILES['imge']
        movie=Movies(name=name,desc=desc,yr=yr,imge=imge)
        movie.save()
    return render(request,'add.html')

def updatee(request,id):
    movie=Movies.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def deletee(request,id):
    if request.method == 'POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')

    return render(request,'delete.html')