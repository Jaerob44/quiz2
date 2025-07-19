from symtable import Class

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Portfolio

def applicant_list_view(request):
    applicants = User.objects.filter(portfolio__isnull=False).order_by('first_name')
    context = {
        'applicants': applicants,
        'position': 'Junior Developer'
    }
    return render(request, 'portfolio/applicant_list.html', context)

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'portfolio'

    def get_object(self, queryset=None):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        return Portfolio.objects.get(user=user)

class ApplicantDeleteView(DeleteView):
    model = User
    template_name = 'portfolio/applicant_confirm_delete.html'
    success_url = reverse_lazy('applicant_list')
    context_object_name = 'user_to_delete'

    def get_object(self, queryset=None):
        username = self.kwargs['username']
        return get_object_or_404(User, username=username)

    def form_valid(self, form):
        return super().form_valid(form)
