from rest_framework import viewsets,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class BahariYouthViewset(viewsets.ModelViewSet):
    '''
    Overriding the viewsets class to fit the BahariYouth project.
    Custom responses include:
        - status: 'success'
        - message: {'en': ..., 'ar': ...}
        - data: actual result data
    '''

    def get_success_message(self, action):
        messages = {
            'create': {'en': f'{self.basename} created successfully', 'ar': f'بنجاح{self.basename} تم إنشاء'},
            'retrieve': {'en': f'{self.basename} retrieved successfully', 'ar': f'بنجاح{self.basename} تم جلب'},
            'list': {'en': f'{self.basename} retrieved successfully', 'ar': f'تم جلب {self.basename} بنجاح'},
            'update': {'en': f'{self.basename} updated successfully', 'ar': f'بنجاح{self.basename} تم تحديث'},
        }
        return messages.get(action, {'en': 'Success', 'ar': 'تمت العملية بنجاح'})

    @swagger_auto_schema(operation_summary="Create object", operation_description="Creates a new object in the database.")
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': self.get_success_message('create'),
            'data': response.data
        }, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(operation_summary="List all objects", operation_description="Returns a list of all objects.")
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': self.get_success_message('list'),
            'data': response.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Retrieve object", operation_description="Retrieves a single object by ID.")
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': self.get_success_message('retrieve'),
            'data': response.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update object", operation_description="Updates an object by ID.")
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': self.get_success_message('update'),
            'data': response.data
        }, status=status.HTTP_200_OK)