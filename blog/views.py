from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from blog.models import Post, Project, Intro
from django.core.mail import send_mail
from forms import ContactForm
from postmark import PMMail

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
		if form.is_valid():
			message = PMMail(
				 api_key = '4c76042b-f1ee-4e39-a8be-1e123b4a7d10',
                 subject = form.cleaned_data['subject'],
                 sender = 'rgott105@mtroyal.ca',
                 to = 'rgotto2@gmail.com',
                 text_body = form.cleaned_data['message'],
                 tag = "Site email")
		if message.send():
			status = "That shit is on its wasy westside"
			return render(request, 'email.html', {
		'status': status,})
		else:
			status = "There seems to be a problem with my email service just shoot me and email \@ iamrylangotto@gmail.com"
			render(request, 'email.html', {
		'form': form,})
	else:
		form = ContactForm()
	return render(request, 'contact.html', {
		'form': form,})


def projects(request):
	projects = Project.objects.all()[:5]
	return render(request, 'projects.html', {'projects':projects})

def getpost(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'getpost.html', {'post':post} )





