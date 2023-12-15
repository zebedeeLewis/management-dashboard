from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Sample
from api.serializers import SampleSerializer

@csrf_exempt
def sample_list(request):
    if request.method == 'GET':
        samples = Sample.objects.all()
        serializer = SampleSerializer(samples, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SampleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def sample_detail(request, pk):
    try:
        sample = Sample.objects.get(pk=pk)
    except Sample.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SampleSerializer(sample)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SampleSerializer(sample, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sample.delete()
        return HttpResponse(status=204)


