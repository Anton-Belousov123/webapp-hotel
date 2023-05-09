from flask import Flask, render_template, request
from utils import is_html_file_exists
from OpenSSL import SSL

context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

app = Flask(__name__)


@app.route('/')
def index_page():
    heading = 'Мир безупречного комфорта'
    sections = [
        {'name': 'Питание в отеле'},
        {'name': 'Массаж и СПА'},
        {'name': 'Трансфер'},
        {'name': 'Товары для вас'}
    ]
    return render_template('pages/main_page.html', sections=sections, heading=heading)


@app.route('/section/<section>')
def section_page(section):
    return render_template(f'pages/section_page.html')


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


app.run(debug=True, host='0.0.0.0', port='5000', ssl_context=context)
