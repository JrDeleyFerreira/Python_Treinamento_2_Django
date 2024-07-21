from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request= request, template_name= 'blog/index.html')

def authors(request):
    return render(request= request, template_name= 'blog/authors.html')