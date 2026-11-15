from django.shortcuts import render
from reservation.models import Booking
from reservation.serializers import BookingSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions

from datetime import datetime,timedelta,time

from turf_management.models import Turf

 
# Create your views here.

class BookingView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request):
        form_data=request.data

        serializer_insatnce=BookingSerializer(data=form_data)

        if serializer_insatnce.is_valid():
            cleaned_data=serializer_insatnce.validated_data
            match_date=cleaned_data.get("match_date")
            start_time=cleaned_data.get("start_time")
            duration=cleaned_data.get("duration")

            end_date_time= datetime.combine(match_date,start_time)+timedelta(hours=duration) # we only get datetime, not time. 
                                                                                             #so combine date and time (combine()) and add  duration to it (timedelta())
                                                                                             # and extract time from it(time()) 
            end_time= end_date_time.time()


            turf_id= cleaned_data.get("turf")
            turf_object=Turf.objects.get(id=turf_id)

            if start_time > time(18):
                amount= turf_object.night_price * duration
            else:
                amount= turf_object.day_price * duration

          # to prevent overlapping of bookings
            booking_object= Booking.objects.filter(
                turf= cleaned_data.get("turf"),
                match_date=cleaned_data.get("match_date"),
                start_time__lt=end_time,
                end_time__gt=start_time
                )

            if booking_object.exists():
                return Response({"message":"slot not available"})
            
            serializer_insatnce.save(end_time=end_time,amount=amount)
            return Response(serializer_insatnce.data)
        else:
            return Response(serializer_insatnce.errors)


class BookingRetreiveUpdateDeleteView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk=None):
        qs= Booking.objects.get(id=pk)
        serializer_instance=BookingSerializer(qs)
        return Response(serializer_instance.data)
    
    def put(self,request,pk=None):
        form_data=request.data
        form_object= Booking.objects.get(id=pk)
        serializer_instance=BookingSerializer(data=form_data,instance=form_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):
        Booking.objects.filter(id=pk).delete()
        return Response({"message":"deleted"})



#view for booking summary
class BookingSummaryView(APIView):

    def post(self,request):

        form_data= request.data
        turf= form_data.get("turf")
        match_date=datetime.strptime(form_data.get("match_date"),"%Y-%m-%d")
        bookings=Booking.objects.filter(turf=turf,match_date=match_date)
        serializer_instance=BookingSerializer(bookings,many=True)
        return Response(serializer_instance.data)






