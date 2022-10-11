from atexit import register
from re import template
from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('dash', views.dash, name='dash'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('deposit', views.deposit, name='deposit'),
    path('invest', views.invest, name='invest'),
    path('walleth', views.walleth, name='walleth'),
    path('withdrawal', views.withdrawal, name='withdrawal'),
    path('i_history', views.i_history, name='i_history'),
    path('w_history', views.w_history, name='w_history'),
    path('kyc', views.kyc, name='kyc'),
    path('transaction', views.transaction, name='transaction'),
    path('contact', views.contact, name='contact'),
    path('prof', views.prof, name='prof'),
    path('plan', views.plan, name='plan'),
    path('policy', views.policy, name='policy'),
    path('send_mail', views.send_mail, name='send_mail'),
    path('pay1', views.pay1, name='pay1'),
    path('pay2', views.pay2, name='pay2'),
    path('pay3', views.pay3, name='pay3'),
    path('pay4', views.pay4, name='pay4'),
    path('pay5', views.pay5, name='pay5'),
    path('pay6', views.pay6, name='pay6'),
    path('pay7', views.pay7, name='pay7'),

    # password reset view
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
    
    # password change
    path('change_password/', PasswordChangeView.as_view(template_name="chge_pass.html", success_url= reverse_lazy('password_change_done')),
     name="password_change"),
    
    path('change_password/done/', PasswordChangeDoneView.as_view(template_name="chge_pass_done.html"), name="password_change_done"),



]

