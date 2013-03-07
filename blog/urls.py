from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
  title = "Patrick's Blog"
  description = "My blog posts"
  link = "/blog/feed"

  def items(self):
    return Post.objects.all().order_by("-created")

  def item_title(self, post):
    return post.title

  def item_description(self, post):
    return post.body

  def item_link(self, post):
    return u"/blog/%d" % post.id

urlpatterns = patterns('blog.views',
   url(r'^$', ListView.as_view( 
     queryset=Post.objects.all().order_by("-created")[:2],
     template_name="blog.html")),
   url(r'^(?P<pk>\d*)$', DetailView.as_view(
     model=Post,template_name="post.html")),
   url(r'^archive/$',ListView.as_view(
     queryset=Post.objects.all().order_by("-created"),
     template_name="archive.html")),
   url(r'^tag/(?P<tag>\w+)$', 'tags'),
   url(r'^feed/$', BlogFeed()),
)
