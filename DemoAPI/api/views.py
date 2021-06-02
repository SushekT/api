from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from DemoAPI.models import Snippet
from .serializer import SnippetSerializer

def snippetList(request):
    if request.method == "GET":
        s = Snippet.objects.all()
        serializer = SnippetSerializer(s, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        data = JSONParser().parse(request)
        s = SnippetSerializer(data=data)

        if s.is_valid():
            s.save()
            return JsonResponse(s.data, status = 201)
        return JsonResponse(s.errors, status=400)
