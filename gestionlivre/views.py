from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView, DetailView
from django.db.models import Q
from gestionlivre.models import livre


class livreviewlist(ListView):
    model =livre
    template_name = "livre_list.html"

class livredetail(DetailView):
    model =livre
    template_name = "livre_detail.html"
# Create your views here.
class recherche(ListView):
    model = livre
    template_name = "resultat.html"

    def get_queryset(self):
        req = self.request.GET.get('q', '')  # ✅ self.request + valeur par défaut
        if req:
            return livre.objects.filter(Q(titre__icontains=req))
        return livre.objects.none()
