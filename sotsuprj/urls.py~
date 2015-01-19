from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^home', 'sotsuapp.views.home'),
	url(r'^list', 'sotsuapp.views.plist'),
	url(r'^login', 'sotsuapp.views.login_view'),
	url(r'^logout', 'sotsuapp.views.logout_view'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^user/(?P<u_id>\d+)/$', 'sotsuapp.views.userinfo'),
)
