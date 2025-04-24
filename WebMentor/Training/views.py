from django.shortcuts import render
from .models import Category, TrainingContent

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'training/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    contents = TrainingContent.objects.filter(category=category)
    return render(request, 'training/category_detail.html', {
        'category': category,
        'contents': contents,
    })