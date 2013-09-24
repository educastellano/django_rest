from django.http import HttpResponse
try:
    import simplejson as json
except ImportError:
    import json

class HttpWrapper(object):
    def output(self,inp):
        if type(inp) != type(''):
            return json.dumps(inp)
        return inp
    def created(self, message='Created'):
        return HttpResponse(self.output(message), status=201)
    def conflict(self, message='Conflict'):
        return HttpResponse(self.output(message), status=409)
    def not_implemented(self, message='Not Implemented'):
        return HttpResponse(self.output(message), status=501)
    def moved(self,message='Unauthorized'):
        return HttpResponse(self.output(message),status=301)
    def unauthorized(self,message='Unauthorized'):
        return HttpResponse(self.output(message),status=401)
    def forbidden(self,message='Forbidden'):
        return HttpResponse(self.output(message),status=403)
    def error(self,message=''):
        return HttpResponse(self.output(message),status=500)
    def bad_request(self,message=''):
        return HttpResponse(self.output(message),status=400)
    def not_found(self,message=''):
        return HttpResponse(self.output(message),status=404)
    def teapot(self, message=''):
        return HttpResponse(self.output(message), status=418)
    def no_content(self,message=''):
        return HttpResponse(self.output(message),status=204)
    def ok(self, message='', content_type='application/json'):
        return HttpResponse(self.output(message),status=200, content_type=content_type)
