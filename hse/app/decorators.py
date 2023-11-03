from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Rediriger l'utilisateur authentifié vers une page d'accueil ou une autre vue
            return redirect('loginPage')  # Remplacez 'nom_de_la_vue' par le nom de la vue de votre choix
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func