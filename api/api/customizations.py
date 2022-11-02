import json
from rest_framework import renderers
from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'pagination': {
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'pages': [page for page in self.page.paginator.page_range],
                'has_previous': self.page.has_previous(),
                'has_next': self.page.has_next(),
                'prev_page': self.page.previous_page_number() if self.page.has_previous() else None,
                'next_page': self.page.next_page_number() if self.page.has_next() else None,
                'results_found': self.page.paginator.count,
            },
            'total': self.page.paginator.count,
            'advocates': data
        })


class CustomRenderer(renderers.JSONRenderer):
    charset = "utf-8"

    def render(self, data, media_type=None, renderer_context=None):
        response = renderer_context['response']
        is_success = False

        if response.status_code // 100 == 2 or response.status_code // 100 == 3:
            is_success = True

        response.data.setdefault('is_success', is_success)
        response.data.setdefault('status_code', response.status_code)
        response.data.setdefault('error_message', None)
        response.data.setdefault('errors', [])
        return json.dumps(response.data)


