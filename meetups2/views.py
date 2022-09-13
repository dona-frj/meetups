from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import meetup


# Create your views here.


def index(request):
    meetups = meetup.objects.all()

    return render(request, 'meetups2/index.html',
                  {'meetups': meetups})


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = meetup.objects.get(slug=meetup_slug)
        return render(request,
                      'meetups2/meetup_details.html', {
                          'meetup_title': selected_meetup.title,
                          'meetup_description': selected_meetup.description
                      })
    except Exception:
        return render(request, 'meetups2/meetup_details.html',
                      {'meetup_found': False

                       })
