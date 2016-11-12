{
    'name' : 'IM Bus',
    'version': ‘1.0.1’,
    'author': 'OpenERP SA',
    'category': 'Hidden',
    'complexity': 'easy',
    'description': "Instant Messaging Bus allow you to send messages to users, in live.",
    'depends': ['base', 'web'],
    'data': [
        'views/bus.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': True,
}
