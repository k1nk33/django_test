from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletters.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact/$', 'newsletters.views.contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
]
