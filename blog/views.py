from django.shortcuts import render, get_object_or_404
from .models import Blog

"""
def allblogs(request):
    blogs=Blog.objects
    return render(request, 'blog/allblogs.html',{'blogs':blogs})

def detail(request, blog_id):
    detailblog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
"""

def optimizewin10(request):
    return render(request, 'home/optimizewin10.html')

def step_1(request):
        return render(request, 'home/step_1.html')

def step_2(request):
        return render(request, 'home/step_2.html')

def step_3(request):
        return render(request, 'home/step_3.html')
"""
def step_4(request):
        return render(request, 'blog/step_4.html')

def step_5(request):
        return render(request, 'blog/step_5.html')
"""
def step3_1(request):
        return render(request, 'home/step_3/step3_1.html')
