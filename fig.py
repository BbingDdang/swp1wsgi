import sys
from cgi import parse_qs,escape
import matplotlib as mpl
import json
mpl.use('Agg')
import matplotlib.pyplot as plt
sys.path.insert(0, '/usr/local/swp1/')
from template import html


def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]

    #a = escape(a)
    #b = escape(b)

    if '' not in [a, b]:
        a, b = int(a), int(b)
        x = a + b
        y = a * b
        x = str(x)
        y = str(y)
        x = bytes(x, 'utf-8')
        y = bytes(y, 'utf-8')
        response_body = html + b'sum : ' + x + b' multiply : ' + y
    else:
        response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
