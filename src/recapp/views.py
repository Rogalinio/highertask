from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import Sum
from django.http import JsonResponse


from url_filter.filtersets import ModelFilterSet
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    FormView,
DetailView
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
        return super().form_valid(form)

class GradeFormView(FormView):
    template_name = "recapp/recapp_add-mark.html"
    form_class = GradeModelForm
    queryset = Grade.objects.all()
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)


class CandidatesListView(ListView):
    template_name = "recapp/candidate_list.html"
    context_object_name = 'object_list'
    queryset = Candidate.objects.all()


class HomeView(View):
    def get(self,request, *args,**kwargs):
        return render(request, "home.html",{})



class UserFilterSet(ModelFilterSet):
    class Meta(object):
        model = Grade

class MyDetailView(ListView):
    model = Grade
    template_name = 'recapp/candidate_detail_gradelist.html'
    def get_queryset(self):
        return Grade.objects.filter(candidate_id=self.kwargs['pk'])
    #context_object_name = 'object_list'




