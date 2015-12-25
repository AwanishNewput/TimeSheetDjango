from django.http import HttpResponse
import django_filters
from rest_framework import filters
from tracker.models import EmployeeDetail, TimeSchedual, TimeSheets
from tracker.serializers import EmplSerializer, UserSerializer, TimeSchedualSerializer, TimeSheetSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from tracker.permission import IsOwnerOrReadOnly
from django.db import IntegrityError
from django.core.wsgi import get_wsgi_application


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tracker': reverse('emp-list', request=request, format=format)
    })


class EmployeeList(generics.ListAPIView):
    queryset = EmployeeDetail.objects.all()
    serializer_class = EmplSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EmployeeDetail(generics.RetrieveUpdateAPIView):
    queryset = EmployeeDetail.objects.all()
    serializer_class = EmplSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TimeSchedualList(generics.ListCreateAPIView):

    serializer_class = TimeSchedualSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        try:
            serializer.save(user_id=self.request.user)
        except IntegrityError as e:
            raise e
            question = "Duplicate record entered."
        return render_to_response('tracker/error.html', question)

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return TimeSchedual.objects.filter(user_id__id=user_id)


class TimeSchedualDetail(generics.RetrieveUpdateAPIView):

    serializer_class = TimeSchedualSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        user_id = self.kwargs['pk']
        workdate = self.kwargs['work_date']
        return TimeSchedual.objects.filter(user_id__id=user_id, work_date=workdate)


class TimeSheetList(generics.ListCreateAPIView):
    serializer_class = TimeSheetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def choose(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            work_date = request.work_date
            print(work_date)
            return Response(serializer.data)

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return TimeSchedual.objects.filter(user_id__id=user_id)


class TimeSheetDetail(generics.ListAPIView):

    serializer_class = TimeSheetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        user_id = self.kwargs['pk']
        work_date = self.kwargs['work_date']
        i=0
        while i<3:
            viewlist = TimeSheets.objects.filter(user_id__id=user_id, work_date=work_date,chunk_id=i).values_list('in_time','out_time')
            #x_list = viewlist.split(',')
            print(viewlist)
            i=i+1