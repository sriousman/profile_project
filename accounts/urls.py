from django.conf.urls import url
from django.views import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'sign_in/$', views.sign_in, name='sign_in'),
    url(r'login/$', views.sign_in, name='sign_in'),
    url(r'sign_up/$', views.sign_up, name='sign_up'),
    url(r'sign_out/$', views.sign_out, name='sign_out'),
    url(r'profile/$', views.profile, name='profile'),
    url(r'password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

]
