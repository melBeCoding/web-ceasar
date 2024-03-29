from flask import Flask, request
from caesar import rotate_char

app = Flask(__name__)
app.config['DEBUG'] = True
form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
  <form method='POST'>
     Rotate By:
     <input type="text" name="rot" value="0">
     <textarea name="text">{0}</textarea>
     </br>
     <input type='submit'/>
  </form>
    </body>
</html>"""
@app.route("/") 

def index():
    
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt(): 
    
 text = request.form["text"]
 rot = int(request.form["rot"])
 encrypted_text = ""

 for i in list(text):
        encrypted_text = encrypted_text + rotate_char(i,rot)

 return form.format(encrypted_text)
app.run() 
