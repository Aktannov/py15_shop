from django.urls import path

from account.views import RegistrationView, ActivationView, LoginView, LogoutView, ChangePasswordView, \
    ForgotPasswordView, ForgotPasswordComplite, test_view, Ret

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password_complete/', ForgotPasswordComplite.as_view()),
    path('test/', test_view),
    path('ret/', Ret.as_view())
]
# as_view() - классы как функ
