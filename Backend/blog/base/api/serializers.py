from rest_framework import  serializers
from base.models import Blog

class BlogSerializer(serializers.Serializer):
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





