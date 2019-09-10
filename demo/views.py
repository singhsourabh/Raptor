from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import CrawlDemoForm
from rest_framework.status import HTTP_200_OK, HTTP_412_PRECONDITION_FAILED
from .task import crawl_one_view


class Index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        return Response({})


class DemoCrawl(APIView):

    def post(self, request):
        data = CrawlDemoForm(request.POST)
        if data.is_valid():
            url = data.cleaned_data['url']
            data = crawl_one_view(url)
            return Response(data, HTTP_200_OK)
        return Response(data.errors.as_json(), status=HTTP_412_PRECONDITION_FAILED)
