from django.urls import path

from gestionlivre.views import livreviewlist, livredetail

urlpatterns = [
    path('', livreviewlist.as_view(), name='livre_list'),
    path('<int:pk>/', livredetail.as_view(), name='livre_detail')
]