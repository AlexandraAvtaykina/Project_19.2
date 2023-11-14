import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Регистрация пользователя на сайте, form_valid отправляет на почту проверочный код
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verify_email')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            send_mail(
                subject='Подтверждение почты',
                message=f'Код {new_user.ver_code}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email]
            )
        return super().form_valid(form)


# Верификация пользователя, проверка на корректность введенного кода
class VerificationTemplateView(TemplateView):
    template_name = 'users/msg_email.html'

    def post(self, request):
        ver_code = request.POST.get('ver_code')
        user_code = User.objects.filter(ver_code=ver_code).first()
        if user_code:
            user_code.email_verified = True
            user_code.save()
        return redirect('users:login')


# Профиль пользователя
class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


# Функция отвечает за генерацию пароля и его отправку на почту
def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:index'))
