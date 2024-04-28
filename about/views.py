from django.shortcuts import render

def about_page(request):
    """
    View to render about page
    """
    return render (request, "about/about.html")
