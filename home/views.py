from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Rediriger vers la page de profil après la connexion
        else:
            messages.error(request, 'Identifiants incorrects. Veuillez réessayer.')  # Message d'erreur en cas d'échec d'authentification
    return render(request, 'login.html')

@login_required
def profile(request):
    user = request.user  # Récupérer l'utilisateur connecté
    context = {
        'username': user.username,
        # Autres données que vous souhaitez passer au template...
    }
    return render(request, 'profile.html', context)