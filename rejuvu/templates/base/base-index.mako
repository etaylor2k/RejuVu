<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>RejuVu - ${self.title()}</title>
<link href="/css/style.css" rel="stylesheet" type="text/css" />
<script type="text/javascript">
<!--
function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function MM_swapImgRestore() { //v3.0
  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}

function MM_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n); return x;
}

function MM_swapImage() { //v3.0
  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}
//-->
</script>
      ${self.head()}
</head>
<body onload="MM_preloadImages('/images/client-ovr.jpg','/images/reports-ovr.jpg')">
<div class="wrapper">
	<div class="top"></div>
	<div class="header">
    	<div class="headerlft"><img src="/images/logo.png" alt="logo" width="112" height="117" align="left" />
        	<div class="middle">
            <h1>ReJu Vu</h1>
            <font style="font-size:12px"><strong>Rejuvenate the way you do business.</strong></font>
            </div>
        </div>
        <div class="headerrt">
      <input name="search" type="text" /> <input name="search" type="submit" value="Search" /></div>
      <div class="undersearch"><a href="/">Home</a> | <a href="contact.html">Contact Us</a> | <a href="/account/logout">Log Out</a></div>
        <div class="clear"></div>
    </div>
		<div class="mainwrap">
          	<div class="main">
                ${next.body()}

	</div>

            <div class="clear"></div>
  </div>
    <div class="footer">&copy; 2011 ReJu Vu. All rights reserved.</div>
</div>
</body>
<%def name="head()"></%def>
