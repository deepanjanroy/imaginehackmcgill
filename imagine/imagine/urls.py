from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from ideastorm import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imagine.views.home', name='home'),
    # url(r'^imagine/', include('imagine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^$', views.index, name='home'),
        url(r'^ideas/$', views.idealist, name='idea-list'),
    # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
        url(r'^logout/$', views.sample_logout, name='logout'),
        url(r'^logged_in/$', views.sample_logged_in, name='logged_in'),
        url(r'^current_user/$', views.current_user, name='current_user'),
        url(r'^login/$', views.imagine_login, name='login'),
        url(r'^signup/$', views.signup, name='signup'),

        url(r'', include('social.apps.django_app.urls', namespace='social')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


