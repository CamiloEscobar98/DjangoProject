import requests

from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from example.models import Vulnerability
from example.api.serializers import VulnerabilitySerializer

class VulnerabilityApiViewSet(ModelViewSet):
    serializer_class = VulnerabilitySerializer
    queryset = Vulnerability.objects.all()

    def connectApi(self):
        url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
        response = requests.get(url, {})

        if response.status_code == 200:
            return response.json()
    

    def list(self, request, *args, **kwargs):

        response = self.connectApi()

        queryset = Vulnerability.objects.filter()

        if response:
            itemsVulnerabilities = response.get('vulnerabilities')
            itemsFixed = list(queryset.values_list('code', flat=True))
            itemsVulnerabilitiesFixed = [item for item in itemsVulnerabilities if item['cve']['id'] not in itemsFixed]
        else:
            itemsVulnerabilities = []

        queryset = self.filter_queryset(self.get_queryset())

        response_data = {
            'count' : len(itemsVulnerabilitiesFixed),
            'results' : itemsVulnerabilitiesFixed
        } 
        return Response(response_data)

    def aa():
        return 1
    

    def getVulnerabilities(request):
        return 1
       
