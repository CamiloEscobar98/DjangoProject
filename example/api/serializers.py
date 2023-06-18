from rest_framework.serializers import ModelSerializer
from example.models import Post, Vulnerability


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']

class VulnerabilitySerializer(ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = ['id', 'code']
