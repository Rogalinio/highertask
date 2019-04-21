from django.shortcuts import render
from django.views import View

from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView
)

from .models import Recruter, Grade, Candidate, Task
from .forms import GradeModelForm

# Create your views here.

class GradeCreateView(CreateView):
    template_name = "recapp/recapp_add-mark.html"
    form_class = GradeModelForm
    queryset = Grade.objects.all()
    success_url = "/"



    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CandidatesListView(ListView):
    template_name = "recapp/candidate_list.html"
    queryset = Candidate.objects.all()

class HomeView(View):
    def get(self,request, *args,**kwargs):
        return render(request, "home.html",{})