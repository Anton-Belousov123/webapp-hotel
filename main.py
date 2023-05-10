import json

from flask import Flask, render_template, request

import test
from utils import is_html_file_exists

application = Flask(__name__)


@application.route('/')
def index_page():
    try:
        query_id = list(request.args.keys())[0]
    except:
        query_id = ''
    info = json.load(open('pages.json'))
    return render_template('pages/main_page.html',
                           sections=info['items'],
                           heading=info['heading'],
                           title=info['title'],
                           page_image=info['image'],
                           titles=info['items'],
                           query_id=query_id)


@application.route('/order', methods=['POST'])
def order_handler():
    test.send_answer(request.form.to_dict())
    return 'ok'


@application.route('/section/<section>', methods=['POST'])
def section_page(section):
    try:
        query_id = list(request.args.keys())[0]
    except:
        query_id = ''
    return f"OK {query_id}"
    pages = json.load(open('pages.json'))['items']
    for page in pages:
        if str(page['id']) == str(section):
            title, image = page['title_at_open'], page['image']
            break

    info = json.load(open('pages.json'))
    services = json.load(open('sections.json'))
    return render_template(f'pages/section_page.html', services=services,
                           title=title, page_image=image, titles=info['items'], query_id=query_id)


@application.route('/service/<service>')
def service_page(service):
    try:
        query_id = list(request.args.keys())[0]
    except:
        query_id = ''
    sections = json.load(open('sections.json'))
    for section in sections:
        if str(section['id']) == str(service):
            title, image = section['title'], section['image']
            break
    services = json.load(open('services.json'))
    info = json.load(open('pages.json'))
    return render_template(f'pages/service_page.html', titles=info['items'], items=services, title=title,
                           page_image=image, query_id=query_id, sections=json.load(open('sections.json')))


