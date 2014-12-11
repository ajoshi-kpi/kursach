from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from publication.models import Publication, Comments
from django.core.context_processors import csrf
# Create your views here.

def mainAll(request):
	view = "Головна"
	return render_to_response('mainAll.html',{'name':view, 'publications':Publication.objects.all()})

def mainCertain(request, publication_id):
	view = "Головна"
	return render_to_response('mainCertain.html',{'name':view, 'publication':Publication.objects.get(id=publication_id), 'comments':Comments.objects.filter(comments_publication_id = publication_id)})

def registration(request):
	view = "Реєстрація"
	return render_to_response('registration.html',{'name':view})

def search(request):
	view = "Пошук"
	return render_to_response('search.html',{'name':view})

def contacts(request):
	view = "Контакти"
	return render_to_response('contacts.html',{'name':view})

def about(request):
	view = "Про нас"
	return render_to_response('about.html',{'name':view})

def addPublication(request):
	view = "Додати публікацію"
	return render_to_response('addPublication.html',{'name':view})

def search(request):
	view = "Пошук"
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		args={}
		args.update(csrf(request))
		args['publications'] = Publication.objects.filter(publication_title__icontains = q)
		return render_to_response('general.html', {'publications':args['publications'], 'q':q, 'name':view})
	else:
		redirect('/main/all')