from django.shortcuts import render

def view_faq(request):
    return render (request, "faq/faq.html")
