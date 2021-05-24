
from django.shortcuts import render, redirect
from .models import Tags, Photo
from django.core.paginator import Paginator
from PIL import Image 
from django.http import HttpResponse
from random import randint
import os
from pathlib import Path
# Create your views here.

def gallery(request):
    tag = request.GET.get('tag')
    if tag == None:
        photos = Photo.objects.get_queryset().order_by('id')
        
    else:
        photos = Photo.objects.filter(tags__name=tag).order_by('id')
    tags = Tags.objects.all()
    paginator = Paginator(photos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'tags':tags,'page_obj': page_obj}
    return render(request, 'photos/gallery.html',context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html',{'photo':photo})

def addPhoto(request):
    tags = Tags.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            tags = Tags.objects.get(id=data['category'])
        elif data['category_new'] != '':
            tags, created = Tags.objects.get_or_create(
                name=data['category_new'])
        else:
            tags = None

        for image in images:
            photo = Photo.objects.create(
                tags=tags,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')
    context = {'tags':tags}
    return render(request, 'photos/add.html',context)

def rotate_right(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        im = Image.open(photo.image)
        angle = 270
        rotated_image = im.rotate(angle)
        """ uploding new transformed image to media folder just to make it visible on UI in no time
            If we save image with same name it takes around 2-3 minutes to reflect the change on UI
            Instead of line 64-70 work can be done by just 2 lines, line 68 and 70"""
        new = randint(1000,10000)
        name = 'photo'+str(new)+'.jpg'
        BASE_DIR = Path(__file__).resolve().parent.parent
        name1 = BASE_DIR /'static/images'/name
        rotated_image.save(name1, overwrite=True)
        Photo.objects.filter(id=pk).update(image=name)
        rotated_image.show()
        return redirect('gallery')
    else:
        return render(request,'photos/add.html')

def rotate_left(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        im = Image.open(photo.image)
        angle = 270
        rotated_image = im.rotate(angle)
        """ uploding new transformed image to media folder just to make it visible on UI in no time
            If we save image with same name it takes around 2-3 minutes to reflect the change on UI
            Instead of line 84-90 work can be done by just 2 lines, line 88 and 90"""
        new = randint(1000,10000)
        name = 'photo'+str(new)+'.jpg'
        BASE_DIR = Path(__file__).resolve().parent.parent
        name1 = BASE_DIR /'static/images'/name
        rotated_image.save(name1, overwrite=True)
        Photo.objects.filter(id=pk).update(image=name)
        rotated_image.show()
        return redirect('gallery')
    else:
        return redirect(request,'photos/add.html')
    

