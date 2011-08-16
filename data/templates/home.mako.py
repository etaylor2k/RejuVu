# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1313453921.2479711
_template_filename='/Users/endristaylor/Repo/RejuVu/rejuvu/templates/home.mako'
_template_uri='/home.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['rightcontent', 'title']


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
    return runtime._inherit_from(context, u'/base/base-index.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n<h1>\n  Welcome to RejuVu.\n</h1>\n\n<div>\n  <p>\n    This <a href="http://pylonshq.com/">Pylons</a> application was created by <a href="http://bitbucket.org/chrismiles/blastoff/">BlastOff</a>.\n    It was configured with the following options:\n    <ul>\n      <li> Email Confirmation - users must confirm their email address before new accounts are activated. </li>\n    </ul>\n  </p>\n</div>\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_rightcontent(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n  This project has the following dependencies:\n  <ul>\n    <li> <a href="http://pylonshq.com/">Pylons &gt;= 0.9.7</a> </li>\n    <li> <a href="http://www.sqlalchemy.org/">SQLAlchemy &gt;= 0.5</a> </li>\n    <li> <a href="http://pypi.python.org/pypi/repoze.who">repoze.who</a> </li>\n    <li> <a href="http://pypi.python.org/pypi/repoze.who.plugins.sa">repoze.who.plugins.sa</a> </li>\n    <li> <a href="http://pypi.python.org/pypi/repoze.who-friendlyform">repoze.who-friendlyform</a> </li>\n    <li> <a href="http://toscawidgets.org/">ToscaWidgets</a> </li>\n    <li> <a href="http://toscawidgets.org/documentation/tw.forms/">tw.forms</a> </li>\n    <li> <a href="http://www.python-turbomail.org/wiki/3.0/BetaRelease2">TurboMail &gt;= 3.0b2</a> </li>\n    <li> <a href="http://python-rum.org/wiki/WebFlash">WebFlash</a> </li>\n  </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


