from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

def ajax(request):
    return render(request, "ajax.html")

#Get 요청만 처리
@api_view(['GET'])
def helloAPI(request):
    return Response("HELLO REST API")

from .serializers import BookSerializer
from rest_framework import status
from .models import Book
@api_view(['POST','GET','PUT','DELETE'])
def booksAPI(request):
    if request.method == 'GET':
        books=Book.objects.all()
        serializer=BookSerializer(books, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print(request.data)
        serializer = BookSerializer(data=request.data)
        #유효성 검사
        if serializer.is_valid():
            serializer.save() #데이터 저장
            #성공했을 때 전송한 데이터를 다시 전송
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
    #실패했을 때 처리
    Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#기본키 가지고 데이터 1개 찾아오는데 없으면 404에러 발생
from rest_framework.generics import get_object_or_404
@api_view(['GET'])
def bookAPI(request,bid):
    #기본키 가지고 데이터 1개 가져오기
    book=get_object_or_404(Book,bid=bid)
    serializer=BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)