from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class ArtList(generic.ListView):
    queryset = Post.objects.filter(category=1).order_by('-created_on')
    template_name = 'art.html'

class MusicList(generic.ListView):
    queryset = Post.objects.filter(category=2).order_by('-created_on')
    template_name = 'music.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'