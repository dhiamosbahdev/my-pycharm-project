from django.shortcuts import render
from django.views.generic import ListView, DetailView

from gestionlivre.models import livre


class livreviewlist(ListView):
    model =livre
    template_name = "livre_list.html"

class livredetail(DetailView):
    model =livre
    template_name = "livre_detail.html"
# Create your views here.
