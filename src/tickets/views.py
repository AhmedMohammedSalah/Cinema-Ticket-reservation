from django.shortcuts import render
from django.http.response import JsonResponse 
from rest_framework.response import Response
# Create your views here.
from .models import Guest,Movie,Reservation
from rest_framework.decorators import api_view
from .serializers import GuestSerializer ,MovieSerializer,Reservation
from rest_framework import status,filters
#1 without Rest Framework FBV 
def no_rest_no_model(request):
    guests=[
        {
            "id":1,
            "Name":"Ahmed ",
            "mobile ":54444,
        },
        {
            "id":2,
            "Name":"Mohamed ",
            "mobile ":17745753,
        }
    ]
    return JsonResponse(guests,safe=False)

#2 model data default without rest 
def no_rest_from_model(request):
    data_guests=Guest.objects.all()
    response = {
        'guests': list(data_guests.values('name','phone'))
    }
    return JsonResponse(response)

# List == GET
# Create == POST
# pk query == GET (id)
# Update == PUT
# Delete destroy == DELETE

#3 Function based views FBV 
# 3.1 GET POST 
@api_view(['GET','POST'])
def fbv_list (request):
    # GET
    if request.method=='GET':
        guests=Guest.objects.all()#query set
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)
    # POST 
    elif request.method=='POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
# 3.1 GET PUT,DELETE   
@api_view(['GET','PUT','DELETE'])
def fbv_pk (request,pk):
    try:
        guest=Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND )
    # GET
    if request.method=='GET':
        serializer=GuestSerializer(guest)
        return Response(serializer.data)
    # PUT
    elif request.method=='PUT':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method=='DELETE':
        
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# 4 CBV Class Based View
from rest_framework.views import APIView
# 4.1 GET POST 
class CBV_list(APIView):
    def get(self,request):
        guests=Guest.objects.all()#query set
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)
    def post(self,request):
            serializer=GuestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 4.2 GET PUT,DELETE   
from django.http import Http404
class CBV_pk(APIView):   
    def get_object (self ,pk):
        try:
             return Guest.objects.get(pk=pk)  
        except Guest.DoesNotExist:
            raise Http404
    
    def get(self ,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest)
        return Response(serializer.data)
    def put (self ,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request ,pk):
        guest=self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 

# 5-MIXins
from rest_framework import generics ,mixins
class Mixins_list(    mixins.ListModelMixin,    mixins.CreateModelMixin,    generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    
    def get(self ,request):
        return self.list(request)
    
    def post(self ,request):
        return self.create(request)
    
# Mixins 
class Mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    
    def get(self ,request,pk):
        return self.retrieve(request)
    
    def put(self ,request,pk):
        return self.update(request)
    def delete(self ,request,pk):
        return self.destroy(request)
'''
    Generics
'''
class Generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

#6.2 get put and delete 
class Generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


# view Sets 
from rest_framework import viewsets

class Viewsets_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    
    
    
    
    