from .models import RegisterationActivities,RegisterationEvents
from project.viewsets import BahariYouthViewset
from events.models import Event
from activities.models import Activities
from .serializers import EventRegistrationSerializers,ActivitiesRegistrationSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .utils import validate_user_data


class EventRegistrationViewSet(BahariYouthViewset):
    queryset = RegisterationEvents.objects.all()
    serializer_class = EventRegistrationSerializers
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        user = request.user
        event_id = request.data.get('event')

        # Handle ID upload
        id_number = request.data.get('id_number')
        id_front = request.FILES.get('id_front')
        id_back = request.FILES.get('id_back')

        validate_user_data(user, id_number, id_front, id_back)

        registration, created = RegisterationEvents.objects.get_or_create(event=event_id)
        if registration.user.filter(id=user.id).exists():
            return Response({
                'status': 'error',
                'message': {
                    'en': 'You have already registered for this event.',
                    'ar': 'لقد قمت بالتسجيل في هذه الفعالية مسبقًا.'
                }
            }, status=status.HTTP_400_BAD_REQUEST)
            
            
        evnet = get_object_or_404(Event,id=event_id)
        if registration.user.count() < evnet.quantity :
            registration.user.add(user)
        else:
            return Response({
            'status': 'success',
            'message': {
                'en': 'No Places Availble',
                'ar': 'لا يوجد مكان '
            },
        }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status': 'success',
            'message': {
                'en': 'Register-event created successfully',
                'ar': 'تم إنشاء التسجيل بنجاح'
            },
        }, status=status.HTTP_201_CREATED)
        
        

class ActivitiesRegistrationViewSet(BahariYouthViewset):
    queryset = RegisterationActivities.objects.all()
    serializer_class = ActivitiesRegistrationSerializers
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        user = request.user
        activity_id = request.data.get('activity')

        # Handle ID upload
        id_number = request.data.get('id_number')
        id_front = request.FILES.get('id_front')
        id_back = request.FILES.get('id_back')

        validate_user_data(user, id_number, id_front, id_back)
        registration, created = RegisterationActivities.objects.get_or_create(activities=activity_id)
        if registration.user.filter(id=user.id).exists():
            return Response({
                'status': 'error',
                'message': {
                    'en': 'You have already registered for this event.',
                    'ar': 'لقد قمت بالتسجيل في هذه الفعالية مسبقًا.'
                }
            }, status=status.HTTP_400_BAD_REQUEST)
            
            
        activity = get_object_or_404(Activities, id=activity_id)
        if registration.user.count() < activity.quantity :
            registration.user.add(user)
        else:
            return Response({
            'status': 'success',
            'message': {
                'en': 'No Places Availble',
                'ar': 'لا يوجد مكان '
            },
        }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status': 'success',
            'message': {
                'en': 'Register-event created successfully',
                'ar': 'تم إنشاء التسجيل بنجاح'
            },
        }, status=status.HTTP_201_CREATED)