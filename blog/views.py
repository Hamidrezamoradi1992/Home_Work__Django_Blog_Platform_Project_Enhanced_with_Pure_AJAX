from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from blog.models import Post, Author
from blog.serializer import PostSerializer, AuthorSerializer

# Create your views here.
'''Api View Author'''


@api_view(['GET'])
def Author_GET_all_view(request):
    if request.method == 'GET':
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Author_update_delete_detail_view(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(author)
    if request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = AuthorSerializer(author)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_author(request):
    print('jjjjjjjjjjjjjj')
    if request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status=status.HTTP_404_NOT_FOUND)


"""Api View Author END"""

"""Api View Post"""


@api_view(['GET'])
def pst_view(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PostSerializer(Post.objects.filter(author_id=pk), many=True)
        return Response([serializer.data, author.name, author.pk], status=status.HTTP_200_OK)


@api_view(['POST'])
def create_post(request, pk):
    print('hamid')
    try:
        print('hamid')
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            Post.objects.create(title=serializer.data['title'], description=serializer.data['description'],
                                author=Author.objects.get(pk=pk))
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def post_update_delete_detail_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)


"""Api View Post END"""


def index(request):
    return render(request, 'home.html', {})
