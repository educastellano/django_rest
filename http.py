from django.http import HttpResponse
try:
    import simplejson as json
except ImportError:
    import json

def output(inp):
    if type(inp) != type(''):
        return json.dumps(inp)
    return inp

def created(message='Created'):
    return HttpResponse(output(message), status=201)

def conflict(message='Conflict'):
    return HttpResponse(output(message), status=409)

def not_implemented(message='Not Implemented'):
    return HttpResponse(output(message), status=501)

def moved(message='Unauthorized'):
    return HttpResponse(output(message), status=301)

def unauthorized(message='Unauthorized'):
    return HttpResponse(output(message), status=401)

def forbidden(message='Forbidden'):
    return HttpResponse(output(message), status=403)

def error(message=''):
    return HttpResponse(output(message), status=500)

def bad_request(message=''):
    return HttpResponse(output(message), status=400)

def not_found(message=''):
    return HttpResponse(output(message), status=404)

def teapot(message=''):
    return HttpResponse(output(message), status=418)

def no_content(message=''):
    return HttpResponse(output(message), status=204)

def ok(message='', content_type='application/json'):
    return HttpResponse(output(message), status=200, content_type=content_type)
