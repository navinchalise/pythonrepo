#!/usr/bin/env python

import time

def application(environ, start_response):
    response_body = 'Hello this is python final test page after slave deployment time is now: %s\n' % time.time()

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
  
    start_response(status, response_headers)
    return [response_body.encode('utf-8')]
