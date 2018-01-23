# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516737145.1220212
_enable_loop = True
_template_filename = 'C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['menu', 'top_content', 'left_column', 'center_column', 'content', 'right_column', 'body_footer']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left_column():
            return render_left_column(context._locals(__M_locals))
        def top_content():
            return render_top_content(context._locals(__M_locals))
        def body_footer():
            return render_body_footer(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def center_column():
            return render_center_column(context._locals(__M_locals))
        def right_column():
            return render_right_column(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>DMP</title>\r\n\r\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.js"></script>\r\n\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css">\r\n\r\n        <link rel="icon" href = "')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/img/fomo.jpg">\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/base.css">\r\n\r\n    </head>\r\n    <body>\r\n\r\n        <title>FOMO Instruments</title>\r\n\r\n        <div class = "maintainence-message">This website is currently under construction</div>\r\n\r\n            <header class = \'top-bar\'>\r\n                <img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/img/fomo.jpg" alt="Logo" class = "logo">\r\n               <nav class="navbar navbar-toggleable-md navbar-light bg-faded">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n                </nav>\r\n                <div class="dropdown">\r\n                  <button class="btn btn-primary dropdown-toggle account-button" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">\r\n                    Account\r\n                    <span class="caret"></span>\r\n                  </button>\r\n                  <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">\r\n                    <li><a href="#">My Account</a></li>\r\n                    <li><a href="#">Settings</a></li>\r\n                    <li role="separator" class="divider"></li>\r\n                    <li><a href="#">Log Out</a></li>\r\n                  </ul>\r\n                </div>\r\n            </header>\r\n\r\n\r\n        <body class = "content">\r\n            <div class = "container">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\r\n                <div class = "row">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column'):
            context['self'].left_column(**pageargs)
        

        __M_writer('\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_column'):
            context['self'].center_column(**pageargs)
        

        __M_writer('\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_column'):
            context['self'].right_column(**pageargs)
        

        __M_writer('\r\n                </div>\r\n            </div>\r\n\r\n        </body>\r\n\r\n    <footer>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_footer'):
            context['self'].body_footer(**pageargs)
        

        __M_writer('\r\n    </footer>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content():
            return render_top_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    <div class = "row top-content">\r\n                    </div>\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_column():
            return render_left_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n                        <div class = "col-xs-2 leftColumn">\r\n                        </div>\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_column():
            return render_center_column(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                        <div class = "col-xs-8 centerColumn">\r\n                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n                        </div>\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_column():
            return render_right_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n                        <div class = "col-xs-2 rightColumn">\r\n                        </div>\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_footer():
            return render_body_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n           ')
        __M_writer('\r\n            &copy Copyright ')
        __M_writer(str( datetime.now().year ))
        __M_writer('. All rights reserved.\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 79, "19": 0, "40": 2, "41": 10, "42": 11, "43": 11, "44": 13, "45": 13, "46": 15, "47": 15, "48": 18, "49": 19, "50": 19, "51": 21, "52": 21, "53": 31, "54": 31, "59": 34, "64": 56, "69": 61, "74": 67, "79": 71, "84": 81, "90": 33, "96": 33, "102": 53, "108": 53, "114": 58, "120": 58, "126": 62, "134": 62, "139": 65, "145": 64, "151": 64, "157": 68, "163": 68, "169": 78, "175": 78, "176": 79, "177": 80, "178": 80, "184": 178}}
__M_END_METADATA
"""
