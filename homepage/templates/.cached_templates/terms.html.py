# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516761616.0152216
_enable_loop = True
_template_filename = 'C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/terms.html'
_template_uri = 'terms.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h2>Terms</h2>\r\n        <p><b>Accelerando:</b> - a term in gereral use to show that music should be played at an increasing speed</p>\r\n        <p><b>Clef</b> - The five lines generally used in modern musical notation have no precise meaning without the addition at the left-hand side of a clef: a sign that specifies a particular note to be indicated by one of the lines, from which other notes may be gauged.</p>\r\n        <p><b>Cadence</b> - Usually consists of two chords that provide musical punctuation at the end of a phrase</p>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/terms.html", "uri": "terms.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 4, "47": 13, "53": 3, "59": 3, "65": 6, "71": 6, "77": 71}}
__M_END_METADATA
"""
