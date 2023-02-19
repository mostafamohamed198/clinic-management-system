from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('patientinfo/<int:id>', views.patientinfo, name='patientinfo'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('edit/<int:idd>', views.editpatient, name='edit'),
    path('profile/<int:patientid>/<int:infoid>', views.related, name='profile'),
    path('newdrug', views.newdrug, name='newdrug')
    ]   