

from .models import RepUser, ImgRep, ImgCart
from rest_framework import serializers
import logging


logger = logging.getLogger("rep.task")

class RepUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = RepUser;
        fields = ("id",'username','firstname', 'lastname', 'email',"password")

    def create(self, validated_data):
        try:
            return RepUser.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


    def update(self, instance, validated_data):
        try:
            instance.id = validated_data.get('id', instance.id);
            instance.first_name = validated_data.get('first_name', instance.first_name);
            instance.last_name = validated_data.get('last_name', instance.last_name);
            instance.password = validated_data.get('password', instance.password);
            #instance.email = validated_data.get('email', instance.email);
            # instance.username = validated_data.get('username', instance.username);
            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))

class ImgRepSerializer(serializers.ModelSerializer):


    class Meta:
        model = ImgRep;
        fields = ("id",'img','name', 'user', 'scope',"access","price","discount","color_palette")

    def create(self, validated_data):
        try:
            return ImgRep.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


    def update(self, instance, validated_data):
        try:
            instance.id = validated_data.get('id', instance.id);
            instance.first_name = validated_data.get('first_name', instance.first_name);
            instance.last_name = validated_data.get('last_name', instance.last_name);
            instance.password = validated_data.get('password', instance.password);
            #instance.email = validated_data.get('email', instance.email);
            # instance.username = validated_data.get('username', instance.username);
            instance.save()
            return instance

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


class ImgCartSerializer(serializers.ModelSerializer):


    class Meta:
        model = ImgCart;
        fields = ("id",'user','img', 'quantity')

    def create(self, validated_data):
        try:
            return ImgCart.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


    def update(self, instance, validated_data):
        try:
            instance.id = validated_data.get('id', instance.id);
            instance.first_name = validated_data.get('first_name', instance.first_name);
            instance.last_name = validated_data.get('last_name', instance.last_name);
            instance.password = validated_data.get('password', instance.password);
            #instance.email = validated_data.get('email', instance.email);
            # instance.username = validated_data.get('username', instance.username);
            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))