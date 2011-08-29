<%inherit file="/base/base-index.mako"/>

<%def name="title()">Home</%def>

<div class="contentleft" style="padding-top:30px">
                	<div class="lefttop"><img src="/images/personal-info.png" /></div>
                    <div class="leftmiddle">
                    <center><form action="/account/updateUserInfo" method="POST"><table width="93%" cellspacing="0">
  ${h.flash.render("flash_container")|n}
  <tr>
    <td width="50%">Name</td>
    <td width="50%">&nbsp;</td>
  </tr>
  <tr>
    <td colspan="2"><input name="name" type="text" value="${c.user.name}" size="40" /></td>
  </tr>
  <tr>
    <td colspan="2" height="3px"></td>
  </tr>
  <tr>
    <td>Username</td>
    <td>User Level</td>
  </tr>
  <tr>
    <td><input name="username" type="text" value="${c.user.username}" size="18" /></td>
    <td><input name="userlevel" type="text" value="${c.user_level.name}" size="18" /></td>
  </tr>
  <tr>
    <td colspan="2" height="3px"></td>
  </tr>
  <tr>
    <td>Email</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td colspan="2"><input name="email" type="text" value="${c.user.email}" size="40" /></td>
  </tr>
  <tr>
    <td colspan="2" height="3px"></td>
  </tr>
  <tr>
    <td>Address</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td colspan="2"><input name="address" type="text" value="${c.user.address}" size="40" /></td>
  </tr>
  <tr>
    <td colspan="2" height="3px"></td>
  </tr>
  <tr>
    <td>City</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td colspan="2"><input name="city" type="text" value="${c.user.city}" size="40" /></td>
  </tr>
  <tr>
    <td colspan="2" height="3px"></td>
  </tr>
  <tr>
    <td>State</td>
    <td>Zip Code</td>
  </tr>
  <tr>
    <td><input name="state" type="text" value="${c.user.state}" size="18" /></td>
    <td><input name="zip" type="text" value="${c.user.zip}" size="18" /></td>
  </tr>
  <tr>
    <td colspan="2" height="14"></td>
  </tr>
  <tr>
    <td><input name="submit" type="submit" value="Submit Changes" /></td>
    <td>&nbsp;</td>
  </tr>
</table>
                    </form></center>
                    </div>
                    <div class="leftbottom"></div>
                </div>
                <div class="contentright"><img src="/images/pic.jpg" align="right" /></div>
                <div class="contentright" style="padding-top:10px">
                	<div class="righttop"><img src="/images/change-password.png" /></div>
                    <div class="rightmiddle" style="padding-top:20px">
                    <center><form action="/account/updatePassword" method="POST">
                    <table width="100%" cellspacing="0">
  <tr>
    <td>Old Password</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td colspan="2"><input name="pwd_old" type="password" value="" size="32" /></td>
  </tr>
  <tr>
    <td colspan="2" height="3px"></td>
  </tr>
  <tr>
    <td>New Password</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td colspan="2"><input name="pwd_new" type="password" value="" size="32" /></td>
  </tr>
  <tr>
    <td colspan="2" height="3px"></td>
  </tr>
  <tr>
    <td colspan="2">Re-enter New Password</td>
  </tr>
  <tr>
    <td colspan="2"><input name="pwd_new_re" type="password" value="" size="32" /></td>
  </tr>
  <tr>
    <td colspan="2" height="14"></td>
  </tr>
  <tr>
    <td width="47%"><input type="submit" value="Submit Changes" /></td>
    <td>&nbsp;</td>
  </tr>
</table>
                    </form></center>
                    </div>
                    <div class="rightbottom"></div></div>
                <div class="clear"></div>
          	</div>
            <div class="nav"><a href="/"><img src="/images/user-ovr.jpg" alt="User" name="user" id="user" border="0" /></a></div>
          <div class="nav"><a href="/clients/index"><img src="/images/client.jpg" alt="Client" name="client" id="client" onmouseover="MM_swapImage('client','','/images/client-ovr.jpg',1)" onmouseout="MM_swapImgRestore()" border="0" /></a></div>
            <div class="nav"><a href="reports.html"><img src="/images/reports.jpg" alt="Reports" name="reports" id="reports" onmouseover="MM_swapImage('reports','','/images/reports-ovr.jpg',1)" onmouseout="MM_swapImgRestore()" border="0" /></a></div>
            <div>