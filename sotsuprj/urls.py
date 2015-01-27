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
	url(r'^add_relation', 'sotsuapp.views.add_relation'),
	url(r'^add_diagnosis', 'sotsuapp.views.add_diagnosis'),
	url(r'^add_medicine', 'sotsuapp.views.add_medicine'),
	url(r'^search', 'sotsuapp.views.search'),
)
