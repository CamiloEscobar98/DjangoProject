import requests

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action

from example.models import Vulnerability
from example.api.serializers import VulnerabilitySerializer

class VulnerabilityApiViewSet(ModelViewSet):
    queryset = Vulnerability.objects.all()     
    serializer_class = VulnerabilitySerializer

    def connectApi(self, param = None):
        url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'

        if param is not None:
            response = requests.get(url, param)
        else:
            response = requests.get(url)            

        if response.status_code == 200:
            return response.json()
        
        return {}
        
    def getByVulnerabilityLevel(self, level = None):
        arrayParameters = None

        if level is not None:
            strVulnerabilityLevel = str(level)
            arrayParameters = {'cvssV3Severity' : strVulnerabilityLevel }
        return self.connectApi(arrayParameters)
    

    def list(self, request, *args, **kwargs):
        response = self.connectApi()
        queryset = Vulnerability.objects.filter()

        itemsVulnerabilities = []

        if response:
            itemsVulnerabilities = response.get('vulnerabilities')
            itemsFixed = list(queryset.values_list('code', flat=True))
            itemsVulnerabilitiesFixed = [
                {
                  'id' : item['cve']['id'],
                  'sourceIdentifier' : item['cve']['sourceIdentifier'],  
                  'published' : item['cve']['published'],
                  'lastModified' : item['cve']['lastModified'],
                  'descriptions' : item['cve']['descriptions'],
                  'status' : item['cve']['vulnStatus']
                }
                for item in itemsVulnerabilities if item['cve']['id'] not in itemsFixed]

        response_data = {
            'count' : response.get('totalResults'),
            'results' : itemsVulnerabilitiesFixed
        } 
        return Response(response_data)
    
    @action(detail=False, methods=['GET'], url_path='severity', url_name='severity')
    def getBySeverity(self, request):
        severityLevel = None
        levelParam = request.query_params.get('severity', None)

        if levelParam is not None:
            severityLevel = levelParam

        print(severityLevel)

        response = self.getByVulnerabilityLevel(severityLevel)

        items = response.get('vulnerabilities')

        itemsByVulnerability = []

        if items:
            itemsByVulnerability = [
                 {
                  'id' : item['cve']['id'],
                  'sourceIdentifier' : item['cve']['sourceIdentifier'],  
                  'published' : item['cve']['published'],
                  'lastModified' : item['cve']['lastModified'],
                  'descriptions' : item['cve']['descriptions'],
                  'status' : item['cve']['vulnStatus']
                }
                 for item in items]
        response_data = {
            'count' : response.get('totalResults'),
            'results' : itemsByVulnerability
        }

        return Response(response_data)