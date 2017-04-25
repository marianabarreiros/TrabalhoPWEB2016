from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.sistema_financeiro, name='sistema_financeiro')
]