from flask import Flask, render_template, request
from utils import is_html_file_exists

application = Flask(__name__)


@application.route('/')
def index_page():
    heading = 'Мир безупречного комфорта'
    sections = [
        {'name': 'Питание в отеле'},
        {'name': 'Массаж и СПА'},
        {'name': 'Трансфер'},
        {'name': 'Товары для вас'}
    ]
    return render_template('pages/main_page.html', sections=sections, heading=heading)


@application.route('/section/<section>')
def section_page(section):
    return render_template(f'pages/section_page.html')


@application.route('/service/<service>')
def service_page(service):
    if not is_html_file_exists(f'templates/services/{service}.html'):
        return render_template('404.html')
    return render_template(f'services/{service}.html')


@application.route('/admin', methods=['GET', 'POST'])
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


application.run(host='0.0.0.0')
