from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializer import RoomSerializer, TopicSerializer, MessageSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/rooom',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serialier = RoomSerializer(rooms, many=True)
    return Response(serialier.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id = pk)
    serialier = RoomSerializer(room, many=False)
    return Response(serialier.data)