<%inherit file="/base/base-index.mako"/>

<%def name="title()">Register</%def>

<h3>Register for an account</h3>

## This will add to the register form for Debtors
<table border="0" cellspacing="0" cellpadding="2">
<tr id="client_select" title="">
    <td class="labelcol">
        <label id="client_select.label" for="client_select" class="fieldlabel required">Client      </label>
    </td>
    <td class="fieldcol" >
        <select xmlns="http://www.w3.org/1999/xhtml" name="client">
        % for cli in c.clients:
            <option value="${cli.client_id}">${cli.name}</option>
        % endfor
        </select> (*)
    </td>
</tr>

<tr id="ref_num" title="">
    <td class="labelcol">
        <label id ="ref_num.label" for="ref_num" class fieldlabel required">Account Reference #</label>
    </td>
    <td class="fieldcol" >
        <input xmlns="http://www.w3.org/1999/xhtml" type="text" name="refnum" class="textfield required form-text" id="register_account_ref_num" value="" size="30" maxlength="255"/>
    (*)
    </td>
</tr>
</table>
${c.register_user_form()|n}

<%def name="rightcontent()">
</%def>
