# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516762768.6176772
_enable_loop = True
_template_filename = 'C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['menu']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def menu():
            return render_menu(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <ul class="navbar-nav">\r\n\r\n       <li class="nav-item ')
        __M_writer(str( 'active' if request.dmp_router_page == 'index' else '' ))
        __M_writer('">\r\n       <a class="nav-link " href="/index/">Home<span class="sr-only">(current)</span></a>\r\n       </li>\r\n       \r\n       <li class="nav-item ')
        __M_writer(str( 'active' if request.dmp_router_page == 'about' else '' ))
        __M_writer('">\r\n       <a class="nav-link " href="/about/">About</a>\r\n       </li>\r\n\r\n       <li class="nav-item ')
        __M_writer(str( 'active' if request.dmp_router_page == 'contact' else '' ))
        __M_writer('">\r\n       <a class="nav-link" href="/contact/">Contact</a>\r\n       </li>\r\n\r\n       <li class="nav-item ')
        __M_writer(str( 'active' if request.dmp_router_page == 'faq' else '' ))
        __M_writer('">\r\n       <a class="nav-link disabled" href="/faq/">FAQ</a>\r\n       </li>\r\n\r\n       <li class="nav-item ')
        __M_writer(str( 'active' if request.dmp_router_page == 'terms' else '' ))
        __M_writer('">\r\n       <a class="nav-link disabled" href="/terms/">Terms</a>\r\n       </li>\r\n\r\n       <li class="nav-item ')
        __M_writer(str( 'active' if request.dmp_router_page == 'sections' else '' ))
        __M_writer('">\r\n       <a class="nav-link disabled" href="/sections/">Sections</a>\r\n       </li>\r\n\r\n    </ul>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "41": 31, "47": 3, "54": 3, "55": 6, "56": 6, "57": 10, "58": 10, "59": 14, "60": 14, "61": 18, "62": 18, "63": 22, "64": 22, "65": 26, "66": 26, "72": 66}}
__M_END_METADATA
"""
