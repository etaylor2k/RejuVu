<%inherit file="/base/base-index.mako"/>

<%def name="title()">Register</%def>

<h3>Register for an account</h3>

<form method ='post' action ='/account/assign'>
<p>Client:  <select name="client">
	        % for a in c.clients:
		        <option value="${a.client_id}">${a.name}</option>
	        % endfor
	          </select></p>
<p>Reference Number: <input type='text' name ='refnum'></p>
</form>

<%def name="rightcontent()">
</%def>