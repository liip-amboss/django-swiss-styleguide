from django.conf.urls import url  # NOQA

from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login /Logout
    url(r'^auth/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^auth/logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # password change
    url(r'^swiss_auth/password_change/$',
        auth_views.password_change,
        {'template_name': 'swiss_auth/change.html'},
        name='password_change'),
    url(r'^swiss_auth/password_change/done/$',
        auth_views.password_change_done,
        {'template_name': 'swiss_auth/change_done.html'},
        name='password_change_done'),

    # password reset
    url(r'^swiss_auth/password_reset/$',
        auth_views.password_reset,
        {'template_name': 'swiss_auth/reset.html'},
        name='password_reset'),
    url(r'^swiss_auth/password_reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'swiss_auth/reset_done.html'},
        name='password_reset_done'),
    url(r'^swiss_auth/password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  # noqa
        auth_views.password_reset_confirm,
        {'template_name': 'swiss_auth/reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^swiss_auth/password_reset/complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'swiss_auth/reset_complete.html'},
        name='password_reset_complete'),
]
