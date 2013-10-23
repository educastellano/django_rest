from django.views.generic.base import View
from django.utils import timezone
try:
    import simplejson as json
except ImportError:
    import json

class RestView(View):

    def __init__(self, *args, **kwargs):
        super(View, self).__init__()
        if hasattr(self, 'put'):
            self.original_put = self.put
            self.put = self.data_tweak
        if hasattr(self, 'delete'):
            self.original_delete = self.delete
            self.delete = self.data_tweak
        if hasattr(self, 'serializer_class') and self.serializer_class:
            self.serializer = self.serializer_class()

    def data_tweak(self, request, *args, **kwargs):
        method = self.request.method
        try:
            self.request.method = 'POST'
            self.request._load_post_and_files()
            self.request.method = method
        except AttributeError:
            self.request.META['REQUEST_METHOD'] = 'POST'
            self.request._load_post_and_files()
            self.request.META['REQUEST_METHOD'] = method
        setattr(self.request, method, self.request.POST)
        if method == 'PUT':
            return self.original_put(request, *args, **kwargs)
        elif method == 'DELETE':
            return self.original_delete(request, *args, **kwargs)

    def get_data(self, request):
        if request.method == 'GET':
            data = request.GET
        elif request.method == 'POST':
            data = request.POST or json.loads(request.body)
        elif request.method == 'PUT':
            data = request.PUT or json.loads(request.body)
        else:
            data = None
        return data

