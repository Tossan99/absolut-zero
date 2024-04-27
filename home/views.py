from django.shortcuts import render

def home_page(request):
    return render (request, "home/index.html")

# Custom error views
def view_custom403(request, exception=None):
    return render(request, '403.html', status=403)

def view_custom404(request, exception=None):
    return render(request, '404.html', status=404)

def view_custom405(request, exception=None):
    return render(request, '405.html', status=405)

def view_custom500(request, exception=None):
    return render(request, '500.html', status=500)
