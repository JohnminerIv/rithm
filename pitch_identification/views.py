from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.


class IndexView(ListView):
    template_name = 'pitch_identification/index.html'

    def get(self, request):
        return render(request, self.template_name)
