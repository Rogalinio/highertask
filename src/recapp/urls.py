from django.urls import path
from .views import (
    GradeFormView,
    GradeCreateView,
    CandidatesListView,


)



app_name = "recapp"
urlpatterns = [
    path('', CandidatesListView.as_view(), name='recapp-list'),
    path('add-mark/', GradeCreateView.as_view(), name='recapp-addmark'),
    #path('<int:id>/', , name='recapp-detail'),
    ]
