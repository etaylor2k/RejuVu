<%inherit file="/base/base-index.mako"/>

<%def name="title()">Home</%def>

<h1>
  Welcome to RejuVu.
</h1>

<div>
  <p>
    This <a href="http://pylonshq.com/">Pylons</a> application was created by <a href="http://bitbucket.org/chrismiles/blastoff/">BlastOff</a>.
    It was configured with the following options:
    <ul>
      <li> Email Confirmation - users must confirm their email address before new accounts are activated. </li>
    </ul>
  </p>
</div>

<%def name="rightcontent()">
  This project has the following dependencies:
  <ul>
    <li> <a href="http://pylonshq.com/">Pylons &gt;= 0.9.7</a> </li>
    <li> <a href="http://www.sqlalchemy.org/">SQLAlchemy &gt;= 0.5</a> </li>
    <li> <a href="http://pypi.python.org/pypi/repoze.who">repoze.who</a> </li>
    <li> <a href="http://pypi.python.org/pypi/repoze.who.plugins.sa">repoze.who.plugins.sa</a> </li>
    <li> <a href="http://pypi.python.org/pypi/repoze.who-friendlyform">repoze.who-friendlyform</a> </li>
    <li> <a href="http://toscawidgets.org/">ToscaWidgets</a> </li>
    <li> <a href="http://toscawidgets.org/documentation/tw.forms/">tw.forms</a> </li>
    <li> <a href="http://www.python-turbomail.org/wiki/3.0/BetaRelease2">TurboMail &gt;= 3.0b2</a> </li>
    <li> <a href="http://python-rum.org/wiki/WebFlash">WebFlash</a> </li>
  </ul>
</%def>
