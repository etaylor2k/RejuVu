<%inherit file="/base/base-index.mako"/>

<html>
<head>
<%def name="title()">Forgot Password</%def>
<title>Forgot Password</title>

</head>
<body>

<p>If you have forgot the account password, you can <strong>reset password</strong>
    and a new password will be sent to your email address.</p>
      <form action="/account/doReset" method="post" name="actForm" id="actForm" >
        <table width="65%" border="0" cellpadding="4" cellspacing="4" class="loginform">
          <tr>
            <td colspan="2">&nbsp;</td>
          </tr>
          <tr>
            <td width="36%">Your Email</td>
            <td width="64%"><input name="user_email" type="text" class="required email" id="txtboxn" size="25"></td>
          </tr>
          <tr>
            <td colspan="2"> <div align="center">
                <p>
                  <input name="doReset" type="submit" id="doLogin3" value="Reset">
                </p>
              </div></td>
          </tr>
        </table>
        <div align="center"></div>
        <p align="center">&nbsp; </p>
      </form>

</body>
</html>