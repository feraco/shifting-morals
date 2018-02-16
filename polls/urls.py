from django.urls import path
from django.views import generic

from . import views

line_chart = generic.TemplateView.as_view(template_name='line_chart.html')
line_chart_json = views.LineChartJSONView.as_view()

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('decision', views.DecisionView.as_view(), name='decision'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('stats', views.StatsView.as_view(), name='stats'),
    path('line_chart_json', views.LineChartJSONView.as_view(), name='line_chart_json'),
    path('decision/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('decision/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('decision/<int:decision_group_id>/vote/', views.vote, name='vote'),
]