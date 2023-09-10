from flask import Flask, render_template, request, redirect, make_response


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post')
def post():
    key = request.cookies.get('key')
    if key == None:
        return redirect('/')
    else:
        return render_template('admin/post.html')
@app.route('/admin')
def admin():
    key = request.cookies.get('key')
    if key == None:
        return redirect('/admin/login')
    else:
        return redirect('/post')

@app.route('/admin/login', methods=['POST', 'GET'])
def admin_login():
    if request.method == 'GET':
        return render_template('admin/login.html')
    elif request.method == 'POST':
        if request.form.get('password') == 'cheese':
            res = make_response( redirect('/') )
            res.set_cookie('key', 'Have a cookie!', max_age=63072000)
            return res
        else:
            return redirect('/post')

if __name__ == '__main__':
    app.run(debug=True)