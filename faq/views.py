from django.shortcuts import render

def view_faq(request):
    """
    View to render FAQ page
    """
    return render (request, "faq/faq.html")
