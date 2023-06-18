from rest_framework.serializers import ModelSerializer
from example.models import Vulnerability

class VulnerabilitySerializer(ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = ['id', 'code']
