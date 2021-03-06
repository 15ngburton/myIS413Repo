# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1518119809.976665
_enable_loop = True
_template_filename = 'C:/Users/15ngb/desktop/fomo/fomo/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['top_content', 'left_column', 'center_column', 'right_column']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        def center_column():
            return render_center_column(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def left_column():
            return render_left_column(context._locals(__M_locals))
        def right_column():
            return render_right_column(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column'):
            context['self'].left_column(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_column'):
            context['self'].center_column(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_column'):
            context['self'].right_column(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def top_content():
            return render_top_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class = "top-content">\r\n    <div class = "row">\r\n      <div class = "col-md-6 col-xs-12">\r\n        <img src = "')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/img/instrument.png" alt = "Instrument" class = "hero">\r\n      </div>\r\n      <div class = "col-md-6 col-xs-12">\r\n        <br><br><br><br><br>\r\n        <h1 class = "hero-heading">Fomo Instruments</h1>\r\n        <hr>\r\n        <a href = \'/faq/\'><button class = "btn hero-btn">Rent now</button></a>\r\n        <h1> Logged in: ')
        __M_writer(str( request.user.is_authenticated ))
        __M_writer('\r\n      </div>\r\n    </div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_column():
            return render_left_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_column():
            return render_center_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_column():
            return render_right_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/15ngb/desktop/fomo/fomo/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "43": 1, "48": 18, "53": 21, "58": 24, "63": 27, "69": 3, "77": 3, "78": 7, "79": 7, "80": 14, "81": 14, "87": 20, "93": 20, "99": 23, "105": 23, "111": 26, "117": 26, "123": 117}}
__M_END_METADATA
"""
