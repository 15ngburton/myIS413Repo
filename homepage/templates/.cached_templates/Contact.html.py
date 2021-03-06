# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516762782.8179204
_enable_loop = True
_template_filename = 'C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['top_content', 'content']


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
        def content():
            return render_content(context._locals(__M_locals))
        csrf_input = context.get('csrf_input', UNDEFINED)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content():
            return render_top_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <h2>Contact Us</h2><br>\r\n\r\n    <form action="/contact/" method="POST">\r\n\r\n        ')
        __M_writer(str( csrf_input ))
        __M_writer('\r\n\r\n        First name: <input type="text" name="fname"><br><br>\r\n        Last name: <input type="text" name = "lname"><br><br>\r\n        Message: <br><textarea rows="4" cols="50" name = "message"></textarea><br><br>\r\n\r\n        <input type="submit" value = "Submit" class = "btn">\r\n\r\n    </form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/contact.html", "uri": "contact.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 4, "48": 22, "54": 3, "60": 3, "66": 6, "73": 6, "74": 12, "75": 12, "81": 75}}
__M_END_METADATA
"""
