# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516764619.3094096
_enable_loop = True
_template_filename = 'C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['maintainence', 'top_bar', 'menu', 'top_content', 'left_column', 'center_column', 'content', 'right_column', 'foot', 'body_footer']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def left_column():
            return render_left_column(context._locals(__M_locals))
        def top_bar():
            return render_top_bar(context._locals(__M_locals))
        def maintainence():
            return render_maintainence(context._locals(__M_locals))
        def body_footer():
            return render_body_footer(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        def center_column():
            return render_center_column(context._locals(__M_locals))
        def foot():
            return render_foot(context._locals(__M_locals))
        def top_content():
            return render_top_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def right_column():
            return render_right_column(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.js"></script>\r\n\r\n')
        __M_writer('        <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css">\r\n\r\n')
        __M_writer('        <link rel="icon" href = "')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/img/fomo.jpg">\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n        <title>FOMO Instruments</title>\r\n\r\n    </head>\r\n    <body>\r\n\r\n\r\n')
        __M_writer('        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence'):
            context['self'].maintainence(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        __M_writer('        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_bar'):
            context['self'].top_bar(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        __M_writer('        <body class = "content">\r\n            <div class = "container">\r\n\r\n')
        __M_writer('                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\r\n\r\n                <div class = "row">\r\n\r\n')
        __M_writer('                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column'):
            context['self'].left_column(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_column'):
            context['self'].center_column(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_column'):
            context['self'].right_column(**pageargs)
        

        __M_writer('\r\n\r\n                </div>\r\n            </div>\r\n          </body>\r\n\r\n\r\n')
        __M_writer('   ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'foot'):
            context['self'].foot(**pageargs)
        

        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintainence(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence():
            return render_maintainence(context)
        __M_writer = context.writer()
        __M_writer('\r\n          <div class = "maintainence-message">This website is currently under construction</div>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_bar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_bar():
            return render_top_bar(context)
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n          <header class = \'top-bar\'>\r\n              <a href = \'/index/\'><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/img/fomo.jpg" alt="Logo" class = "logo"></a>\r\n             <nav class="navbar navbar-toggleable-md navbar-light bg-faded">\r\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n              </nav>\r\n              <div class="dropdown">\r\n                <button class="btn btn-primary dropdown-toggle account-button" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">\r\n                  Account\r\n                  <span class="caret"></span>\r\n                </button>\r\n                <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">\r\n                  <li><a href="#">My Account</a></li>\r\n                  <li><a href="#">Settings</a></li>\r\n                  <li role="separator" class="divider"></li>\r\n                  <li><a href="#">Log Out</a></li>\r\n                </ul>\r\n              </div>\r\n          </header>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n                  ')
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
        __M_writer('\r\n                        <div class = "col-xs-2 rightColumn">\r\n                        </div>\r\n\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_foot(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def foot():
            return render_foot(context)
        def body_footer():
            return render_body_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n     <footer>\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_footer'):
            context['self'].body_footer(**pageargs)
        

        __M_writer('\r\n      </footer>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_footer():
            return render_body_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n             ')
        __M_writer('\r\n              &copy Copyright ')
        __M_writer(str( datetime.now().year ))
        __M_writer('. All rights reserved.\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 101, "19": 0, "46": 2, "47": 8, "48": 11, "49": 11, "50": 11, "51": 14, "52": 14, "53": 14, "54": 17, "55": 17, "56": 17, "57": 20, "58": 21, "59": 21, "60": 30, "65": 32, "66": 36, "71": 56, "72": 60, "73": 64, "78": 67, "79": 72, "84": 75, "85": 78, "90": 83, "91": 86, "96": 90, "97": 98, "102": 105, "108": 30, "114": 30, "120": 36, "129": 36, "130": 38, "131": 38, "136": 41, "142": 40, "148": 40, "154": 64, "160": 64, "166": 72, "172": 72, "178": 78, "186": 78, "191": 81, "197": 80, "203": 80, "209": 86, "215": 86, "221": 98, "229": 98, "234": 103, "240": 100, "246": 100, "247": 101, "248": 102, "249": 102, "255": 249}}
__M_END_METADATA
"""
