from flask import Flask, url_for

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/hello/<username>')
def hellouser(username):
    return 'hello ' + username +'!'

@app.route('/url_for')
def show_urlfor():
    return url_for("hellouser", username="Testuser")

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post" + str(post_id)

app.run(port=8000, debug=True)