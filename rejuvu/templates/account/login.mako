<%inherit file="/base/base-index.mako"/>

<html>
<head>
<%def name="title()">Login</%def>
<title> Member Login</title>
</head>

<body>

<div class="login">

<form action="/account/dologin" method="POST">
<table width="50%" border="0" cellspacing="5" cellpadding="0" align="center">
  <tr>
    <td>Username</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td colspan="2"><input type="text" name="login" value=""/></td>
  </tr>
  <tr>
    <td colspan="2" height="5px"></td>
  </tr>
  <tr>
    <td>Password</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td colspan="2"><input type="password" name="password" value ="" /></td>
  </tr>
  <tr>
    <td colspan="2" height="5px"></td>
  </tr>
  <tr>
    <td><input type="submit" value="Login" /></td>
    <td>&nbsp;</td>
  </tr>
</table>
</form></div>


</body>
</html>