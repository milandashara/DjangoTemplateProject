from django.conf.urls import url, include



from myapp.views import dashboard_view, user_views, ip_range_setting_views

from django.views.generic.base import RedirectView
from myapp.views import login_view
from axes.decorators import watch_login

app_name = 'myapp'
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/myapp/dashboard')),
    
    url(r'^locked/$', login_view.login_locked_view, name='locked_out'),
    url(r'^login', watch_login(login_view.login_view),name='login'),
   
    url(r'^logout', login_view.logout_view,name='logout'),

    
    url(r'^dashboard', dashboard_view.get_switch_mode_view, name='switch-mode'),
    
    url(r'^user/new', user_views.get_new_user_view, name='user-new'),
    url(r'^user/edit', user_views.get_edit_user_view, name='user-edit'),
    url(r'^user/delete', user_views.get_delete_user_view, name='user-delete'),
    url(r'^user', user_views.get_user_view, name='user'),
    url(r'^ip-range-setting', ip_range_setting_views.get_ip_range_setting_view, name='ip-range-setting'),
    url(r'^ip-range-delete', ip_range_setting_views.delete_ip_range_view, name='ip-range-delete'),
    
]