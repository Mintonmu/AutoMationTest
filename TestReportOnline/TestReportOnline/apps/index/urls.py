from django.conf.urls import url
from .views import TestCaseAPI,TestSystemMultipleAPI2,TestSystemVagueQuery

urlpatterns = [
    url(r'^$', TestCaseAPI.as_view({"get": "list", "post": "create"})),
    url(r'^(?P<pk>\d+)/$', TestCaseAPI.as_view({"get": "retrieve", "delete": "destroy", "put": "update"})),
    url(r'^getresultByresult=(?P<result>(passed|failed))/$', TestSystemMultipleAPI2.as_view({"get": 'retrieve'})),
    url(r'^getresultBytaskname=(?P<taskname>\w+)/$', TestSystemMultipleAPI2.as_view({"get": 'retrieve'})),
    url(r'^getresultBycreate_worker=(?P<create_worker>.*)/$', TestSystemMultipleAPI2.as_view({"get": 'retrieve'})),
    url(r'^getresultBycase_number=(?P<case_number>.*)/$', TestSystemMultipleAPI2.as_view({"get": 'retrieve'})),
    url(r'getresultByVague', TestSystemVagueQuery.as_view())
]
