from django.shortcuts import render
from rest_framework import status
from project.viewsets import BahariYouthViewset
from .models import News
from .serializers import NewsSerializers
from rest_framework.permissions import IsAuthenticated
from project.paginations import BaharyYouthPagination



class NewsViewSets(BahariYouthViewset):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializers
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    pagination_class = BaharyYouthPagination
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            page_number = self.paginator.page.number  # current page number

        # Inject page number into each item
            data_with_page = [
                {**item, 'page': page_number} for item in serializer.data
            ]

            return self.get_paginated_response(data_with_page)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'status': 'success',
            'message': self.get_success_message('list'),
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
