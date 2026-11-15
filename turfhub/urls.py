"""
URL configuration for turfhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from turf_management.views import TurfListCreateView
from turf_management.views import TurfRetrieveUpdateDeleteView
from reservation.views import BookingView,BookingSummaryView
from reservation.views import BookingRetreiveUpdateDeleteView

from accounts.views import AdminCreateView,UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),

    ### TURF URLS
    path('turf/', TurfListCreateView.as_view()),
    path('turf/<int:pk>/', TurfRetrieveUpdateDeleteView.as_view()),

    ### BOOKING URL
    path('booking/',BookingView.as_view()),
    path('booking/summary/',BookingSummaryView.as_view()),
    path('booking/<int:pk>/',BookingRetreiveUpdateDeleteView.as_view()),


    ### ACCOUNTS URL

    path('owner/register/',AdminCreateView.as_view()),
    path('player/register/',UserCreateView.as_view()),

]
