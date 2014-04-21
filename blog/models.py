from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=140)
	description = models.TextField(max_length=140)
	content = models.TextField()
	slug = slugify(title)
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	slug = models.SlugField()
	link = models.URLField(blank=True)
	link_description = models.CharField(max_length=140, blank=True)
	image_source = models.ImageField(upload_to='images/posts', blank=True, null=True)

	class Meta:
		ordering = ['-created']
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('blog.views.getpost', args=[self.slug])

class Project(models.Model):
	title = models.CharField(max_length=140)
	description = models.TextField(max_length=140)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	link = models.URLField(blank=True)
	link_description = models.CharField(max_length=140, blank=True)
	image_source = models.ImageField(upload_to='images/projects',blank=True, null=True)

	class Meta:
		ordering = ['-created']
	def __str__(self):
		return self.title

class Intro(models.Model):
	title = models.CharField(max_length=140)
	context = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	
	class Meta:
		ordering = ['-context']
	def __str__(self):
		return self.title
