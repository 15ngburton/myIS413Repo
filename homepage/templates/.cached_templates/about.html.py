# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516729815.806978
_enable_loop = True
_template_filename = 'C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content']


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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h2>About Us</h2>\r\n        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam at mattis metus, in ultricies dolor. Nulla in efficitur enim. Sed lacinia vulputate ante, in auctor ipsum varius ut. Nunc at aliquet magna. Sed vel massa at dui vehicula rutrum et eget mi. Nunc pellentesque eros tellus, commodo feugiat eros gravida ac. Donec leo arcu, pharetra vitae tincidunt eu, egestas at lacus. Curabitur auctor pulvinar lacus at pellentesque. Etiam vel viverra ex. Integer suscipit sem sit amet lorem feugiat, id lacinia metus pellentesque. Donec aliquet magna a dui efficitur, vitae dapibus tortor fermentum. Etiam in arcu libero. In vitae pellentesque ante. Mauris ac massa at nisl semper imperdiet rutrum et lectus.</p>\r\n\r\n        <p>Nunc eu felis eget augue condimentum cursus. Cras id odio velit. Mauris a urna fermentum, sollicitudin ipsum nec, consequat odio. Quisque nec volutpat tortor. Duis mattis orci odio, vitae commodo dui sodales id. Ut a ligula eu lectus dignissim varius. Nullam sollicitudin felis ac nibh aliquam, vel tincidunt metus viverra. Nulla consequat nulla velit, eget pellentesque nunc lacinia ut. Vivamus sit amet magna ut dui placerat luctus. Mauris laoreet purus est, vel consequat tortor aliquam ac. Integer sodales arcu eget orci malesuada dignissim. Sed ultrices dignissim vestibulum. Proin vel interdum orci. Donec in sollicitudin dolor.</p>\r\n\r\n<p>Vestibulum ut facilisis felis. Suspendisse a ligula ultrices, dignissim risus ac, varius metus. Aenean pretium elit at sem pretium dictum. Mauris quam libero, rhoncus et ante sit amet, feugiat pretium ipsum. Sed eu augue sapien. Donec pellentesque placerat dictum. Aliquam cursus lorem nec faucibus lobortis. Maecenas convallis venenatis ullamcorper. Ut rutrum facilisis velit, at eleifend sapien maximus ut. Vivamus a purus ac ex iaculis commodo sed eu nisl. Sed a laoreet elit. Maecenas lacinia, nisl eget luctus hendrerit, ipsum risus suscipit nisi, a tempor lacus dolor eu felis. Phasellus laoreet ac nulla ut sagittis. Curabitur sed aliquet ex, sed sagittis urna.</p>\r\n\r\n<p>Sed suscipit neque id vulputate egestas. Vivamus placerat aliquet tortor vel malesuada. Cras cursus risus et diam efficitur, ut suscipit erat porttitor. Morbi elit justo, tincidunt at turpis id, venenatis vestibulum nunc. Integer convallis mi vitae interdum fringilla. Donec placerat lobortis orci eu ultricies. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris rutrum ante id sollicitudin fringilla. Donec varius justo et nisi imperdiet lacinia. Pellentesque pretium gravida tortor, eget ultrices leo auctor ut. Maecenas vehicula lectus et velit tristique porttitor. Nunc eu ante a ligula malesuada dignissim. Pellentesque lacus urna, posuere eu volutpat vitae, aliquam a lorem.</p>\r\n\r\n        <p>Integer mollis ornare odio, id eleifend leo sollicitudin in. Vestibulum non varius est, vel pharetra urna. Vivamus rutrum varius erat ac pellentesque. In accumsan mollis augue vel efficitur. Vivamus id diam in dui blandit consequat. In hac habitasse platea dictumst. Aenean laoreet accumsan nisi at rhoncus. Aliquam consectetur felis pharetra nisl accumsan, et gravida tortor porta. Duis et magna ut nisl commodo consequat. Nullam orci tellus, porttitor sed orci ac, luctus ornare nibh. Praesent ac mi sapien. Curabitur at felis rutrum, pellentesque mauris nec, aliquam ante.</p>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/15ngb/Desktop/Fomo/fomo/homepage/templates/about.html", "uri": "about.html", "source_encoding": "utf-8", "line_map": {"28": 0, "35": 1, "40": 16, "46": 3, "52": 3, "58": 52}}
__M_END_METADATA
"""
