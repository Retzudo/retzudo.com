import os
from flask import Flask, render_template, send_from_directory, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static/images'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )


@app.route('/browserconfig.xml')
def browserconfig():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'browserconfig.xml',
        mimetype='application/xml'
    )


@app.route('/apple-touch-icon.png')
@app.route('/apple-touch-icon-precomposed.png')
@app.route('/apple-touch-icon-57x57.png')
@app.route('/apple-touch-icon-60x60.png')
@app.route('/apple-touch-icon-72x72.png')
@app.route('/apple-touch-icon-76x76.png')
@app.route('/apple-touch-icon-114x114.png')
@app.route('/apple-touch-icon-120x120.png')
@app.route('/apple-touch-icon-144x144.png')
@app.route('/apple-touch-icon-152x152.png')
@app.route('/apple-touch-icon-180x180.png')
@app.route('/mstile-70x70.png')
@app.route('/mstile-144x144.png')
@app.route('/mstile-150x150.png')
@app.route('/mstile-310x150.png')
@app.route('/mstile-310x310.png')
def touch_icons():
    filename = request.path.lstrip('/')
    return send_from_directory(
        os.path.join(app.root_path, 'static/images'),
        filename,
        mimetype='image/png'
    )


if __name__ == '__main__':
    app.run(debug=True)
