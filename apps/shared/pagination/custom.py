from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):

    page_size = 20
    page_size_query_param = 'per_page'
    max_page_size = 50

    def get_paginated_response(self, data):
        return super().get_paginated_response({
            "success": True,
            "data": data,
            "meta": {
                "total_pages": self.page.paginator.num_pages,
                "current_page": self.page.number,
                "total_items": self.page.paginator.count
            }
        })