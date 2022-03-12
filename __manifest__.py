# -*- coding: utf-8 -*-
{
    'name': "Wedding Masbin 14",

    'summary': """
        Wedding""",

    'description': """
        Aplikasi Sistem Weding untuk masbin
    """,

    'author': "Bintang Mas",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',
    'aplication':True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/panggung_views.xml',
        'views/pelaminan_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}