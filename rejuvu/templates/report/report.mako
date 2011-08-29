<%inherit file="/base/base-index.mako"/>

<%def name="title()">Report</%def>

           	<center><div class="topbar"></div>
                <div class="title">REPORTS</div></center>
            	<div class="contentleft" style="padding-top:30px">
                	<div class="left" style="padding-top:10px; padding-left:0; padding-right:0; width:325px">
                    <table width="60%" height="216" border="0" cellpadding="0" cellspacing="0" align="center">
  <tr>
    <td bgcolor="#f2bf49" align="center"><strong>Client</strong></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" align="center">YTD</td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" align="center">MTD</td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" align="center">&nbsp;</td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" align="center">&nbsp;</td>
  </tr>
  <tr>
    <td bgcolor="#f2bf49" align="center"><strong>Transactions</strong></td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" align="center">Daily Transactions Report</td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" align="center">Last 7 Days</td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" align="center">&nbsp;</td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" align="center">&nbsp;</td>
  </tr>
  <tr>
    <td bgcolor="#999999" align="center"><strong>Debtor</strong></td>
  </tr>
</table>

                    <div style="margin-top:20px">
                    <div style="padding-bottom:5px;">Geospatial Analysis</div>
                    <img src="/images/pic1.jpg" width="314" height="153" /></div>
                    </div>
                </div>
                 <div class="contentright"><img src="/images/pic.jpg" align="right" /></div>
                <div class="contentright" style="padding-top:10px">
                	<div class="righttopreports"><img src="/images/report-builder.png" /></div>
                    <div class="rightmiddle" style="padding-top:20px">
                    <center><form>
                    <table width="100%" cellspacing="0">
  <tr>
    <td>Old Password</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td colspan="2"><input name="name" type="password" value="" size="32" /></td>
  </tr>
  <tr>
    <td colspan="2" height="3px"></td>
  </tr>
  <tr>
    <td>New Password</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td colspan="2"><input name="name" type="password" value="" size="32" /></td>
  </tr>
  <tr>
    <td colspan="2" height="3px"></td>
  </tr>
  <tr>
    <td colspan="2">Re-enter New Password</td>
  </tr>
  <tr>
    <td colspan="2"><input name="name" type="password" value="" size="32" /></td>
  </tr>
  <tr>
    <td colspan="2" height="14"></td>
  </tr>
  <tr>
    <td width="47%"><input name="submit2" type="submit" value="Submit Changes" /></td>
    <td>&nbsp;</td>
  </tr>
</table>
                    </form></center>
                    </div>
                    <div class="rightbottom"></div></div>
                <div class="clear"></div>
          	</div>
            <div class="nav"><a href="/"><img src="/images/user.jpg" alt="User" name="user" id="user" onmouseover="MM_swapImage('user','','/images/user-ovr.jpg',1)" onmouseout="MM_swapImgRestore()" border="0"/></a></div>
          <div class="nav"><a href="/clients/index"><img src="/images/client.jpg" alt="Client" name="client" id="client" onmouseover="MM_swapImage('client','','/images/client-ovr.jpg',1)" onmouseout="MM_swapImgRestore()" border="0" /></a></div>
            <div class="nav"><a href="/reports/index"><img src="/images/reports-ovr.jpg" alt="Reports" name="reports" id="reports" border="0" /></a></div>