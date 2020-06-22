from .serializer import ScheduleSerializer,Schedule
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.http import JsonResponse
from django.utils import timezone
from background_task import background



@background(schedule=100)
def notify_user(string):
    r = requests.get(string)
    # do something here
    print(r)

@api_view(['GET'])
def schedule(request):
    serializer = ScheduleSerializer(data=request.GET)
    if serializer.is_valid():
        url = serializer.validated_data.get('url')
        date_time = serializer.validated_data.get('datetime')
        now = timezone.localtime(timezone.now())
        if date_time > now:
            notify_user(url,schedule=date_time)
            serializer.save()                                                           #saving the data get from request
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'datetime_error':'datetime should be later than now'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PingView(APIView):
    def get(self, request):
        return Response({'status': 'ok'})


