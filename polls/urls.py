from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('decision', views.DecisionView.as_view(), name='decision'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('stats', views.StatsView.as_view(), name='stats'),
    path('decision/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('decision/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('decision/<int:decision_group_id>/vote/', views.vote, name='vote'),
]