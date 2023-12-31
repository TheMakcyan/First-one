from django.urls import include,path
from rest_framework import routers
from polls import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
