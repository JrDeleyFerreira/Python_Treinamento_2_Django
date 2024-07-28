from django.urls import path
from . import views

app_name = 'blog' # namespace da view, usado no template para declarar a url

urlpatterns = [
    path('', view= views.blog, name='home_blog'),
    path('authors/', view= views.authors, name='blog_authors'),
    path('posts/<int:id>', view= views.posts, name='blog_posts'),
]

