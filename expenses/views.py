# Create your views here.
from django.views.generic import (
    DeleteView, CreateView, ListView, UpdateView, DetailView, TemplateView
)
from django.core.urlresolvers import reverse
from django.db.models import Sum

from braces.views import (
    LoginRequiredMixin, UserFormKwargsMixin, FormValidMessageMixin
)


from .models import Transfer
from .forms import ExpenseCreateForm, IncomeCreateForm

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['latest_transfers'] = Transfer.objects.filter(user=self.request.user)[:5]
        
        income = Transfer.objects.filter(user=self.request.user, incoming=True).aggregate(Sum('amount'))
        expense = Transfer.objects.filter(user=self.request.user, incoming=False).aggregate(Sum('amount'))
        context['account_balance'] = (income['amount__sum'] or 0) - (expense['amount__sum'] or 0)
        return context
        

class TransferListView(LoginRequiredMixin, ListView):
    model = Transfer
    template_name = 'expenses/transfer_list.html'
    
    def get_queryset(self):
        return Transfer.objects.filter(user=self.request.user)

class ExpenseCreateView(LoginRequiredMixin, FormValidMessageMixin, UserFormKwargsMixin, CreateView):
    form_class = ExpenseCreateForm    
    model = Transfer
    template_name = 'expenses/expense_form.html'
    form_valid_message = 'Expense added!'
    
    def get_success_url(self):
        return reverse('home')
    
    
class IncomeCreateView(LoginRequiredMixin, FormValidMessageMixin, UserFormKwargsMixin, CreateView):
    form_class = IncomeCreateForm    
    model = Transfer
    template_name = 'expenses/income_form.html'
    form_valid_message = 'Income added!'
    
    def get_success_url(self):
        return reverse('home')
    