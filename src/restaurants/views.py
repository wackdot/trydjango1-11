from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
# def home(request):

#     html_var = "f strings"

#     html_ = f"""<!DOCTYPE html>
#         <html lang=en>
#         <head>
#         </head>
#         <body>
#             <h1>Hello World</h1>
#             <p>This is coming through </p>
#         </body>
#         </html>
#     """
#    return HttpResponse(html_)

def home(request):
    return render(request, "base.html", {"html_var": "context variable"}) #response
