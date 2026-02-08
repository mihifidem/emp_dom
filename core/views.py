# Vista para listar todos los Domingos publicados
def domingo_list(request):
	domingos = Domingo.objects.filter(is_published=True).order_by('liturgical_time', 'sunday_number')
	return render(request, 'domingos/list.html', {'domingos': domingos})
from django.shortcuts import get_object_or_404
from .models import Domingo
# Vista para mostrar un Domingo por slug
def domingo_detail(request, slug):
	domingo = get_object_or_404(Domingo, slug=slug, is_published=True)
	user_groups = []
	if request.user.is_authenticated:
		user_groups = list(request.user.groups.values_list('name', flat=True))
	return render(request, 'domingos/detail.html', {'domingo': domingo, 'request': request, 'user_groups': user_groups})
from django.contrib.auth import logout
def logout_view(request):
	logout(request)
	return redirect('landing')
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
def login_view(request):
	error_message = None
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		email = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('landing')
		else:
			error_message = 'Correo o contraseña incorrectos.'
	else:
		form = AuthenticationForm()
	return render(request, 'core/login.html', {'form': form, 'error_message': error_message})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from .forms import RegistrationForm
from .decorators import premium_required

@premium_required
def premium_content(request):
    user_groups = []
    if request.user.is_authenticated:
        user_groups = list(request.user.groups.values_list('name', flat=True))
    return render(request, 'core/premium_content.html', {'user_groups': user_groups})

@premium_required
def premium_content_view(request):
    user_groups = []
    if request.user.is_authenticated:
        user_groups = list(request.user.groups.values_list('name', flat=True))
    return render(request, 'premium/content.html', {'user_groups': user_groups})

def landing(request):
	user_groups = []
	if request.user.is_authenticated:
		user_groups = list(request.user.groups.values_list('name', flat=True))
	context = {
		'user_groups': user_groups,
		'qr_range': range(1, 53),
	}
	return render(request, 'core/landing.html', context)

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			if User.objects.filter(username=email).exists():
				form.add_error('email', 'Este correo ya está registrado.')
			else:
				user = User.objects.create_user(username=email, email=email, password=password)
				group = Group.objects.get(name='freeUser')
				user.groups.add(group)
				login(request, user)
				return redirect('landing')
	else:
		form = RegistrationForm()
	return render(request, 'core/register.html', {'form': form})

def upgrade(request):
    return render(request, 'upgrade.html')

def qr_sunday_content(request):
    user_groups = []
    if request.user.is_authenticated:
        user_groups = list(request.user.groups.values_list('name', flat=True))
    context = {
        'user_groups': user_groups,
        'title': 'I Domingo de Adviento – Esperanza',
        'intro': 'Bienvenido al contenido especial del I Domingo de Adviento. Descubre el significado de la esperanza.',
        'full_content': 'Este es el contenido completo para usuarios premium y administradores. Reflexiones, recursos y material litúrgico.',
        'admin_notes': 'Notas administrativas: solo visibles para administradores.'
    }
    return render(request, 'qr/sunday.html', context)
