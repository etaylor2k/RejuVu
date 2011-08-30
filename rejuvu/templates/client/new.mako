<%inherit file="/base/base-index.mako"/>

<%def name="title()">Create New Client</%def>

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