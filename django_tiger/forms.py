from django import forms
from django.conf import settings

from .models import CreditCard

class CCForm (forms.ModelForm):
  token = forms.CharField(max_length=255, widget=forms.HiddenInput)
  
  stripe_name = forms.CharField(label='Name on Credit Card', max_length=255, required=False)
  stripe_number = forms.CharField(label='Card Number', max_length=255, required=False)
  stripe_cvc = forms.CharField(label='Card Verfication Code', max_length=10, required=False)
  stripe_month = forms.IntegerField(label='Expiration Month (MM)', required=False)
  stripe_year = forms.IntegerField(label='Expiration Year (YYYY)', required=False)
  
  class Meta:
    model = CreditCard
    widgets = {
      'name': forms.HiddenInput,
      'last4': forms.HiddenInput,
      'exp_month': forms.HiddenInput,
      'exp_year': forms.HiddenInput,
      'ctype': forms.HiddenInput,
    }
    
    exclude = ('active', 'customer_id')
    
  class Media:
    js = ('https://js.stripe.com/v1/', 'tiger/tiger.js')
    
  def pubkey (self):
    return 'Stripe.setPublishableKey(\'%s\');' % settings.STRIPE_PUB
    