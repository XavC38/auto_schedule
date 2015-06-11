from django.conf.urls import include, url, patterns
from schedule.views import Home

urlpatterns = patterns('',
               url('^', Home.as_view(), name='index')
)
