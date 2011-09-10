<%inherit file="/base/base-index.mako"/>

<%def name="title()">Create New Client</%def>

<<<<<<< HEAD
<!--form method ="post" action="/clients/create">
    <center>
        Client Name:  <input type="text" name="client_name"/>
        <input type="submit" value="Submit" />
    <center>
</form-->

${c.new_client_form()|n}

<%def name="rightcontent()">
</%def>
=======
## Flash container
${h.flash.render("flash_container")|n}

<div class="contentleft" style="padding-top:30px">
    <center>
        <form method="POST" action="/clients/create" >
             Name: <input type="text" name="name"/><br/>
            <input type="submit" value="add"/>
        </form>
    </center>
</div>
>>>>>>> d81c52a691f6ce33cf473aa0559af6d8523ae322
