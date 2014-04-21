from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from blog.models import Post, Project, Intro
from django.core.mail import send_mail
from forms import ContactForm


# Create your views here.

def home(request):
	post = Post.objects.latest('created')
	project = Project.objects.latest('created')
	intro = Intro.objects.latest('context')
	return render(request, 'home.html', { 'post':post, 'project':project, 'intro':intro })

def blog(request):
	posts = Post.objects.all()[:5]
	return render(request, 'blog.html', { 'posts': posts })

def contact(request):

	if request.method == "POST":
		form = ContactForm(request.POST) 
		if form.is_valid(): # All validation rules pass
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['email']
			recipients = ['rgotto2@gmail.com']
			print "valid form"
			if send_mail(subject, message, sender, recipients):
				print "success"
			return HttpResponseRedirect('home.html') # Redirect after POST
	else:
		form = ContactForm() # An unbound form
	return render(request, 'contact.html', {
		'form': form,})
	


def projects(request):
	projects = Project.objects.all()[:5]
	return render(request, 'projects.html', {'projects':projects})

def getpost(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'getpost.html', {'post':post} )





