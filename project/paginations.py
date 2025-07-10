from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class BaharyYouthPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            'status': 'success' if self.page.paginator.count != 0 else 'error',
            'message': {
                'en': 'Data retrieved successfully' if self.page.paginator.count != 0 else 'No Data to show',
                'ar': 'تم جلب البيانات بنجاح' if self.page.paginator.count != 0 else 'لا يوجد بيانات'
            },
            'count': self.page.paginator.count,
            'page_size': self.page.paginator.per_page,
            'page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data,
        })
