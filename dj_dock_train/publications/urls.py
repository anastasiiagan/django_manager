from django.urls import path
from .views import PublicationListView, PublicationCreateView, PublicationDetailView

app_name = "publications"  #name of folder

urlpatterns = [
    path('', PublicationListView.as_view(), name='publication-list'),
    path('<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('create/', PublicationCreateView.as_view(), name='publication-create'),
]