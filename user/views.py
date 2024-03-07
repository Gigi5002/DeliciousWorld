from django.contrib.auth import login
from rest_framework import status
from rest_framework.views import Response, APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import UserLoginSerializer, UserListSerializers, UserCreateSerializer


class UserListView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request):
        paginator = self.pagination_class()
        users = User.objects.all()
        result_page = paginator.paginate_queryset(users, request)
        serializer = UserListSerializers(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class UserCreateView(APIView):

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data, context={'requesr':request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            return Response(status.HTTP_202_ACCEPTED)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.session.flush()
        return Response(data='Вы успешно вышли!', status=status.HTTP_200_OK)