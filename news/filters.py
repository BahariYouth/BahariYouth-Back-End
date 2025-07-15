import django_filters
from .models import News

class NewsFilter(django_filters.FilterSet):
    governorate = django_filters.NumberFilter(field_name='governorate__id', lookup_expr='exact')

    ordering = django_filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
        ),
        field_labels={
            'created_at': 'تاريخ الإنشاء',
        }
    )

    class Meta:
        model = News
        fields = ['governorate']
