## -*- coding: utf-8 -*-
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
  <title>RejuVu - ${self.title()}</title>
  <link href="/css/style.css" type="text/css" rel="stylesheet" />

  ${self.head()}
</head>

<body>
  <div id="header">
    <a href="${url('/')}"><div id="header_logo"></div></a>
    <div id="user_login">
    % if h.user():
        ${h.user().displayname or h.user().username}.
        <a href="/account/logout">Logout</a> 
    % else:
      <a href="/account/register">Register</a> |
      <a href="/account/login?came_from=${h.url.current()}">Login</a>
    % endif
    </div>  <!-- id="user_login" -->
  </div>  <!-- id="header" -->
  
  <div id="nav_strip">
    <ul>
      <li> <a href="/nav1">Nav Item 1</a> </li>
      <li> <a href="/nav2">Nav Item 2</a> </li>
    </ul>
  </div>  <!-- id="nav_strip" -->
  
  <div class="clearingdiv" />

  ${h.flash.render("flash_container")|n}

  <div id="maincontent">
  ${next.body()}
  </div>  <!-- id="maincontent" -->

  <div id="rightcontent">
    ${self.rightcontent()}
  </div>    <!-- id="rightcontent" -->

  <div id="footer">
    &copy; Copyright <a href="#">You</a> 2009.
  </div>  <!-- id="footer" -->
</body>

<%def name="head()"></%def>
<%def name="rightcontent()"></%def>
