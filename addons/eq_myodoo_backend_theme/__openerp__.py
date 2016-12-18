{
    # Theme information
    'name' : 'MyOdoo Backend Theme v8',
    'license': 'AGPL-3',
    'category' : 'Theme/Backend',
    'version' : '1.1.2',
    'summary': 'Backend, Theme, Equitania, MyOdoo',
    'description': """
    MyOdoo Backend Theme v8
    Die visuelle und benutzerfreundliche Überarbeitung des odoo-Backends.
    """,
    'images': ['static/description/theme.jpg'],

    # Dependencies
    'depends': [
        'web'
    ],
    'external_dependencies': {},

    # Views
    'data': [
	   'views/backend.xml'
    ],

    # Author
    'author' : 'by Equitania Software GmbH',
    'website' : 'http://www.myodoo.de',

    # Technical
    'installable': True,
    'auto_install': False,
    'application': False,

}
