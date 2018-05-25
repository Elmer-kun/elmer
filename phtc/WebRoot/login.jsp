<%@ page contentType="text/html; charset=gb2312" %>
<%@ taglib uri="/struts-bean" prefix="bean" %>
<%@ taglib uri="/struts-html" prefix="html" %>
<%@ taglib uri="/struts-logic" prefix="logic" %>
<html>
<head>
<title><bean:message key="website.title"/></title>
<link href="CSS/stylesheet.css" rel="stylesheet" type="text/css">
</head>
  
  <body> 
  <table width="780" border="0" align="center" cellpadding="0" cellspacing="0" >
  <tr><td width="200" height="60"></td>
  <td width="580"></td>
  </tr>
  <tr>
	<td width="200" height="80" background="images/log.jpg"></td>
	<td width="580"></td>
  </tr>
</table>
<table>
<tr><td height="30"></td></tr>
<tr><td width="250"></td>
<td width="450"><IMG src="images/login.jpg"></td>
  <td>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
      <tr>
        <td width="200" valign="top"><TABLE cellSpacing=0 cellPadding=0 width="100%" border=0>
            <TR>
              <TD><IMG src="images/Bule_43.gif"></TD>
            </TR>
            <tr>
            <TR>           
              <TD class="C_Item_bg">
              	<logic:present name="member">
				  <TABLE cellSpacing=0 cellPadding=0 width="100%" border=0>
                    <TR>
                     
                    </TR>
                    <TR>
                      <TD>
						  <TABLE cellSpacing=0 cellPadding=0 width="90%" align=center border=0>
	                           <TR height="10"><TD></TD></TR>						  
	                           <TR height="30" class="text">
	                             <TD><bean:message key="member.logined" arg0="${member.memberName}" arg1="${member.memberlevel.levelName}"/></TD>
	                           </TR>
	                           <TR height="30">
	                             <TD align="center">
	                   			   <a href="login.do?method=logout"><span class="blueText"><bean:message key="member.logout"/></span></a>          
							    </TD>
	                         </TR>
                      </TABLE> 
					</TR>
				  </TABLE>              	
              	</logic:present>
              	<logic:notPresent name="member">
	                <html:javascript formName="memLoginForm"/>
					<html:form action="/login.do?method=login" style="margin:0px;" onsubmit="return validateMemLoginForm(this);">
					  <TABLE cellSpacing=0 cellPadding=0 width="100%" border=0>
	                    <TR>
	                      <TD class="C_login_Title"><bean:message key="member.login.label"/></TD>
	                    </TR>
	                    <TR>
	                      <TD>
							  <TABLE cellSpacing=0 cellPadding=0 width="90%" align=center border=0>
		                           <TR height="30">
		                             <TD class="text"><bean:message key="member.login.name"/>£º
								 	<html:text property="loginName" size="10" styleClass="textBox"/>
								  </TD>
		                           </TR>
		                           <TR height="30">
		                             <TD class="text"><bean:message key="member.login.pwd"/>£º
									  <html:password property="loginPwd" size="10" styleClass="textBox"/>
								  </TD>
		                           </TR>
		                           <TR height="30">
		                             <TD class="UserRegster" align="right">
		                               <html:button property="btn" onclick="reg()"><bean:message key="member.reg.text"/></html:button>
								  	<html:submit><bean:message key="member.login.text"/></html:submit>
								  </TD>
		                         </TR>
	                      </TABLE> 
						</TR>
					  </TABLE>
					  <logic:messagesPresent>
					  	<script language="javascript">
					  		alert('<html:errors property="loginError"/>');
					  	</script>
					  </logic:messagesPresent>
					</html:form>              	
              	</logic:notPresent>
			  </TD>
            </TR>
            <TR>
              <TD><IMG src="images/Bule_58.gif"></TD>
            </TR>
          </TABLE>
          <script type="text/javascript">
	//»áÔ±×¢²á
	function reg(){
		window.location = "reg.jsp";
	}
	

</script>
  </body>
</html>
