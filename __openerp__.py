# -*- coding: utf-8 -*-
{
    'name': "Physical Access Controllers",

    'summary': """
       A module to add physical card access to odoo""",

    'description': """
        You can define multiple machines and user permission per machine
    """,

    'author': "Kevin Harrington",
    'website': "https://github.com/nation-of-makers/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
	'templates.xml',
	'data/defaultdata.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
