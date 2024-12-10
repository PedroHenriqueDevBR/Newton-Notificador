from rest_framework.pagination import PageNumberPagination

class LimitePaginacao(PageNumberPagination):
    page_size = 5
