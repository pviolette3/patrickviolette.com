from blog.models import Post
from django.shortcuts import render_to_response

def tags(request, tag):
  print "got tag " + str(tag)
  posts = Post.objects.filter(tags__name__in=tag)
  return render_to_response("tags.html", {"posts": posts, "tag": tag})
