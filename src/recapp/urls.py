from django.urls import path
from .views import (
    GradeFormView,
    GradeCreateView,
    CandidatesListView,
    MyDetailView


)



app_name = "recapp"
urlpatterns = [
    path('', CandidatesListView.as_view(), name='recapp-list'),
    path('add-mark/', GradeCreateView.as_view(), name='recapp-addmark'),
    path('<int:pk>/', MyDetailView.as_view(), name='detail'),
    #path('<int:id>/', , name='recapp-detail'),
    ]
