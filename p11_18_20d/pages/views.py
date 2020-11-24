from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def homepage_view(request):
    my_con={
        "my_text":"i love allah",
        "this_is_true":True,
        "my_num":1105003,
        "my_list":[
        111,112,113,114
    ]
    }
    return render(request,"home.html",my_con)

def contactpage_view(request):
    return render(request,"contact.html")