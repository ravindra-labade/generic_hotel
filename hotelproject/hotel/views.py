
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Hotel

class Add_hotel(CreateView):
    model = Hotel
    fields = "__all__"


class List_hotel(ListView):
    model = Hotel

class Detail_hotel(DetailView):
    model = Hotel


class Update_hotel(UpdateView):
    model = Hotel

    fields = "__all__"
    success_url = "/"

class Delete_hotel(DeleteView):
    model = Hotel
    success_url = "/"
    template_name = "hotel/Hotel_confirm.html"
