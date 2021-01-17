from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, login as auth_login  # accounts의 User모델로 가져오면 X
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView, CreateView
from accounts.forms import ProfileForm
from accounts.models import Profile

User = get_user_model()


# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')
#
class ProfileView(LoginRequiredMixin, TemplateView):  # TemplateView 클래스 적용
    template_name = 'accounts/profile.html'


profile = ProfileView.as_view()


@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_form.html', {
        'form': form,
    })


class SignupView(CreateView):
    model = User,
    form_class = UserCreationForm,
    success_url = settings.LOGIN_REDIRECT_URL,
    template_name = 'accounts/signup_form.html',

    def form_valid(self, form): #django->views->generic->edit.py 참고 (ModelFormMixin에선 유효성 save 후 반환)
        response = super().form_valid(form)
        user = self.object
        auth_login(self.request, user)
        return response


signup = SignupView.as_view()
# signup = CreateView.as_view(
#     model=User,
#     form_class=UserCreationForm,
#     success_url=settings.LOGIN_URL,
#     template_name='accounts/signup_form.html',
# )


# def signup(request):
#     pass


def logout(request):
    pass

# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileForm
#
#
# profile_edit = ProfileUpdateView.as_view()
