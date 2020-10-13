
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CatSerializer
from .model import Cat
from rest_framework.decorators import api_view


@api_view(['GET'])
def catList(request):
    cats = Cat.objects.all().order_by('-id')
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def catDetail(request, pk):
    cats = Cat.objects.get(id=pk)
    serializer = CatSerializer(cats, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def catCreate(request):
    serializer = CatSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def catUpdate(request, pk):
    cat = Cat.objects.get(id=pk)
    serializer = CatSerializer(instance=cat, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def catDelete(request, pk):
    cat = Cat.objects.get(id=pk)
    cat.delete()

    return Response('Item succsesfully delete!')
