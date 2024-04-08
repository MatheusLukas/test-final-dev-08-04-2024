from django import forms
from consumer.models import CONSUMER_TYPE_CHOICES
from consumer.models import Consumer


class CalculatorForm(forms.Form):
    number1 = forms.IntegerField(label='Primeiro mês' ,widget=forms.NumberInput(attrs={'placeholder': 'Digite o valor'}), label_suffix=" (R$):")
    number2 = forms.IntegerField(label='Segundo mês',widget=forms.NumberInput(attrs={'placeholder': 'Digite o valor'}), label_suffix=" (R$):")
    number3 = forms.IntegerField(label='Terceiro mês',widget=forms.NumberInput(attrs={'placeholder': 'Digite o valor'}), label_suffix=" (R$):")
    distributor_tax = forms.FloatField(label='Tarifa da Distribuidora',widget=forms.NumberInput(attrs={'placeholder': 'Digite o valor'}))
    tax_type = forms.ChoiceField(label='Tipo de Consumidor', choices=CONSUMER_TYPE_CHOICES)

class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['name', 'document', 'city', 'state', 'consumer_type', 'consumption_range', 'cover_value', 'distributor_tax']
        widgets = {
            'consumer_type': forms.Select(choices=CONSUMER_TYPE_CHOICES)
        }



     