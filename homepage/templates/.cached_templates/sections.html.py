# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516761739.9725263
_enable_loop = True
_template_filename = 'C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/sections.html'
_template_uri = 'sections.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['maintainence', 'top_content', 'left_column', 'center_column', 'right_column', 'foot']


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
        def right_column():
            return render_right_column(context._locals(__M_locals))
        def foot():
            return render_foot(context._locals(__M_locals))
        def left_column():
            return render_left_column(context._locals(__M_locals))
        def maintainence():
            return render_maintainence(context._locals(__M_locals))
        def top_content():
            return render_top_content(context._locals(__M_locals))
        def center_column():
            return render_center_column(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'maintainence'):
            context['self'].maintainence(**pageargs)
        

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
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'foot'):
            context['self'].foot(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintainence(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def maintainence():
            return render_maintainence(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <div class = "maintainence-message">This website is currently under construction</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content():
            return render_top_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class = "row sectionTop-content">\r\n      <h2>Top Content</h2>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_column():
            return render_left_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class = "col-xs-2 sectionLeftColumn">\r\n      <h2>Left Column</h2>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_column():
            return render_center_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class = "col-xs-8 sectionCenterColumn">\r\n        <h2>Center Column</h2>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_column():
            return render_right_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class = "col-xs-2 sectionRightColumn">\r\n      <h2>Right Column</h2>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_foot(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def foot():
            return render_foot(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <footer class = "sectionFoot">\r\n    <p>Footer</p>\r\n  </footer>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/sections.html", "uri": "sections.html", "source_encoding": "utf-8", "line_map": {"28": 0, "45": 1, "50": 5, "55": 11, "60": 17, "65": 23, "70": 29, "75": 35, "81": 3, "87": 3, "93": 7, "99": 7, "105": 13, "111": 13, "117": 19, "123": 19, "129": 25, "135": 25, "141": 31, "147": 31, "153": 147}}
__M_END_METADATA
"""
