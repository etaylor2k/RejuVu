# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1314059836.1066799
_template_filename=u'/Users/endristaylor/Repo/RejuVu/rejuvu/templates/base/base-index.mako'
_template_uri=u'/base/base-index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<title>RejuVu - ')
        # SOURCE LINE 5
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n<link href="/css/style.css" rel="stylesheet" type="text/css" />\n<script type="text/javascript">\n<!--\nfunction MM_preloadImages() { //v3.0\n  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();\n    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)\n    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}\n}\n\nfunction MM_swapImgRestore() { //v3.0\n  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;\n}\n\nfunction MM_findObj(n, d) { //v4.01\n  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {\n    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}\n  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];\n  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);\n  if(!x && d.getElementById) x=d.getElementById(n); return x;\n}\n\nfunction MM_swapImage() { //v3.0\n  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)\n   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}\n}\n//-->\n</script>\n      ')
        # SOURCE LINE 33
        __M_writer(escape(self.head()))
        __M_writer(u'\n</head>\n<body onload="MM_preloadImages(\'/images/client-ovr.jpg\',\'/images/reports-ovr.jpg\')">\n<div class="wrapper">\n\t<div class="top"></div>\n\t<div class="header">\n    \t<div class="headerlft"><img src="/images/logo.png" alt="logo" width="112" height="117" align="left" />\n        \t<div class="middle">\n            <h1>ReJu Vu</h1>\n            <font style="font-size:12px"><strong>Rejuvenate the way you do business.</strong></font>\n            </div>\n        </div>\n        <div class="headerrt">\n      <input name="search" type="text" /> <input name="search" type="submit" value="Search" /></div>\n      <div class="undersearch"><a href="/">Home</a> | <a href="contact.html">Contact Us</a> | <a href="/account/logout">Log Out</a></div>\n        <div class="clear"></div>\n    </div>\n\t\t<div class="mainwrap">\n          \t<div class="main">\n                ')
        # SOURCE LINE 52
        __M_writer(escape(next.body()))
        __M_writer(u'\n\n\t</div>\n\n            <div class="clear"></div>\n  </div>\n    <div class="footer">&copy; 2011 ReJu Vu. All rights reserved.</div>\n</div>\n</body>\n')
        # SOURCE LINE 61
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


