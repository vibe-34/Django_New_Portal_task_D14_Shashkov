from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter
from django.forms import DateInput
from .models import Category
from django.utils.translation import gettext as _, gettext_lazy


class RecordFilter(FilterSet):

    category = ModelChoiceFilter(field_name='category__title',
                                 queryset=Category.objects.all(),
                                 label=gettext_lazy('Категория'),
                                 empty_label=gettext_lazy('Категория не выбрана')
                                 )

    title = CharFilter(lookup_expr='contains',)

    date = DateFilter(field_name='data',
                      lookup_expr='gt',
                      label=gettext_lazy('Дата'),
                      widget=DateInput(attrs={'type': 'date'},)
                      )
