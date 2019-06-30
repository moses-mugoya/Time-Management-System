from rest_framework.serializers import ModelSerializer
from activity.models import Activities


class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activities
        fields = ('id', 'activity', 'date', 'duration')
