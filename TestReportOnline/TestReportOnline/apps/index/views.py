import django_filters
# Create your views here.
import importlib

from django.http import Http404
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import TestCaseSerializer
from .models import Testcaseresult

from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework.filterset import FilterSet
from django_filters import filters


def count(string, query_alpha):
    i = 0
    for j in string:
        if j == query_alpha:
            i += 1
    return i


class TestCasePagination(PageNumberPagination):
    page_size_query_param = 'page_num'
    max_page_size = 3


class TestCaseAPI(ModelViewSet):
    serializer_class = TestCaseSerializer
    queryset = Testcaseresult.objects.all()


class TestSystemMultipleAPI(APIView):

    def get(self, request):

        param_list = ['create_worker', 'create_time', 'result', 'case_number', 'marker', 'taskname']
        request_data = {}
        for i in param_list:
            p = request.GET.get(i)
            if p:
                if str(p).endswith("/"):
                    p = str(p)[:-1]
                request_data[i] = p
        queryset = None
        if len(request_data) == 1:
            if 'create_worker' in str(request_data):
                queryset = Testcaseresult.objects.filter(create_worker=request_data['create_worker'])
            elif 'create_time' in str(request_data):
                queryset = Testcaseresult.objects.filter(create_time__icontains=request_data['create_time'])
            elif 'result' in str(request_data):
                queryset = Testcaseresult.objects.filter(result=request_data["result"])
            elif 'case_number' in str(request_data):
                queryset = Testcaseresult.objects.filter(case_number=request_data['case_number'])
            elif 'marker' in str(request_data):
                queryset = Testcaseresult.objects.filter(marker__icontains=request_data['marker'])
            elif 'taskname' in str(request_data):
                queryset = Testcaseresult.objects.filter(taskname=request_data['taskname'])

        seriliazer = TestCaseSerializer(queryset, many=True)
        return Response(seriliazer.data)


class ResultFilter(FilterSet):
    result = filters.CharFilter(field_name="result", lookup_expr='__exact')

    class Meta:
        model = Testcaseresult
        fields = ['result']


class TestSystemMultipleAPI2(TestCaseAPI):
    # 局部配置过滤器类
    filter_backends = [DjangoFilterBackend]
    # 参与分类筛选的字段：
    filter_class = ResultFilter

    def get_object(self):

        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_list_or_404(queryset, **filter_kwargs)

        return obj

    def retrieve(self, request, *args, **kwargs):
        path = request.get_full_path()
        from urllib import parse
        path = parse.unquote(path.split("/")[-2])
        # getresultByresult=passed
        req_pa = path.split("By")[-1]
        req_a = req_pa.split("=")[0]
        if req_a in ["result", "marker", "create_worker", "taskname", 'case_number']:
            self.lookup_url_kwarg = req_a
            self.lookup_field = req_a
        queryset = self.get_object()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TestSystemVagueQuery(APIView):

    def get(self, request):

        vague_list = ["create_time", 'marker', "ending_time", 'nodeid']
        now_case_filter = None
        for i in vague_list:
            request_param = request.query_params.get(i)
            if request_param:
                now_case_filter = {"%s__icontains" % i: request_param}

        query_set = Testcaseresult.objects.filter(**now_case_filter)
        if query_set:
            seriliazer = TestCaseSerializer(query_set, many=True)
            return Response(seriliazer.data)
        else:
            raise Http404('MMP')
