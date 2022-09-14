from django.urls import path

from . import views

# app_name for namespacing
# https://docs.djangoproject.com/en/4.1/intro/tutorial03/#namespacing-url-names
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    # int: converter
    # question_id: pattern name
    # ':': separator
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
