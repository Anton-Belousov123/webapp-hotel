from flask import Flask, render_template, request
from utils import is_html_file_exists
app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/section/<section>')
def section_page(section):
    if not is_html_file_exists(f'templates/sections/{section}.html'):
        return render_template('404.html')
    return render_template(f'sections/{section}.html')


@app.route('/service/<service>')
def service_page(service):
    if not is_html_file_exists(f'templates/services/{service}.html'):
        return render_template('404.html')
    return render_template(f'services/{service}.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'GET':
        args = request.args.to_dict()
        if 'page' in args.keys():
            if args['page'] == 'main':
                return render_template('admin/main.html')
            elif args['page'] == 'section':
                return render_template('admin/section.html')
            elif args['page'] == 'service':
                return render_template('admin/service.html')
            else:
                return render_template('404.html')
        return render_template('admin.html')
    print(request.form.to_dict())



app.run(debug=True, host='0.0.0.0', port='8000')
