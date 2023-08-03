from django.views.generic import TemplateView   
from django.http import HttpResponse 

# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"
