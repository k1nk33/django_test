from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletters.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact/$', 'newsletters.views.contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Remove above for below when switching

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

