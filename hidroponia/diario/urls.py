from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^historico/(?P<dia>[0-9]+)/(?P<mes>[0-9]+)/(?P<ano>[0-9]+)',views.historico, name='historico'),
	url(r'^historico/',views.historico),
	url(r'^temporeal/',views.temporeal),
	url(r'^cadastrar/',views.cadastrar),
	url(r'^buscar',views.buscar),
    url(r'^controlar',views.controlar),
]
