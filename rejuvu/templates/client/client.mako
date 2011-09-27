<%inherit file="/base/base-index.mako"/>

<%def name="title()">Client</%def>

            <center><div class="topbar"></div>
                <div class="title" style="width:125px;"><em>${c.user.name}</em></div></center>

            	<div class="contentleft" style="padding-top:30px">
                	<div class="left" style="padding-top:40px;"><img src="/images/pie-chart.png" width="212" height="219" />
                    <div style="margin-top:10px">Snapshot Statistics</div>
                    </div>
                </div>
                    <div class="contentright"><img src="/images/pic.jpg" align="right" /></div>
                <div class="contentright" style="padding-top:10px">
                	<div class="admintop">${c.user_level.name}<!--img src="/images/admin.png" /--></div>
                    <div class="adminmiddle">
                    <form>
                    <table width="100%" border="0" cellspacing="20" cellpadding="0">
  <tr>
    <td height="40">&nbsp;</td>
  </tr>
  ## Test for Super Users to create a client
  % if c.user_level.name == "Super User":
    <tr>
        <td align="center"><input name="Create Client" type="button" value="Create Client" onclick="document.location.href='/clients/new';" style="width:115px" /></td>
    </tr>

  % endif
  <tr>
    <td align="center"><input name="upload" type="button" value="Upload Data" style="width:115px" /></td>
  </tr>
  <tr>
    <td align="center"><input name="account" type="button" value="Accounts" onclick="document.location.href='/account/list';" style="width:115px" /></td>
  </tr>
  <tr>
    <td align="center"><input name="search" type="button" value="Search Accounts" style="width:115px" /></td>
  </tr>
</table>
                    </form>
                    </div>
                    <div class="adminbottom"></div>
                </div>
                <div class="clear"></div>
          	</div>
            <div class="nav"><a href="/"><img src="/images/user.jpg" alt="User" name="user" id="user" onmouseover="MM_swapImage('user','','/images/user-ovr.jpg',1)" onmouseout="MM_swapImgRestore()" border="0"/></a></div>
          <div class="nav"><a href="/clients/index"><img src="/images/client-ovr.jpg" alt="Client" name="client" id="client" border="0" /></a></div>
            <div class="nav"><a href="/reports/index"><img src="/images/reports.jpg" alt="Reports" name="reports" id="reports" onmouseover="MM_swapImage('reports','','/images/reports-ovr.jpg',1)" onmouseout="MM_swapImgRestore()" border="0" /></a></div>
            <div>
