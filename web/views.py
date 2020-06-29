from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from web.models import Publication


def index(request):
    return render(request, 'main.html')


def status(request):
    return HttpResponse("Status OK")


def contacts(request):
    return render(request, 'contacts.html')



def publications(request):
    sorted_pubs = Publication.objects.all().order_by('-date')
    # sorted_pubs = sorted(publications_data, key=lambda pub: pub['date'], reverse=True)
    return render(request, 'publications.html', {
        'publications': sorted_pubs
    })

def publication(request, pub_id):
    try:
        publication = Publication.objects.get(id=pub_id)

        return render(request, 'publication.html', {'publication': publication})

    except Publication.DoesNotExist:
        return redirect('/')

def post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        if title and text:
            Publication.objects.create(
                title=title,
                text=text
            )
            redirect("/publications")
        else:
            return render(request, 'post.html', {'error' : 'title and text should not be blank'})
    return render(request, 'post.html')
