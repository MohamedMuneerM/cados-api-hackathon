from rest_framework import serializers
from . import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

    # add default company logo to response data (sample data)
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response.setdefault('company_logo', 'https://i.pravatar.cc/200')
        return response

class AdvocateSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True, read_only=True)
    class Meta:
        model = models.Advocate
        fields = '__all__'

    # add default profile pic to response data (sample data)
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response.setdefault('profile_pic', 'https://i.pravatar.cc/200')
        return response
