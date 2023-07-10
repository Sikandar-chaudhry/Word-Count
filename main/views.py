from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render (request , "main/index.html")

def counter(request):
    if request.method == "POST":
        words = request.POST.get("text", "")
        total_words = len(words.split())
        return render(request, 'main/counter.html', {
            "number_of_words": total_words
        })
    else:
        return render(request, 'main/index.html')