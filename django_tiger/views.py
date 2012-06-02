from django import http

from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.conf import settings
from django.contrib import messages

from .models import Charge

import stripe
stripe.api_key = settings.STRIPE_SECRET

@staff_member_required
@permission_required('charge.change')
def admin_refund (request, cid):
  try:
    amt = int(request.REQUEST.get('amt'))
    
  except:
    messages.add_message(request, messages.ERROR, 'Invalid refund.')
    return http.HttpResponseRedirect(request.META['HTTP_REFERER'])
    
  chobj = get_object_or_404(Charge, id=cid)
  if chobj.refunded is None or chobj.refunded < chobj.amount:
    if chobj.refunded:
      total = chobj.refunded + amt
      
    else:
      total = amt
      
    if total > chobj.amount:
      messages.add_message(request, messages.ERROR, 'Invalid refund amount.')
      
    else:
      chobj.refunded = total
      chobj.save()
      
      ch = stripe.Charge.retrieve(chobj.charge_id)
      ch.refund(amount=amt)
      
      messages.add_message(request, messages.INFO, 'Refund successful.')
      
  else:
    messages.add_message(request, messages.ERROR, 'Invalid refund.')
    
  return http.HttpResponseRedirect(request.META['HTTP_REFERER'])
  