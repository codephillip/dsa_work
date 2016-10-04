from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def dsa_notes(request):
    return render(request, 'dsa_notes.html')


def about(request):
    return render(request, 'about.html')


def dsa_notes_details(request):
    return render(request, 'dsa_notes_details.html')