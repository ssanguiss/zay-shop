from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import gettext as _

from accounts.forms import LoginForm, ProfileForm, RegistrationForm


def _get_next_url(request):
    """`next` parametrini xavfsiz tarzda oladi (open redirect'dan himoya)."""
    next_url = request.POST.get('next') or request.GET.get('next') or ''
    if next_url and url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return next_url
    return ''


def register_view(request):
    if request.user.is_authenticated:
        return redirect('products:home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('products:home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('products:home')

    next_url = _get_next_url(request)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                # "Remember me" belgilanmagan bo'lsa, brauzer yopilganda sessiya tugaydi
                if not request.POST.get('remember'):
                    request.session.set_expiry(0)
                return redirect(next_url or 'products:home')

            # Shablondagi form.non_field_errors shuni ko'rsatadi
            form.add_error(None, _('Invalid username or password.'))
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'next': next_url})


@login_required
def logout_view(request):
    logout(request)
    return redirect('products:home')


@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'profile.html', {'user': user, 'form': form})