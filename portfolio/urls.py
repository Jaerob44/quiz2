from django.urls import path
from . import views
from .views import PortfolioDetailView, ApplicantDeleteView

urlpatterns = [
    path('', views.applicant_list_view, name='applicant_list'),
    path('portfolio/<str:username>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('delete/<str:username>/', ApplicantDeleteView.as_view(), name='applicant_delete'),
]