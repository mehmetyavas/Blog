from rest_framework import  serializers
from base.models import Blog, Bloger
from datetime import datetime, date
from django.utils.timesince import timesince





class BlogSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    # yazar = serializers.StringRelatedField()
    # yazar = BloggerSerializer()


    class Meta:
        model = Blog
        fields = '__all__'
        # fields = [
        #     'yazar',
        #     'baslik',
        #     'metin'
        # ]

    def get_time_since_pub(self, object):

        now =datetime.now()
        pub_date = object.yayinlanma_tarihi
        if object.aktif == True:

            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return 'aktif değil'
    def validate_yayinlanma_tarihi(self,value):
        today = date.today()
        if value > today:
            raise serializers.ValidationError('yayınlanma tarihi ileri bir tarih olamaz')
        return value


class BlogerSerializer(serializers.ModelSerializer):

    # blog = BlogSerializer(many=True,read_only=True)#RELATED

    blog = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='blog-detay'
    )
    class Meta:
        model = Bloger
        fields = '__all__'












## Standart SERIALIZER

class BlogDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayinlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    guncelleme_tarihi = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        return Blog.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.aciklama = validated_data.get('aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayinlanma_tarihi = validated_data.get('yayinlanma_tarihi', instance.yayinlanma_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.save()
        return instance

    def validate(self, data):
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError(
                'baslık ve acıklama alanları aynı olamaz!'
            )
        return data

    def validate_baslik(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                f'baslık minimum 20 karakter olmalı!, siz {len(value)} karakter girdiniz'
            )
        return value






