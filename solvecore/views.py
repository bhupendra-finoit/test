from django.shortcuts import render


def custom_handler403(request):
    """
    """
    return render(request, '403.html', {})


def custom_handler404(request):
    """
    """
    return render(request, '404.html', {})


def custom_handler500(request):
    """
    """
    return render(request, '500.html', {})
