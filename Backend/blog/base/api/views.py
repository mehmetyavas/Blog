from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Blog
from base.api.serializers import BlogSerializer

#CLASS VIEWS
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class BlogListCreateAPIView(APIView):

    def get(self, request):
        blog = Blog.objects.filter(aktif=True)
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailAPIView(APIView):

    def get_object(self, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return blog


    def get(self, request, pk):
        blog = self.get_object(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)


    def put(self, request, pk):
        blog = self.get_object(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        blog = self.get_object(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




## FUNCTION METHOD ##

# @api_view(['GET', 'POST'])
# def blog_list_create_api_view(request):
#
#     if request.method == 'GET':
#         blogs = Blog.objects.filter(aktif=True)
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def blog_detail_api_view(request,pk):
#     try:
#         blog= Blog.objects.get(pk=pk)
#     except Blog.DoesNotExist:
#         return Response(
#             {
#                 'errors:': {
#                     'code:': 404,
#                     'message:': f'boyle bir id ({pk}) ile ilgili blog yok'
#                 }
#             },
#             status = status.HTTP_404_NOT_FOUND
#         )
#     if request.method == 'GET':
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
#
#
#     elif request.method == 'PUT':
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
#     elif request.method == 'DELETE':
#         blog.delete()
#         return Response(
#             {
#                 'işlem:': {
#                     'code:': 204,
#                     'message:': f'{pk}) id numaralı blog silindi'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )





