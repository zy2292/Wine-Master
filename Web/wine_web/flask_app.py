<!DOCTYPE html>

<html lang="en" style="height: 100%">
    <head>
        <meta charset="utf-8">
        <title>flask_app.py : /home/WineMaster/mysite/flask_app.py : Editor : WineMaster : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="flask_app.py : /home/WineMaster/mysite/flask_app.py : Editor : WineMaster : PythonAnywhere">
        <meta name="author" content="PythonAnywhere LLP">
        <meta name="google-site-verification" content="O4UxDrfcHjC44jybs2vajc1GgRkTKCTRgVzeV6I9V14" />


        <!-- Le styles -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i" />

        <link rel="stylesheet" href="/static/CACHE/css/58620f2cf098.css" type="text/css" media="screen" />
        <link rel="stylesheet" href="/static/CACHE/css/0acd5cb7a143.css" type="text/css" /><link rel="stylesheet" href="/static/CACHE/css/6eec124e142e.css" type="text/css" media="screen" />

        <!-- Le javascript -->
        <script type="text/javascript">
            var Anywhere = {};
            Anywhere.urls = {};
            Anywhere.csrfToken = "Kln2Piw3wLo33vrpxrOZlvxWkq9AwLTe";
        </script>
        <script type="text/javascript" src="/static/CACHE/js/8dc09e227063.js"></script>
        

        <script type="text/javascript" src="/static/CACHE/js/400872570903.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          save: "/user/WineMaster/files/home/WineMaster/mysite/flask_app.py",
          check_hash: "/user/WineMaster/files/home/WineMaster/mysite/flask_app.py",
          run: "/user/WineMaster/files/home/WineMaster/mysite/flask_app.py" + "?run",
          update_editor_mode_preference: "/user/WineMaster/account/update_editor_mode_preference",
        });
        var filename = "/home/WineMaster/mysite/flask_app.py";
        var hash = "2587fee6eaf526e56d453b8a3442122b";
        var interpreter = "python3.6";

        
            Anywhere.Editor.InitialiseAce(ace, Anywhere.urls, filename, hash, interpreter);
            $("#id_keybinding_mode_select").val("normal");
            $("#id_keybinding_mode_select").trigger("change");
        
        var consoleVisible = true;
        Anywhere.Editor.splitPanes(consoleVisible);

        Anywhere.WebAppControl.initialize();
        Anywhere2.initializeFileSharingOptions(
          $('#id_file_sharing_options')[0],
          {
            url: "/api/v0/user/WineMaster/files/sharing/",
            csrfToken: "Kln2Piw3wLo33vrpxrOZlvxWkq9AwLTe",
            path: "/home/WineMaster/mysite/flask_app.py"
          }
        );

      });
    </script>

        

        <!-- Le fav and touch icons -->
        <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
        <link rel="apple-touch-icon" sizes="72x72" href="images/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="114x114" href="images/apple-touch-icon-114x114.png">



    </head>

     <body style="height:100%;">
       <div style="min-height: 100%; position: relative;">
        
  




  <nav class="navbar navbar-default fullscreen-main-navbar">
    <div class="navbar-header">
      <a class="navbar-brand" href="/">
        <img id="id_logo" src="/static/anywhere/images/PA-logo-snake-only.svg" height="100%" />
      </a>
    </div>

    <div class="extra-nav-content">
      

  <div id="id_editor_toolbar">

    <div class="pull-left">
      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/WineMaster/files/">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/WineMaster/files/home">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/WineMaster/files/home/WineMaster">WineMaster</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/WineMaster/files/home/WineMaster/mysite">mysite</a><span class="breadcrumb_entry">/</span><wbr><span class="breadcrumb_entry breadcrumb_terminal">flask_app.py</span></span>

      <span>
        <span id="id_unsaved_changes_spacer">
          <span id="id_unsaved_changes" class="pa_hidden muted">(unsaved changes)</span>
        </span>
      </span>
    </div>

    <div id="id_editor_messages" class="pull-left">
      

    </div>

    <div class="pull-right">
      <div id="id_editor_buttons_right" class="form-inline">
        <span id="id_save_error" class="pa_hidden alert alert-danger">Error saving.</span>
        <img src="/static/anywhere/images/spinner-small.gif" class="pa_hidden" id="id_save_spinner" />
        
          <span id="id_keyboard_shortcuts"><a href="#">Keyboard shortcuts:</a></span>
          <select id="id_keybinding_mode_select" class="form-control input-sm">
            <option value="normal">Normal</option>
            <option value="vim">Vim</option>
          </select>
        
        <button id="id_display_sharing_options" class="btn btn-default" data-toggle="modal" data-target="#id_file_sharing_modal" title="Get a URL to share this file">
          <span class="glyphicon glyphicon-paperclip" aria-hidden="true"></span>
          Share
        </button>
        
          <button id="id_save" class="btn btn-success" title="Save (Ctrl + S)">
            <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
            Save
          </button>
          <button id="id_save_as" class="btn btn-default" title="Save As">Save as...</button>
        
        
          <button class="btn btn-info run_button" title="Save &amp; Run (Ctrl + R)">
            <span><code>&gt;&gt;&gt;</code></span>
            Run
          </button>
        

        
          
            <form class="reload_web_app" style="display: flex" method="POST" action="/user/WineMaster/webapps/WineMaster.pythonanywhere.com/reload">
              <button class="btn btn-default" type="submit" title="Reload WineMaster.pythonanywhere.com">
                <i class="glyphicon glyphicon-refresh"></i>
              </button>
              <img style="display: none;" class="spinner" src="/static/anywhere/images/spinner-small.gif" />
              <div style="display: none; clear: both;" class="alert alert-danger error_message generic_error">
                There was a problem. If this keeps happening, please <a href="" class="feedback_link">send us feedback</a>.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message slow_startup_error">
                Your webapp took a long time to reload. It probably reloaded, but we were unable to check it.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message virtualenv_error">
                There is a problem with your virtualenv setup. Look at the <b>virtualenv</b> section on the web app tab for details.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message cname_error">
                There is a problem with your DNS configuration. Take a look at the <b>DNS setup</b> section on the web app tab for details.
              </div>
            </form>
          
        
      </div>
    </div>

  </div>


    </div>

    <div class="dropdown fullscreen-hamburger fullscreen-mini-nav">
      <button type="button" class="navbar-toggle" data-toggle="dropdown"  role="button" aria-haspopup="true" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <ul class="dropdown-menu pull-right">
        
  
    <li class=""><a id="id_dashboard_link" href="/user/WineMaster/">Dashboard</a></li>
  
  <li class=""><a id="id_consoles_link" href="/user/WineMaster/consoles/">Consoles</a></li>
  <li class=""><a id="id_files_link" href="/user/WineMaster/files/home/WineMaster">Files</a></li>
  <li class=""><a id="id_web_app_link" href="/user/WineMaster/webapps/">Web</a></li>
  <li class=""><a id="id_tasks_link" href="/user/WineMaster/tasks_tab/">Tasks</a></li>
  <li class=""><a id="id_databases_link" href="/user/WineMaster/databases/">Databases</a></li>


        <li class=""><a href="" class="feedback_link">Send feedback</a></li>
<li class=""><a href="/forums/" class="forums_link">Forums</a></li>
<li class=""><a href="https://help.pythonanywhere.com/" class="help_link">Help</a></li>
<li class=""><a href="https://blog.pythonanywhere.com/" class="blog_link">Blog</a></li>

  
  <li class=""><a href="/user/WineMaster/account/" class="account_link">Account</a></li>
  <li class="">
    <form action="/logout/" method="POST">
      <input type='hidden' name='csrfmiddlewaretoken' value='Kln2Piw3wLo33vrpxrOZlvxWkq9AwLTe' />
      <button type="submit" class="btn-link logout_link">Log out</button>
    </form>
  </li>


      </ul>
    </div>

  </nav>



        
    


        
  <div>
    <div id="id_ide_split_panes">

      
        <div id="id_editor">from flask import Flask, flash, redirect, render_template, request, session, abort
import numpy as np
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import text_matching
import image_ocr
import winerd
from PIL import Image
from tempfile import mkdtemp
from werkzeug import secure_filename
from os.path import  join

app = Flask(__name__)
app.config[&quot;DEBUG&quot;] = True
SQLALCHEMY_DATABASE_URI = &quot;mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}&quot;.format(
    username=&quot;WineMaster&quot;,
    password=&quot;sqlpassword&quot;,
    hostname=&quot;WineMaster.mysql.pythonanywhere-services.com&quot;,
    databasename=&quot;WineMaster$default&quot;,
)
app.config[&quot;SQLALCHEMY_DATABASE_URI&quot;] = SQLALCHEMY_DATABASE_URI
app.config[&quot;SQLALCHEMY_POOL_RECYCLE&quot;] = 299
app.config[&quot;SQLALCHEMY_TRACK_MODIFICATIONS&quot;] = False

db = SQLAlchemy(app)

db_uri = SQLALCHEMY_DATABASE_URI
engine = create_engine(db_uri)
wine = pd.read_sql_query(&#39;SELECT * FROM wine_data&#39;, engine)
wineshow = pd.read_sql_query(&#39;SELECT * FROM wine_data&#39;, engine)
pd.set_option(&#39;display.max_colwidth&#39;, 10000)
def str_process(string):
    string=string.replace(&#39;\n&#39;,&#39;&#39;)
    string=string.replace(&#39; &#39;, &#39;&#39;)
    string=&#39;&#39;.join([*filter(str.isalnum, string)])
    string=&#39;&#39;.join(string)
    string=string.upper()
    return string
wine[&#39;designation&#39;]=wine[&#39;designation&#39;].apply(str).apply(str_process)
wine[&#39;province&#39;]=wine[&#39;province&#39;].apply(str).apply(str_process)
wine[&#39;region_1&#39;]=wine[&#39;region_1&#39;].apply(str).apply(str_process)
wine[&#39;variety&#39;]=wine[&#39;variety&#39;].apply(str).apply(str_process)
wine[&#39;winery&#39;]=wine[&#39;winery&#39;].apply(str).apply(str_process)
wine[&#39;year&#39;]=wine[&#39;year&#39;].fillna(0).apply(int).apply(str).apply(str_process)

@app.route(&#39;/&#39;)
def homepage():
    return render_template(&quot;index.html&quot;)

@app.route(&quot;/input&quot;)
def index():
    return render_template(&#39;input.html&#39;)


@app.route(&#39;/predict&#39;, methods=[&#39;POST&#39;])
def make_prediction():
	if request.method==&#39;POST&#39;:
	    file = request.form[&#39;text&#39;]
	#if not file: return render_template(&#39;input.html&#39;, label=&quot;No file&quot;)
	prediction = text_matching.matching(file,wine,wineshow)[[  &#39;province&#39;, &#39;designation&#39;, &#39;variety&#39;, &#39;winery&#39;, &#39;year&#39;, &#39;description&#39;, &#39;price&#39;]]
	return render_template(&#39;predict.html&#39;,table=prediction.to_html())

@app.route(&quot;/image&quot;)
def image():
    return render_template(&#39;image.html&#39;)

@app.route(&quot;/predictpic&quot;,methods=[ &#39;POST&#39;])
def predictpic():
    if request.method == &#39;POST&#39; :
        tempdir = mkdtemp()
        file = request.files[&#39;file&#39;]
        filename = secure_filename(file.filename)
        filepath = join(tempdir, filename)
        file.save(filepath)
        image=Image.open(filepath).convert(&quot;L&quot;)
        prediction = image_ocr.matching(image,wine,wineshow)
    return render_template(&#39;predict.html&#39;,table=prediction)

@app.route(&#39;/recommend&#39;, methods=[&#39;POST&#39;])
def make_recommendation():
	if request.method==&#39;POST&#39;:
	    index = request.form[&#39;text&#39;]
	#if not file: return render_template(&#39;input.html&#39;, label=&quot;No file&quot;)
	recommendation = winerd.get_recommendations(index, wine,wineshow)[[ &#39;province&#39;, &#39;designation&#39;, &#39;variety&#39;, &#39;winery&#39;, &#39;year&#39;, &#39;description&#39;, &#39;price&#39;]]
	#return recommendation.iloc[1,1]
	return render_template(&#39;recommend.html&#39;, ttable=recommendation.to_html())
	#return index






</div>
      

      <div id="id_ide_console">
        
          <iframe src="/user/WineMaster/consoles/8923735/frame/" id="id_console" name="console" class="soft_keyboard_sensitive">
          </iframe>
        
      </div>

    </div>

    <div id="id_go_to_line_dialog" class="pa_hidden">
      <p class="form-inline">Line number: <input id="id_go_to_line_dialog_input" /></p>
      <div class="dialog_buttons">
        <button class="btn btn-default" id="id_go_to_line_dialog_ok_button">Go</button>
        <button class="btn btn-default" id="id_go_to_line_dialog_close_button">Close</button>
      </div>
    </div>

    <div id="id_file_changed_on_disk" class="pa_hidden">
      <p>Are you sure you want to save it?  Alternatively, you could re-open it in a new tab to check differences</p>
      <div class="dialog_buttons">
        <button id="id_force_save" class="btn btn-danger">Force Save</button>
        <button id="id_cancel_save" class="btn btn-default">Cancel</button>
      </div>
    </div>

    <div id="id_save_as_dialog" class="pa_hidden">
      <form class="form-inline">
        <div class="form-group">
          <label for="id_save_as_path">Please enter a path:</label>
          <input id="id_save_as_path" class="form-control" style="width: 100%;" />
        </div>
        <img id="id_save_as_spinner" class="spinner pa_hidden" src="/static/anywhere/images/spinner-small.gif" />
        <p>
          <span id="id_save_as_error" class="error_message"></span>
        </p>
        <div class="dialog_buttons">
          <button id="id_save_as_ok" type="submit" class="btn btn-primary">Save</button>
          <button id="id_save_as_cancel" type="button" class="btn btn-default">Cancel</button>
        </div>
      </form>
    </div>

    <div class="modal fade" id="id_file_sharing_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">File Sharing options</h4>
          </div>
          <div class="modal-body">
            <div id="id_file_sharing_options"></div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

  </div>


        
      </div>

        


        <div id="id_feedback_dialog" title="Help us improve" style="display:none">
    <div id="id_feedback_dialog_blurb_big" class="dialog_blurb_big">
        It's always a pleasure to hear from you!
    </div>
    <div id="id_feedback_dialog_blurb_small">
        Ask us a question, or tell us what you love or hate about PythonAnywhere.<br/>
        We'll get back to you over email ASAP.
    </div>
    <textarea id="id_feedback_dialog_text" rows="6"></textarea>
    <input id="id_feedback_dialog_email_address" type="text" placeholder="Email address (optional - only necessary if you would like us to contact you)"/>
    
    <div id="id_feedback_dialog_error" class="pa_hidden">
        Sorry, there was an error connecting to the server. <br/>Please try again in a few moments...
    </div>
    <div class="dialog_buttons">
        <img id="id_feedback_dialog_spinner" src="/static/anywhere/images/spinner-small.gif" />
        <button class="btn btn-primary" id="id_feedback_dialog_ok_button">OK</button>
        <button class="btn btn-default" id="id_feedback_dialog_cancel_button">Cancel</button>
    </div>
</div>


        
            <script>
                (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                ga('create', 'UA-18014859-6', 'auto');
                ga('send', 'pageview');
            </script>
        

        
        <!-- preload font awesome fonts to avoid glitch when switching icons -->
        <div style="width: 0; height: 0; overflow: hidden"><i class="fa fa-square-o fa-3x" ></i></div>
    </body>
</html>
