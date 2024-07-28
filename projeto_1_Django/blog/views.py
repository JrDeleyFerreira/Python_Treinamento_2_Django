from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request= request, template_name= 'blog/index.html')

def authors(request):
    return render(request= request, template_name= 'blog/authors.html')

def posts(request, id):
    context = {'posts' : posts}
    return render(request= request, template_name= 'blog/index.html', context= context)