@application.route('/admin', methods=['GET', 'POST'])
def admin_page():
    information = json.load(open('pages.json'))
    info = information['items']
    main_page = {'title_at_open': information['heading'], 'title': information['title'], 'image': information['image']}
    sections = json.load(open('sections.json'))
    services = json.load(open('services.json'))
    if request.method == 'GET':
        args = request.args.to_dict()

        if 'page' in args.keys():
            if args['page'] == 'main':
                return render_template('admin/main.html', pages=info, main_page=main_page)
            elif args['page'] == 'section':
                return render_template('admin/section.html', pages=sections, titles=information)
            elif args['page'] == 'service':
                return render_template('admin/service.html', pages=services, sections=sections)
            else:
                return render_template('utils/404.html')
        return render_template('admin/admin.html')
    else:
        data = request.form.to_dict()
        print(data)
        if data['method'] == 'delete-page':
            pg = json.load(open('pages.json'))
            new_pg = []
            for i in pg['items']:
                if str(i['id']) != str(data['id']):
                    new_pg.append(i)
            pg['items'] = new_pg
            with open('pages.json', 'w', encoding='UTF-8') as f:
                f.write(json.dumps(pg))
            f.close()
            info = json.load(open('pages.json'))['items']
            return render_template('admin/main.html', pages=info, main_page=main_page)

        if data['method'] == 'create-page':
            s = request.form.to_dict()
            pg = json.load(open('pages.json'))
            pg['items'].append({'title': s['name'], 'image': s['photo'], 'title_at_open': s['name_at_open'],
                                'id': str(int(pg['items'][-1]['id']) + 1)})
            with open('pages.json', 'w', encoding='UTF-8') as f:
                f.write(json.dumps(pg))
            f.close()
            info = json.load(open('pages.json'))['items']
            return render_template('admin/main.html', pages=info, main_page=main_page)

        if data['method'] == 'editmainpage-page':
            s = request.form.to_dict()
            pg = json.load(open('pages.json'))
            pg['image'] = s['photo']
            pg['title'] = s['name']
            pg['heading'] = s['name_at_open']
            with open('pages.json', 'w', encoding='UTF-8') as f:
                f.write(json.dumps(pg))
            f.close()
            information = json.load(open('pages.json'))
            info = information['items']
            main_page = {'title_at_open': information['heading'], 'title': information['title'],
                         'image': information['image']}
            return render_template('admin/main.html', pages=info, main_page=main_page)

        if data['method'] == 'update-page':
            pg = json.load(open('pages.json'))
            c = pg['items']
            for i in range(len(c)):
                if str(c[i]['id']) == str(data['id']):
                    c[i]['id'] = data['id']
                    c[i]['image'] = data['photo']
                    c[i]['title'] = data['name']
                    c[i]['title_at_open'] = data['name_at_open']
            pg['items'] = c
            with open('pages.json', 'w', encoding='UTF-8') as f:
                f.write(json.dumps(pg))
            f.close()
            info = json.load(open('pages.json'))['items']
            return render_template('admin/main.html', pages=info, main_page=main_page)

        if data['method'] == 'update-section':
            c = json.load(open('sections.json'))
            for i in range(len(c)):
                if str(c[i]['id']) == str(data['id']):
                    c[i]['id'] = data['id']
                    c[i]['image'] = data['image']
                    c[i]['title'] = data['name']
                    c[i]['worked_at'] = data['worked_at']
                    c[i]['description'] = data['description']

            with open('sections.json', 'w', encoding='UTF-8') as f:
                f.write(json.dumps(c))
            f.close()
            info = json.load(open('sections.json'))
            return render_template('admin/section.html', pages=sections, titles=information)

        if data['method'] == 'update-service':
            c = json.load(open('services.json'))
            for i in range(len(c)):
                if str(c[i]['id']) == str(data['id']):
                    c[i]['id'] = data['id']
                    c[i]['image'] = data['photo']
                    c[i]['title'] = data['name']
                    c[i]['price'] = data['price']
                    c[i]['description'] = data['description']

            with open('services.json', 'w', encoding='UTF-8') as f:
                f.write(json.dumps(c))
            f.close()
            info = json.load(open('services.json'))
            return render_template('admin/service.html', pages=info, sections=sections)

        if data['method'] == 'create-section':
            s = request.form.to_dict()
            pg = json.load(open('sections.json'))
            try:
                new_id = str(int(pg[-1]['id']) + 1)
            except:
                new_id = 0
            pg.append({
                'connected_with': s['connected_with'],
                'title': s['name'], 'image': s['photo'], 'worked_at': s['worked_at'], 'description': s['description'],
                'id': new_id})
            with open('sections.json', 'w', encoding='UTF-8') as f:
                f.write(json.dumps(pg))
            f.close()
            info = json.load(open('sections.json'))
            return render_template('admin/section.html', pages=sections, titles=information)

        if data['method'] == 'create-service':
            s = request.form.to_dict()
            print(s)
            pg = json.load(open('services.json'))
            try:
                new_id = str(int(pg[-1]['id']) + 1)
            except:
                new_id = 0
            pg.append({
                'connected_with': s['connected_with'],
                'title': s['name'], 'image': s['photo'], 'price': s['price'], 'description': s['description'],
                'id': new_id})
            with open('services.json', 'w', encoding='UTF-8') as f:
                f.write(json.dumps(pg))
            f.close()
            info = json.load(open('services.json'))
            return render_template('admin/service.html', pages=info, sections=sections)

        if data['method'] == 'delete-section':
            print('I erergergerge')
            pg = json.load(open('sections.json'))
            new_pg = []
            for i in pg:
                if str(i['id']) != str(data['id']):
                    new_pg.append(i)
            with open('sections.json', 'w', encoding='UTF-8') as f:
                f.write(json.dumps(new_pg))
            f.close()
            info = json.load(open('sections.json'))
            return render_template('admin/section.html', pages=sections, titles=information)

        if data['method'] == 'delete-service':
            pg = json.load(open('services.json'))
            new_pg = []
            for i in pg:
                if str(i['id']) != str(data['id']):
                    new_pg.append(i)
            with open('services.json', 'w', encoding='UTF-8') as f:
                f.write(json.dumps(new_pg))
            f.close()
            info = json.load(open('services.json'))
            return render_template('admin/service.html', pages=info, sections=sections)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
