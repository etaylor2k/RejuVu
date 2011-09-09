<%inherit file="/base/base-index.mako"/>

<%def name="title()">Create New Client</%def>

<!--form method ="post" action="/clients/create">
    <center>
        Client Name:  <input type="text" name="client_name"/>
        <input type="submit" value="Submit" />
    <center>
</form-->

${c.new_client_form()|n}

<%def name="rightcontent()">
</%def>