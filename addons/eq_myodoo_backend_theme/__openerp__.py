{
    # Theme information
    'name' : 'MyOdoo Backend Theme v8',
    'license': 'AGPL-3',
    'category' : 'Theme/Backend',
    'version' : '1.1.22',
    'summary': 'Backend, Theme, Equitania, MyOdoo',
    'description': """
    MyOdoo Backend Theme v8
    Die visuelle und benutzerfreundliche Überarbeitung des odoo-Backends.
    """,
    'images': ['static/description/theme.jpg'],

    # Dependencies
    'depends': [
        'base_setup',
        'web',
        'web_widget_color',
        'equitania',
    ],
    'external_dependencies': {},

    # Views
    'data': [
        'security/ir.model.access.csv',
	    'views/backend.xml',
        'views/base_config_settings_view.xml',
        'views/eq_theme_customization_view.xml',
        'data/ribbon_data.xml',
        'data/theme_data.xml',
        'data/theme_customization_data.xml',
    ],

    # Author
    'author' : 'by Equitania Software GmbH',
    'website' : 'http://www.myodoo.de',

    # Technical
    'installable': True,
    'auto_install': True,
    'application': True,

}
