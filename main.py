from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    key = request.cookies.get('key')
    if key == None:
        return redirect('/admin/login')
    else:
        return 'Work in progress'

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

if __name__ == '__main__':
    app.run(debug=True)