from django.shortcuts import render, get_object_or_404
from .models import Category, TrainingContent

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'training/base.html', {
        'categories': categories,
        'page_type': 'list',
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    contents = TrainingContent.objects.filter(category=category)
    return render(request, 'training/base.html', {
        'category': category,
        'contents': contents,
        'categories': Category.objects.all(),
        'page_type': 'detail',
    })