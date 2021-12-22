from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters, generics
from .serializers import FilmDetailSerializer, FilmSerializer
from .models import Film
from django.shortcuts import render

# Create your views here.
class Showcase(APIView):
 
    def get(self,request):
        # TODO BALQIS tarik data
        film = Film.objects.all()

        # TODO SWAS sorting
        sort = request.GET.get("sort", None)
        if sort == "asc":
            film.order_by("year_released")
        elif sort == "dsc":
            film.order_by("-year_released")
        
        # serialize, kirim response
        serializers = FilmSerializer(film, many=True)
        return Response({
            "status" : 200,
            "message" : "Success",
            "data": serializers.data,
        })
            
    def post(self,request):
        films = Film.objects.all()

        # TODO IQBAL cek kalau title udah ada di model
        judul = request.data['title']
        for film in films:
            if judul == film.title:
                serializers = FilmSerializer(films, many=True)
                return Response({
                    "status" : 400,
                    "message" : f"Film dengan judul {judul} sudah ada di daftar",
                    "data": serializers.data,
                })

        # TODO IQBAL bikin objek film kalau belum ada
        new_film = Film.objects.create(
            title = request.data['title'],
            poster = request.data['poster'],
            trailer = request.data['trailer'],
            genre = request.data['genre'],
            year_released = request.data['year_released']
        )
        
        # serialize, kirim response
        serializers = FilmSerializer(film, many=True)
        return Response({
            "status" : 200,
            "message" : "berhasil menambahkan film",
            "data": serializers.data,
        })
             
        
class Search(APIView):
    def get(self, request, title):
        pass
        # TODO BALQIS tarik data yang difilter dari nama
        film = None

        # TODO SWAS sorting
        # TODO SWAS sorting
        sort = request.GET.get("sort", None)
        if sort == "asc":
            film.order_by("year_released")
        elif sort == "dsc":
            film.order_by("-year_released")
        
        # serialize, kirim response
        serializers = FilmSerializer(film, many=True)
        return Response({
            "status" : 200,
            "message" : "berhasil mendapatkan film",
            "data": serializers.data,
        })

class Detail(APIView):
    def get(self, request, id):
        #TODO SWAS detail film
        try:
            film = Film.objects.get(id=id)
            serializers = FilmDetailSerializer(film)
        except Film.DoesNotExist:
            return Response({
                "error" : "tidak ada film dengan id"
            })
        
        # serialize, return response
        return Response({
            "status" : 200,
            "message" : "berhasil mendapatkan film",
            "data" : serializers.data
        })
        

    def delete(self, request, id):
        pass
        # TODO FALEN cari id, hapus kalo ada, handle kalo gaada
        

class Like(APIView):
    def put(self, request, id, event):
        pass
        # TODO FALEN cari id, like/dislike, handle kalo gaada
        

        # serialize, send response
