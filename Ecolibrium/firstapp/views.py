from django.contrib.auth import authenticate, login, get_user_model
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from firstapp.models import *

from firstapp.permission import IsReadOnlyOrIsAdmin
from firstapp.permission import *
from .models import Movie
from .serializers import MovieSerializer, UserSerializer
from firstapp.models import Movie, Genre
from rest_framework.response import Response


from rest_framework import generics
class IndexView(generics.ListAPIView):
    """
    API view for searching Movies
    """
    queryset = Movie.objects.all()
    serializer_class=MovieSerializer
    pagination_class = PageNumberPagination
    search_fields = ('name','director')  # exactly equal to eno.
    ordering_fields = ('popularity',)
    # authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsReadOnlyOrIsAdmin,IsAuthenticated ]

    #
    # def post(self, request):
    #     data = request.data
    #     serli = MovieSerializer(data=data)
    #     if serli.is_valid():
    #         serli.save()
    #         return Response(serli.data)
    #     else:
    #         return Response({'error': 'invalid data'})

class MoviesCreate(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser,IsAuthenticated ]



class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser,IsAuthenticated ]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


class UserCreateView(generics.CreateAPIView):
    # @csrf_exempt
    def post(self,request,*args,**kwargs):
        data=request.data
        isStaff=data.get("isStaff",False)
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            username=serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            if isStaff:
                get_user_model().objects.create_superuser(username=username,password=password,email="")
            else:
                get_user_model().objects.create_user(username=username,password=password)
        return Response(status=status.HTTP_200_OK)










