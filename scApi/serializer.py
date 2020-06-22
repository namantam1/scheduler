from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Schedule

class ScheduleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ['url','datetime']