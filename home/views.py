from django.shortcuts import render

# Create your views here.
def credits(request):
    content = "Nicky\nPeter"

    return HttpResponse(content, content_type="text/plain")
def About(request):
    content = "This website is for musician and bands to utilize"

    return HttpResponse(content, content_type="text/plain")

def news(request):
    data = {
        'news' : [
            "Riffmates now has a news page!",
            "Riffmates has its first web page",
        ],
    }

    return render(request, "news2.html", data)

