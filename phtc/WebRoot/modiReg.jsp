<%@ page contentType="text/html; charset=gb2312" %>
<%@ taglib uri="/struts-bean" prefix="bean" %>
<%@ taglib uri="/struts-logic" prefix="logic" %>
<%@ taglib uri="/struts-html" prefix="html" %>
<jsp:useBean id="JSONRPCBridge" scope="session" class="com.metaparadigm.jsonrpc.JSONRPCBridge"/>
<jsp:useBean id="ajax" class="com.base.AjaxBean"></jsp:useBean>
<%
	JSONRPCBridge.registerObject("ajax",ajax);
%>
<html>
<head>
<title><bean:message key="website.title"/></title>
<link href="CSS/stylesheet.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="JS/jsonrpc.js"></script>
<script type="text/javascript" src="JS/checkform.js"></script>
</head>
<body class="body">
<table width="780" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
	<td height="150" background="images/biaoti.jpg"></td>
  </tr>
</table>
<table width="780" border="0" align="center" cellpadding="0" cellspacing="0" bgcolor="#FFFFFF" style="border:1px; border-style:solid; border-color:#888888">
    <tr>
	<td valign="top"><br></td><td  align="right"></td>
	
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td>
	<TABLE cellSpacing=0 cellPadding=0 width="100%" border=0 height="35" bgcolor="#00FF00">
        <TR align="center">
          <TD valign="top" width="9"><br></TD>
          <TD class="header_menu" align="middle">
		  	<A href="mer.do?method=browseIndexMer"><span class="whiteTitle"><bean:message key="menu.item1"/></span></A>
		  </TD>
          <TD  width="2"></TD>
          <TD class="header_menu" align="middle">
		  	<A href="cart.do?method=browseCart"><span class="whiteTitle"><bean:message key="menu.item2"/></span></A>
		  </TD>
          <TD  width="2"></TD>
          <TD class="header_menu" align="middle">
		  	<A href="order.do?method=browseOrder"><span class="whiteTitle"><bean:message key="menu.item3"/></span></A>
		  </TD>
          <TD  width="2"></TD>
          <TD class="header_menu" align="middle">
		  	<A href="mem.do?method=browseWord"><span class="whiteTitle"><bean:message key="menu.item4"/></span></A>
		  </TD>
          <TD width="2"></TD>
          <TD class="header_menu" align="middle">
		  	<A href="mem.do?method=loadMember"><span class="whiteTitle"><bean:message key="menu.item5"/></span></A>
		  </TD>
          <TD vAlign=top width=7><br></TD>
        </TR>
    </TABLE></td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td>
	<form action="mem.do?method=updateMember" style="margin:0px;" method="post" onSubmit="return CheckForm.Check(this,2)">             	
	<table width="100%" border="0" cellpadding="0" cellspacing="1" bgcolor="#FFFFFF">
      <tr>
        <td height="30" colspan="2">&nbsp;</td>
      </tr>
      <tr>
        <td height="40" colspan="2" style="color:green;font-weight:bold;">������Ϣ���޸ģ�<br></td>
      </tr>
      <tr >
        <td width="260" height="26" class="text" align="right"><bean:message key="member.level"/>
          ��</td>
        <td height="26" class="text">${member.memberlevel.levelName}</td>
      </tr>
      <tr >
        <td width="260" height="26" class="text" align="right"><bean:message key="member.realname"/>
          ��</td>
        <td height="26"><input type="text" name="memberName" size="30" class="textBox" value="${member.memberName}" require="true" dataType="Require" msg="��ʵ��������Ϊ��!"/></td>
      </tr>
      <tr >
        <td width="260" height="26" class="text" align="right"><bean:message key="member.login.name"/>
          ��</td>
        <td height="26"><input type="text" name="loginName" size="30" class="textBox" value="${member.loginName}" require="true" dataType="Require" msg="��¼������Ϊ��!"/></td>
      </tr>
      <tr >
        <td width="260" height="26" class="text" align="right"><bean:message key="member.login.pwd"/>
          ��</td>
        <td height="26"><input type="password" name="loginPwd" size="30" class="textBox"/></td>
      </tr>
      <tr >
        <td width="260" height="26" class="text" align="right"><bean:message key="member.login.repwd"/>
          ��</td>
        <td height="26"><input name="password" type="password" class="textBox" id="reLoginPwd" onBlur="checkPwd()" size="30"/></td>
      </tr>
      <tr >
        <td width="260" height="26" class="text" align="right"><bean:message key="member.phone"/>
          ��</td>
        <td height="26"><input type="text" name="phone" size="30" class="textBox" value="${member.phone}" require="true" dataType="Phone" msg="��ϵ�绰����ȷ!"/></td>
      </tr>
      <tr >
        <td width="260" height="26" class="text" align="right"><bean:message key="member.address"/>
          ��</td>
        <td height="26"><input type="text" name="address" size="30" class="textBox" value="${member.address}" require="true" dataType="Require" msg="��ϵ��ַ����Ϊ��!"/></td>
      </tr>
      <tr >
        <td width="260" height="26" class="text" align="right"><bean:message key="member.zip"/>
          ��</td>
        <td height="26"><input type="text" name="zip" size="30" class="textBox" value="${member.zip}" require="true" dataType="Zip" msg="�������벻��ȷ!"/></td>
      </tr>
      <tr >
        <td width="260" height="26" class="text" align="right"><bean:message key="member.email"/>
          ��</td>
        <td height="26"><input type="text" name="email" size="30" class="textBox" value="${member.email}" require="false" dataType="Email" msg="�������䲻��ȷ!"/></td>
      </tr>
      <tr>
        <td height="40" colspan="2" align="center">
			<input class="C_Input" type="submit" value="����"/>
	   </td>
      </tr>
    </table>
	</form> 
	</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td height="30">&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td height="30" bgcolor="#7CFC00" class="whiteText" align="center">
		<bean:message key="website.foot"/>	</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td height="20">&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
</table>
<script language="javascript">
	//������Ʒ���������б�
	jsonrpc = new JSONRpcClient("JSON-RPC");
	var result = jsonrpc.ajax.getCategory();
	for (var i=0;i<result.length;i++){
		option =document.createElement("OPTION");
		option.value = result[i][0];
		option.text = result[i][1];
		document.all.category.options.add(option);
	}
	
	//����˶�
	function checkPwd(){
		if (document.all.loginPwd.value != document.all.reLoginPwd.value){
			alert('�Բ���������������벻һ�£����������룡');
			document.all.loginPwd.value = "";
			document.all.reLoginPwd.value ="";
			document.all.loginPwd.focus();
		}
	}
	
	//������Ʒ
	function QuickSearch(){
		var url = "mer.do?method=searchMer&cateid="+document.all.category.value;
		var key = document.all.qKey.value;
		if (key !=null && key!="��Ʒ�ؼ���" && key.length>0)url = url+"&key="+key;
		window.location = url;
	}
</script>
<logic:messagesPresent property="modiMemberStatus">
	<script language="javascript">
		alert('<html:errors property="modiMemberStatus"/>');
	</script>
</logic:messagesPresent>	
</body>
</html>