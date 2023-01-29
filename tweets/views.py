from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Tweet


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html")

def tweets_list_view(request, *args, **kwargs):
    return render(request, "tweets/list.html")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404
    return JsonResponse(data=data, status=status)
    
    print(args, kwargs)
    return HttpResponse(f"<h1>Hello tweet No. {kwargs['tweet_id']} </h1>")
    return render(request, "tweets/list.html")