# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1314145393.33776
_template_filename='/Users/endristaylor/Repo/RejuVu/rejuvu/templates/home.mako'
_template_uri='home.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['title']


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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n<div class="contentleft" style="padding-top:30px">\n                \t<div class="lefttop"><img src="/images/personal-info.png" /></div>\n                    <div class="leftmiddle">\n                    <center><form><table width="93%" cellspacing="0">\n  <tr>\n    <td width="50%">Name</td>\n    <td width="50%">&nbsp;</td>\n  </tr>\n  <tr>\n    <td colspan="2"><input name="name" type="text" value="')
        # SOURCE LINE 14
        __M_writer(escape(c.user.displayname))
        __M_writer(u'" size="40" /></td>\n  </tr>\n  <tr>\n    <td colspan="2" height="3px"></td>\n  </tr>\n  <tr>\n    <td>Username</td>\n    <td>User Level</td>\n  </tr>\n  <tr>\n    <td><input name="username" type="text" value="')
        # SOURCE LINE 24
        __M_writer(escape(c.user.username))
        __M_writer(u'" size="18" /></td>\n    <td><input name="userlevel" type="text" value="')
        # SOURCE LINE 25
        __M_writer(escape(c.user_level.name))
        __M_writer(u'" size="18" /></td>\n  </tr>\n  <tr>\n    <td colspan="2" height="3px"></td>\n  </tr>\n  <tr>\n    <td>Email</td>\n    <td>&nbsp;</td>\n  </tr>\n  <tr>\n    <td colspan="2"><input name="email" type="text" value="')
        # SOURCE LINE 35
        __M_writer(escape(c.user.email))
        __M_writer(u'" size="40" /></td>\n  </tr>\n  <tr>\n    <td colspan="2" height="3px"></td>\n  </tr>\n  <tr>\n    <td>Address</td>\n    <td>&nbsp;</td>\n  </tr>\n  <tr>\n    <td colspan="2"><input name="address" type="text" value="1234 Address Street" size="40" /></td>\n  </tr>\n  <tr>\n    <td colspan="2" height="3px"></td>\n  </tr>\n  <tr>\n    <td>City</td>\n    <td>&nbsp;</td>\n  </tr>\n  <tr>\n    <td colspan="2"><input name="city" type="text" value="City" size="40" /></td>\n  </tr>\n  <tr>\n    <td colspan="2" height="3px"></td>\n  </tr>\n  <tr>\n    <td>State</td>\n    <td>Zip Code</td>\n  </tr>\n  <tr>\n    <td><input name="state" type="text" value="State" size="18" /></td>\n    <td><input name="zip" type="text" value="77777" size="18" /></td>\n  </tr>\n  <tr>\n    <td colspan="2" height="14"></td>\n  </tr>\n  <tr>\n    <td><input name="submit" type="submit" value="Submit Changes" /></td>\n    <td>&nbsp;</td>\n  </tr>\n</table>\n                    </form></center>\n                    </div>\n                    <div class="leftbottom"></div>\n                </div>\n                <div class="contentright"><img src="/images/pic.jpg" align="right" /></div>\n                <div class="contentright" style="padding-top:10px">\n                \t<div class="righttop"><img src="/images/change-password.png" /></div>\n                    <div class="rightmiddle" style="padding-top:20px">\n                    <center><form>\n                    <table width="100%" cellspacing="0">\n  <tr>\n    <td>Old Password</td>\n    <td>&nbsp;</td>\n  </tr>\n  <tr>\n    <td colspan="2"><input name="name" type="password" value="" size="32" /></td>\n  </tr>\n  <tr>\n    <td colspan="2" height="3px"></td>\n  </tr>\n  <tr>\n    <td>New Password</td>\n    <td>&nbsp;</td>\n  </tr>\n  <tr>\n    <td colspan="2"><input name="name" type="password" value="" size="32" /></td>\n  </tr>\n  <tr>\n    <td colspan="2" height="3px"></td>\n  </tr>\n  <tr>\n    <td colspan="2">Re-enter New Password</td>\n  </tr>\n  <tr>\n    <td colspan="2"><input name="name" type="password" value="" size="32" /></td>\n  </tr>\n  <tr>\n    <td colspan="2" height="14"></td>\n  </tr>\n  <tr>\n    <td width="47%"><input name="submit2" type="submit" value="Submit Changes" /></td>\n    <td>&nbsp;</td>\n  </tr>\n</table>\n                    </form></center>\n                    </div>\n                    <div class="rightbottom"></div></div>\n                <div class="clear"></div>\n          \t</div>\n            <div class="nav"><a href="user.html"><img src="/images/user-ovr.jpg" alt="User" name="user" id="user" border="0" /></a></div>\n          <div class="nav"><a href="client.html"><img src="/images/client.jpg" alt="Client" name="client" id="client" onmouseover="MM_swapImage(\'client\',\'\',\'images/client-ovr.jpg\',1)" onmouseout="MM_swapImgRestore()" border="0" /></a></div>\n            <div class="nav"><a href="reports.html"><img src="/images/reports.jpg" alt="Reports" name="reports" id="reports" onmouseover="MM_swapImage(\'reports\',\'\',\'images/reports-ovr.jpg\',1)" onmouseout="MM_swapImgRestore()" border="0" /></a></div>\n            <div>')
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


