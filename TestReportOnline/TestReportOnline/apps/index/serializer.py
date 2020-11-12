from rest_framework.serializers import ModelSerializer
from .models import Testcaseresult


class TestCaseSerializer(ModelSerializer):
    class Meta:
        model = Testcaseresult
        exclude = []
