from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Information

# ModelSerializer
# 一组自动确定的字段。
# 默认简单实现的create()
# 和update()
# 方法。

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class InformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Information
        fields = ('url','in_id','in_title','in_time','in_site','in_introduce')