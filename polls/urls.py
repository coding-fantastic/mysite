from django.urls import path

from . import views
urlpatterns = [
    #call index function from views
    # execute /polls/
    path('',views.index, name='index'),
    # /polls/5/
    path('<int:question_id',views.detail, name='detail'),
    # call results function from views file
    # /polls/5/results
    path('<int:question_id/results',views.results, name='results'),
    # call vote function from views file
    # /polls/5/vote
    path('<int:question_id/vote',views.vote, name='vote'),
]
