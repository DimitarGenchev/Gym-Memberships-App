from django.contrib.auth import login, views as auth_views, get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from formtools.wizard.views import SessionWizardView

from GymMembershipsApp.users.forms import UserRegisterForm, UserDetailsForm

UserModel = get_user_model()


class UserRegisterWizardView(SessionWizardView):
    template_name = 'register.html'
    form_list = [UserRegisterForm, UserDetailsForm]

    def done(self, form_list, **kwargs):
        form_data = {}

        for form in form_list:
            form_data.update(form.cleaned_data)

        new_user = UserModel.objects.create_user(
            email=form_data['email'],
            password=form_data['password1'],
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            date_of_birth=form_data['date_of_birth'],
            phone_number=form_data['phone_number'],
        )

        login(self.request, new_user)

        return redirect('index')


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'


class UserLogoutView(auth_views.LogoutView):
    ...
