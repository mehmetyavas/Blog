from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Blog
from base.api.serializers import BlogSerializer



@api_view(['GET'])
def blog_list_create_api_view(request):

    if request.method == 'GET':
        blogs = Blog.objects.filter(aktif=True)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)




