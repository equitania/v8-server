{
    'name': 'Web Gantt',
    'category': 'Hidden',
    'description': """
OpenERP Web Gantt chart view.
=============================

""",
    'version': '2.0.060617',
    'depends': ['web'],
    'data' : [
        'views/web_gantt.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'auto_install': True
}
