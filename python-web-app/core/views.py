# core/views.py
from django.shortcuts import render

def welcome_view(request):
    """A simple view that renders the welcome page."""
    context = {
        'title': 'Welcome to Django',
        'message': 'Your project has been successfully initialized using best practices.'
    }
    return render(request, 'core/welcome.html', context)