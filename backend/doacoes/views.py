from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .forms import DoacaoForm
from .models import Doacao


class DoacoesListView(ListView):
    model = Doacao
    paginate_by = 10


class DoacoesDetailView(DetailView):
    model = Doacao


class DoacoesCreateView(CreateView):
    model = Doacao
    form_class = DoacaoForm


class DoacoesUpdateView(UpdateView):
    model = Doacao
    form_class = DoacaoForm


class DoacoesDeleteView(DeleteView):
    model = Doacao
    success_url = reverse_lazy('doacoes:doacoes_list')
