from blog.models import Post
from django.shortcuts import render_to_response

def tags(request, tag):
  posts = Post.objects.filter(tags__name=tag)
  return render_to_response("tags.html", {"posts": posts, "tag": tag})
