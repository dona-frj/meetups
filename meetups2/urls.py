from django.urls import path
from . import views

urlpatterns = [

    path('meetups2/', views.index, name='all-meetups'),
    # our-domain.com/meetups2/<dynamic>
    path('meetups2/<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]
