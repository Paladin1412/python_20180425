#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auhtor: @merlinhuang
#


def application(environ, start_response):
    """csgi handler"""
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

