from django.urls import path

from . import views

# app_name for namespacing
# https://docs.djangoproject.com/en/4.1/intro/tutorial03/#namespacing-url-names
app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # int: converter
    # question_id: pattern name
    # ':': separator
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
