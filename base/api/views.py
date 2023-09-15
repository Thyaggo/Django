from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.api.serializers import RoomSerializer
from base.models import Room

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request, pk=None):
    if pk:
        rooms = Room.objects.get(id=pk)
        serializer = RoomSerializer(rooms)
    else:
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)