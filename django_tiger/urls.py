from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('django_tiger.views',
  url(r'^admin/refund/(\d+)/$', 'admin_refund', name='admin_refund'),
)
