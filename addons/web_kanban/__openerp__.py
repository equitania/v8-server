{
    'name': 'Base Kanban',
    'category': 'Hidden',
    'description': """
OpenERP Web kanban view.
========================

""",
    'version': '2.0.1',
    'depends': ['web'],
    'data' : [
        'views/web_kanban.xml',
    ],
    'qweb' : [
        'static/src/xml/*.xml',
    ],
    'auto_install': True
}
