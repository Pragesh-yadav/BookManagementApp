from rest_framework import serializers
from .models import Book


class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
# class CompanyDetailSerializer(serializers.ModelSerializer):
#     full_address = serializers.CharField(read_only=True)

#     class Meta:
#         model = Company
#         fields = "__all__"
