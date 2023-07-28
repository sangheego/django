from django.urls import path
from .views import helloAPI, booksAPI,bookAPI

urlpatterns=[
    #/example/hello/ 요청이 오면 helloAPI 함수가 처리
    path("hello/",helloAPI),
    #/example/fbv/books 요청이 오면 booksAPI 함수가 처리
    path("fbv/books",booksAPI),
    #bid를 받아서 1개의 데이터를 찾아오는 것을 bookAPI 함수가 처리
    path("fbv/book/<int:bid>/",bookAPI)
]