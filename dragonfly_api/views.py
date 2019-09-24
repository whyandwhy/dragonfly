from django.contrib.auth.models import User, Group
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Information
from rest_framework import viewsets
from dragonfly_api.serializers import UserSerializer, GroupSerializer, InformationSerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all().order_by('in_time')
    serializer_class = InformationSerializer

    @action(detail=False)
    def school(self,request,*args,**kwargs):
        ti_se = Information.objects.all()
        page = PageNumberPagination()
        page_roles = page.paginate_queryset(queryset=ti_se, request=request, view=self)
        ser = InformationSerializer(instance=page_roles, many=True)
        # serializer = self.get_serializer(ti_se, many=True)
        return Response(ser.data)
        # return Response(serializer.data)

    @action(detail=False)
    def FiltrateSchool(self,request,*args,**kwargs):
        FiltrateData = Information.objects.all().values_list("in_time","in_site")
        FiltrateData_a = Information.objects.all()
        serializer = self.get_serializer(FiltrateData, many=True)
        # return Response(serializer.data)
        print('*********************')
        print(FiltrateData_a)
        print('*********************')
        print('#####################')
        print(FiltrateData)
        print('#####################')







