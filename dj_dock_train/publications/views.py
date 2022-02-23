from django.shortcuts import render, redirect, reverse
from .models import Publication
from .forms import PublicationForm
from django.views import generic

# Create your views here.
class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class PublicationListView( generic.ListView):
    template_name = "publications/publication_list.html"
    context_object_name = "publications"

    def get_queryset(self):
        return Publication.objects.all()

class PublicationDetailView(generic.DetailView):
    template_name = "publications/publication_detail.html"
    queryset = Publication.objects.all()
    context_object_name = "publication" 

class PublicationCreateView( generic.CreateView):
    template_name = "publications/publication_create.html"
    form_class = PublicationForm
    
    def get_success_url(self):
        return reverse("publications:publication-list")

    def form_valid(self, form):
        # TO DO send email
        '''send_mail(
            subject="A lead has been created", 
            message="Go to the site to see a new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )'''
        return super(PublicationCreateView, self).form_valid(form)