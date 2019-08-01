from django.shortcuts import render

# Create your views here.

#0013
from django.utils import timezone
from .models import Post

#0011
def post_list(request):
	#0013
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})