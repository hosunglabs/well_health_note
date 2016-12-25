from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q

from .models import Disease
from .forms import PostForm

import operator

def post_list(request):
    disease_list = Disease.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'disease/post_list.html', {'disease_list': disease_list})

def post_detail(request, pk):
	disease = get_object_or_404(Disease, pk=pk)
	return render(request, 'disease/post_detail.html', {'disease': disease})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('disease.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'disease/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Disease, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('disease.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'disease/post_edit.html', {'form': form})

def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        disease_list = Disease.objects.filter(name__contains=query)
    return render(request, 'disease/result.html', {'disease_list': disease_list})
