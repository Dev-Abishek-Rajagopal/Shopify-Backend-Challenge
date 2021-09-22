from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authtoken.models import (Token)
from django.conf.urls.static import static
from django.db.models import Q

import os
import json
from collections import Counter

import webcolors

import logging
from .models import RepUser, ImgRep, ImgCart
from django.conf import settings

from PIL import Image

from .serializers import RepUserSerializer, ImgRepSerializer, ImgCartSerializer


logger = logging.getLogger("rep.request")

class RepUserVeiwSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]'

    queryset = RepUser.objects.all()
    serializer_class = RepUserSerializer

    def list_RepUser(self, request):
        try:
            book_list = RepUser.objects.all()
            serializer = RepUserSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def create_RepUser(self, request):
        try:
            serializer = RepUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                list = RepUser.objects.get(username=serializer.data["username"])
                datas = request.data.copy()
                datas["user"] = list.id
                try:
                    Token.objects.create(user=list)
                except Exception as e:
                    logger.info("Error")
                    logger.info(str(e))
                    return Response(str(e), status=404)
                return Response(serializer.data, status=200)

            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def get_RepUser(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = RepUser.objects.get(id=pk)
            serializer = RepUserSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)


    def delete_RepUser(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = RepUser.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book removed from Wishlist."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def update_RepUser(self, request, *args, **kwargs):
        try:
            serializer = RepUserSerializer(data=request.data)
            pk = self.kwargs['pk']
            item = RepUser.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = RepUser.objects.get(id=pk)
                serializer = RepUserSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)


class ImgRepVeiwSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    queryset = ImgRep.objects.all()
    serializer_class = ImgRepSerializer

    def list_ImgRep(self, request):
        try:
            book_list = ImgRep.objects.all()
            serializer = ImgRepSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def create_ImgRep(self, request):
        try:
            serializer = ImgRepSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                imgp = ImgRep.objects.get(id=serializer.data["id"])
                logger.info(imgp.img.path)
                im = Image.open(imgp.img.path)
                im = im.copy()
                im.thumbnail((150, 150))
                print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
                color_array = []
                for pixel in im.getdata():
                    print(pixel)
                    logger.info(pixel)
                    try:
                        color_array.append(webcolors.rgb_to_name(pixel))
                    except:
                        a = 10
                result = [item for items, c in Counter(color_array).most_common()
                              for item in [items] * c]
                result = list(dict.fromkeys(result))
                print(result)
                imgp.color_palette=''.join(str(e)+"," for e in result)
                imgp.save()
                return Response(serializer.data, status=200)

            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def get_ImgRep(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = ImgRep.objects.get(id=pk)
            serializer = ImgRepSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)


    def delete_ImgRep(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = ImgRep.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book removed from Wishlist."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def search_ImgRep(self, request, *args, **kwargs):
        try:
            search_query = self.kwargs['search']
            search_user = self.kwargs['user']
            dbi = ImgRep.objects.filter(Q(name=search_query) & Q(scope="PUBLIC") | Q(name=search_query) & Q(scope="PUBLIC") & Q(user=int(search_user)))
            serializer = ImgRepSerializer(dbi, many=True)
            return Response(serializer.data, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def update_ImgRep(self, request, *args, **kwargs):
        try:
            serializer = ImgRepSerializer(data=request.data)
            pk = self.kwargs['pk']
            item = ImgRep.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = ImgRep.objects.get(id=pk)
                serializer = ImgRepSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

@api_view(['GET'])
@authentication_classes((TokenAuthentication, ))
# @permission_classes((AllowAny, ))
def search_ImgRep(request):
    try:
        pk = request.query_params.get('pk')
        search_query = request.query_params.get('search')
        search_user = request.query_params.get('user')
        print(search_query)
        print(search_user)
        dbi = ImgRep.objects.filter(Q(name=search_query) & Q(scope="PUBLIC") |
                                    Q(name=search_query) & Q(scope="PRIVATE") &Q(scope=search_user) |
                                    Q(color_palette__icontains=search_query) & Q(scope="PUBLIC") |
                                    Q(color_palette__icontains=search_query) & Q(scope="PRIVATE") & Q(scope=search_user)
                                    )
        print(dbi)
        serializer = ImgRepSerializer(dbi, many=True)
        return Response(serializer.data, status=200)

    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)


class ImgCartVeiwSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]'

    queryset = ImgCart.objects.all()
    serializer_class = ImgCartSerializer

    def list_ImgCart(self, request):
        try:
            book_list = ImgCart.objects.all()
            serializer = ImgCartSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def create_ImgCart(self, request):
        try:
            serializer = ImgCartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=200)

            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def get_ImgCart(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = ImgCart.objects.get(id=pk)
            serializer = ImgCartSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)


    def delete_ImgCart(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = ImgCart.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book removed from Wishlist."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def update_ImgCart(self, request, *args, **kwargs):
        try:
            serializer = ImgCartSerializer(data=request.data)
            pk = self.kwargs['pk']
            item = ImgCart.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = ImgCart.objects.get(id=pk)
                serializer = ImgCartSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)
