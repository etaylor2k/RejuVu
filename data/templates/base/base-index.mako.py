# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1313453921.279294
_template_filename=u'/Users/endristaylor/Repo/RejuVu/rejuvu/templates/base/base-index.mako'
_template_uri=u'/base/base-index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'rightcontent']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">\n<head>\n  <title>RejuVu - ')
        # SOURCE LINE 7
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n  <link href="/css/style.css" type="text/css" rel="stylesheet" />\n\n  ')
        # SOURCE LINE 10
        __M_writer(escape(self.head()))
        __M_writer(u'\n</head>\n\n<body>\n  <div id="header">\n    <a href="')
        # SOURCE LINE 15
        __M_writer(escape(url('/')))
        __M_writer(u'"><div id="header_logo"></div></a>\n    <div id="user_login">\n')
        # SOURCE LINE 17
        if h.user():
            # SOURCE LINE 18
            __M_writer(u'        ')
            __M_writer(escape(h.user().display_name or h.user().user_name))
            __M_writer(u'.\n        <a href="/account/logout">Logout</a> \n')
            # SOURCE LINE 20
        else:
            # SOURCE LINE 21
            __M_writer(u'      <a href="/account/register">Register</a> |\n      <a href="/account/login?came_from=')
            # SOURCE LINE 22
            __M_writer(escape(h.url.current()))
            __M_writer(u'">Login</a>\n')
            pass
        # SOURCE LINE 24
        __M_writer(u'    </div>  <!-- id="user_login" -->\n  </div>  <!-- id="header" -->\n  \n  <div id="nav_strip">\n    <ul>\n      <li> <a href="/nav1">Nav Item 1</a> </li>\n      <li> <a href="/nav2">Nav Item 2</a> </li>\n    </ul>\n  </div>  <!-- id="nav_strip" -->\n  \n  <div class="clearingdiv" />\n\n  ')
        # SOURCE LINE 36
        __M_writer(h.flash.render("flash_container"))
        __M_writer(u'\n\n  <div id="maincontent">\n  ')
        # SOURCE LINE 39
        __M_writer(escape(next.body()))
        __M_writer(u'\n  </div>  <!-- id="maincontent" -->\n\n  <div id="rightcontent">\n    ')
        # SOURCE LINE 43
        __M_writer(escape(self.rightcontent()))
        __M_writer(u'\n  </div>    <!-- id="rightcontent" -->\n\n  <div id="footer">\n    &copy; Copyright <a href="#">You</a> 2009.\n  </div>  <!-- id="footer" -->\n</body>\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n')
        # SOURCE LINE 52
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_rightcontent(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


