import os
from flask import Flask, render_template, send_from_directory


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


@app.route('/apple-touch-icon<size>.png', defaults={'size': ''})
@app.route('/apple-touch-icon.png')
def apple_touch_icons(size=None):
    print('######### apple-touch-icon{}.png'.format(size))
    if size:
        filename = 'apple-touch-icon{}.png'.format(size)
    else:
        filename = 'apple-touch-icon.png'
    return send_from_directory(
        os.path.join(app.root_path, 'static/images'),
        filename,
        mimetype='image/png'
    )


@app.route('/mstile-<size>.png')
def ms_tiles(size):
    return send_from_directory(
        os.path.join(app.root_path, 'static/images'),
        'mstile-{}.png'.format(size),
        mimetype='image/png'
    )


if __name__ == '__main__':
    app.run(debug=True)
