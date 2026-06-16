from rest_framework.views import APIView, Response
from relacionamentos.models.pessoa import Pessoa
from ..serializers.pessoa import PessoaMinimalSerializer, PessoaCompleteSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response




class PessoaSimpleService(APIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaMinimalSerializer


    def get(self,request):
        pessoas = Pessoa.objects.all()
        contexto = {
            'request': request
        }

        serializer = PessoaMinimalSerializer(pessoas, many=True,context = contexto)

        return Response(serializer.data)
    
    def post(self,request):
        pessoa_dados = request.data
        contexto = {
            'request': request
        }

        serializer = PessoaMinimalSerializer(Pessoa,data=pessoa_dados,context=contexto)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

class PersonCompleteService(APIView):
    serializer_class = PessoaCompleteSerializer()
    queryset = Pessoa.objects.all()

    def get(self,request,pk):
        Pessoa = get_object_or_404(Pessoa,pk=pk)
        contexto = {
            'request': request
        }

        serializer = PessoaCompleteSerializer(Pessoa,context = contexto)
        
        return Response(serializer.data)
    
    def delete(self,request,pk):
        pessoa = get_object_or_404(Pessoa,pk=pk)
        pessoa.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,pk):
        pessoa = get_object_or_404(Pessoa,pk=pk)
        pessoa_dados = request.data
        contexto = {
            'request': request
        }

        serializer = PessoaCompleteSerializer(Pessoa,data=pessoa_dados,context=contexto)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)