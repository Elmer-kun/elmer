<%@ page contentType="text/html; charset=gb2312" %>
<%@ taglib uri="/struts-bean" prefix="bean" %>
<%@ taglib uri="/struts-html" prefix="html" %>
<%@ taglib uri="/struts-logic" prefix="logic" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
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
          <TD valign="top" width="9"></TD>
          <TD class="header_menu" align="middle">
		  	<A href="mer.do?method=browseIndexMer"><span class="whiteTitle"><bean:message key="menu.item1"/></span></A>		  </TD>
          <TD  width="2"></TD>
          <TD class="header_menu" align="middle">
		  	<A href="cart.do?method=browseCart"><span class="whiteTitle"><bean:message key="menu.item2"/></span></A>		  </TD>
          <TD  width="2"></TD>
          <TD class="header_menu" align="middle">
		  	<A href="order.do?method=browseOrder"><span class="whiteTitle"><bean:message key="menu.item3"/></span></A>		  </TD>
          <TD  width="2"></TD>
          <TD class="header_menu" align="middle">
		  	<A href="mem.do?method=browseWord"><span class="whiteTitle"><bean:message key="menu.item4"/></span></A>		  </TD>
          <TD  width="2"></TD>
          <TD class="header_menu" align="middle">
		  	<A href="mem.do?method=loadMember"><span class="whiteTitle"><bean:message key="menu.item5"/></span></A>		  </TD>
          <TD vAlign=top width=7></TD>
        </TR>
    </TABLE></td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td><table width="100%" border="0" cellpadding="0" cellspacing="0">
      <tr>
        <td height="60" style="color:green;font-weight:bold;">&nbsp;&nbsp; 订单详情：</td>
      </tr>
      
      <tr>
        <td align="center">
			<table width="94%" border="0" cellpadding="0" cellspacing="1" bgcolor="#FFFFFF">
			<logic:notPresent name="order">
              <tr align="center" bgcolor="#F7F3F7">
                <td colspan="2" height="26" class="redText"><bean:message key="order.notExist"/></td>
              </tr>				
			</logic:notPresent>
			<logic:present name="order">		  
              <tr  class="text">
                <td width="220" height="26" align="right"><bean:message key="order.no"/>：</td>
                <td>&nbsp;${order.orderNo}</td>
              </tr>
              <tr  class="text">
                <td width="220" height="26" align="right"><bean:message key="sel.money"/>：</td>
                <td>&nbsp;￥${order.cart.money}</td>
              </tr>
			  <fmt:formatDate value="${order.orderDate}" var="orderDateTime" type="both" pattern="yyyy年MM月dd日 hh:mm:ss"/>			
              <tr  class="text">
                <td width="220" height="26" align="right"><bean:message key="order.date"/>：</td>
                <td>&nbsp;${orderDateTime}</td>
              </tr>
              <tr  class="text">
                <td width="220" height="26" align="right"><bean:message key="member.level"/>：</td>
                <td>&nbsp;${order.member.memberlevel.levelName}</td>
              </tr>
              <tr  class="text">
                <td width="220" height="26" align="right"><bean:message key="order.favourable"/>：</td>
                <td>&nbsp;${order.member.memberlevel.favourable}<bean:message key="order.zhe"/></td>
              </tr>
              <tr  class="text">
                <td width="220" height="26" align="right"><bean:message key="order.consignee"/>：</td>
                <td>&nbsp;${order.member.memberName}</td>
              </tr>
              <tr  class="text">
                <td width="220" height="26" align="right"><bean:message key="order.phone"/>：</td>
                <td>&nbsp;${order.member.phone}</td>
              </tr>
              <tr  class="text">
                <td width="220" height="26" align="right"><bean:message key="order.zip"/>：</td>
                <td>&nbsp;${order.member.zip}</td>
              </tr>
              <tr  class="text">
                <td width="220" height="26" align="right"><bean:message key="order.address"/>：</td>
                <td>&nbsp;${order.member.address}</td>
              </tr>
              <tr  class="text">
                <td height="26" colspan="2" align="center" bgcolor="#FFFFFF" class="itemTitle"><bean:message key="order.list"/></td>
                </tr>
              <tr  class="text">
                <td height="26" colspan="2" align="center" bgcolor="#FFFFFF">
				 <table cellspacing="1" cellpadding="0" width="100%" border="0" bgcolor="#F7F3F7">
                  <tr height="26">
                    <td class="blackTitle" align="center"><bean:message key="mer.name"/></td>
                    <td class="blackTitle" align="center"><bean:message key="mer.price"/></td>
                    <td class="blackTitle" align="center"><bean:message key="sel.price"/></td>
                    <td class="blackTitle" align="center"><bean:message key="sel.number"/></td>
                    <td class="blackTitle" align="center"><bean:message key="sel.money"/></td>
                    </tr>
                    <logic:iterate id="row" name="result" type="java.util.Map">
                      <tr class="text" align="center" bgcolor="#FFFFFF">
                        <td>&nbsp;${row.merName}</td>
                        <td>￥${row.price}</td>
                        <td>￥${row.memprice}</td>
                        <td>${row.number}</td>
                        <td>￥${row.money}</td>
                      </tr>
                    </logic:iterate>
				    <tr height="10" bgcolor="#F7F3F7"><td colspan="5"></td></tr>					
                </table>
				</td>
              </tr>
              <tr bgcolor="#F7F3F7" class="text">
                <td height="40" colspan="2" align="center" bgcolor="#FFFFFF" valign="bottom">
				 <html:link page="/order.do?method=browseOrder">
				 	<span class="redText"><bean:message key="return.text"/></span>
				 </html:link>
				</td>
              </tr>
			</logic:present>						
            </table>
		  </td>
      </tr>
	  <tr height="20"><td colspan="5"></td></tr>      
      <tr align="right">
        <td height="20">&nbsp;</td>
      </tr>
    </table>
	</td>
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
	//构造商品分类下拉列表
	jsonrpc = new JSONRpcClient("JSON-RPC");
	var result = jsonrpc.ajax.getCategory();
	for (var i=0;i<result.length;i++){
		option =document.createElement("OPTION");
		option.value = result[i][0];
		option.text = result[i][1];
		document.all.category.options.add(option);
	}
	
	//搜索商品
	function QuickSearch(){
		var url = "mer.do?method=searchMer&cateid="+document.all.category.value;
		var key = document.all.qKey.value;
		if (key !=null && key!="商品关键字" && key.length>0)url = url+"&key="+key;
		window.location = url;
	}
</script>
</body>
</html>