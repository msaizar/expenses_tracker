from django import forms

from braces.forms import UserKwargModelFormMixin

from .models import Transfer



class ExpenseCreateForm(UserKwargModelFormMixin, forms.ModelForm):
    
    class Meta:
        model = Transfer
        fields = ('description', 'amount',)

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(ExpenseCreateForm, self).save(commit=False)
        m.incoming = False
        m.user = self.user
        if commit:
            m.save()		
        return m

class IncomeCreateForm(UserKwargModelFormMixin, forms.ModelForm):

    class Meta:
        model = Transfer        
        fields = ('description', 'amount',)
        
    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(IncomeCreateForm, self).save(commit=False)
        m.user = self.user
        if commit:
            m.save()		
        return m
