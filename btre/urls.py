from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


from django.contrib.staticfiles.views import serve as serve_static
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', never_cache(serve_static)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# url(r'^static/(?P<path>.*)$', never_cache(serve_static)),
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
