from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

import stripe
stripe.api_key = settings.STRIPE_SECRET

class CreditCard (models.Model):
  customer_id = models.CharField(max_length=255, blank=True, null=True)
  
  name = models.CharField('Name on Card', max_length=255, blank=True, null=True)
  last4 = models.CharField('Last 4 Digits', max_length=4)
  ctype = models.CharField('Card Type', max_length=25)
  exp_month = models.IntegerField('Expiration Month')
  exp_year = models.IntegerField('Expiration Year')
  
  active = models.BooleanField(default=True)
  
  created = models.DateTimeField(auto_now_add=True)
  
  def __unicode__ (self):
    return self.name + ' - ' + self.last4
  
  class Meta:
    ordering = ('-created',)
    
  def expiration (self):
    return '%d/%d' % (self.exp_month, self.exp_year)
    
  def create_customer (self, token):
    customer = stripe.Customer.create(card=token, description=self.name)
    self.customer_id = customer.id
    self.save()
    
  def charge (self, amount, description, token=None):
    #Amount should be in cents
    if token:
      charge = stripe.Charge.create(amount=amount, currency="usd", card=token, description=description)
      
    else:
      charge = stripe.Charge.create(amount=amount, currency="usd", customer=self.customer_id, description=description)
      
    ch = Charge(charge_id=charge.id, card=self, amount=amount, desc=description)
    ch.save()
    
class Charge (models.Model):
  charge_id = models.CharField(max_length=255)
  card = models.ForeignKey(CreditCard)
  
  amount = models.IntegerField(help_text="In Cents")
  desc = models.CharField('Description', max_length=255)
  refunded = models.IntegerField(blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)
  
  def Amount (self):
    return '%.2f' % (self.amount / 100.0)
    
  def Refunded (self):
    if self.refunded:
      return '%.2f' % (self.refunded / 100.0)
      
    return ''
    
  def __unicode__ (self):
    return self.desc
    
  class Meta:
    ordering = ('-created',)
    get_latest_by = 'created'
    
  def Actions (self):
    if self.refunded is None or self.refunded < self.amount:
      url = reverse('tiger:admin_refund', args=[self.id])
      return '<a href="javascript: void()" onclick="refund_charge(\'%s\', %d)">Refund</a>' % (url, self.amount)
      
    return ''
    
  Actions.allow_tags = True
  
SUB_STATUS = (
  ('active', 'Active'),
  ('expired', 'Expired'),
  ('Cancelled', 'Cancelled'),
)

class Subscription (models.Model):
  card = models.ForeignKey(CreditCard)
  status = models.CharField(max_length=10, choices=SUB_STATUS)
  customer_id = models.CharField(max_length=255)
  plan_id = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  
  def __unicode__ (self):
    return self.plan_id + ' - ' + str(self.id)
    
  class Meta:
    ordering = ('-created',)
    get_latest_by = 'created'
    