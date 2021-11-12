from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def main(request):
    posts = Post.objects.all()
    return render(request,'index.html', {'home': 'active', 'posts': posts} )

def about(request):
    return render(request,'about.html',  {'about': 'active'})

def post(request):
    return render(request,'post.html',  {'post': 'active'})
    
def contact(request):
    return render(request,'contact.html',  {'contact': 'active'})

# Чисто если написать # # 127.0.0.1:8000/hello/?a=10&b=15
# выйдет HELLO World 25
#     c = request.GET.get('c',10)
#     a = int(request.GET.get('a'))
#     b = int(request.GET.get('b'))
#     return HttpResponse(f"HELLO World {a+b}")
# # 127.0.0.1:8000/hello/?a=10&b=15

# Create your views here.

