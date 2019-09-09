from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_412_PRECONDITION_FAILED
from rest_framework.permissions import IsAuthenticated, AllowAny
from .forms import CrawlForm
from .task import crawl_one_view
from .models import User


class Crawl(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = CrawlForm(request.POST)
        if data.is_valid():
            rollno = data.cleaned_data['roll_no']
            url = data.cleaned_data['url']
            reciever = request.user.reciever
            crawl_one_view(rollno, url, reciever)
            return Response({'task scheduled'}, HTTP_200_OK)
        return Response(data.errors.as_json(), HTTP_412_PRECONDITION_FAILED)
