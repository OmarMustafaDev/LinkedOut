from django.contrib.auth.views import LoginView

from users.forms import EmailLoginForm


class login_view(LoginView):
    form_class=EmailLoginForm
    template_name="users/login.html"
    redirect_authenticated_user = True


