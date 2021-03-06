from django import forms

from braces.forms import UserKwargModelFormMixin

from .models import Transfer



class ExpenseCreateForm(UserKwargModelFormMixin, forms.ModelForm):

    date_added = forms.DateField(required=False, label='Date', input_formats=('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M', '%Y-%m-%d',), help_text="Format is YYYY/MM/DD")
    
    class Meta:
        model = Transfer
        fields = ('description', 'amount', 'date_added')

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(ExpenseCreateForm, self).save(commit=False)
        m.incoming = False
        m.user = self.user
        if commit:
            m.save()		
        return m

class IncomeCreateForm(UserKwargModelFormMixin, forms.ModelForm):

    date_added = forms.DateField(label='Date', input_formats=('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M', '%Y-%m-%d',), help_text="Format is YYYY/MM/DD")

    class Meta:
        model = Transfer        
        fields = ('description', 'amount', 'date_added')
        
    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(IncomeCreateForm, self).save(commit=False)
        m.user = self.user
        if commit:
            m.save()		
        return m
