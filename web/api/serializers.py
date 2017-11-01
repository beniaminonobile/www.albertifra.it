# -*- coding: utf-8 -*-

from rest_framework import serializers

from django.contrib.auth import models


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permission
        fields = '__all__'
