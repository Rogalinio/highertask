from django.urls import path
from .views import (
    GradeCreateView,
    CandidatesListView
)



app_name = "recapp"
urlpatterns = [
    path('', CandidatesListView.as_view(), name='recapp-list'),
    path('add-mark/', GradeCreateView.as_view(), name='recapp-addmark'),
    #path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    #path('<int:id>/update/',  ArticleUpdateView.as_view(), name='article-update'),
    #path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    ]
