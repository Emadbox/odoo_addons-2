# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom sale',
    'version': '1.0',
    'category': 'Sales',
    'sequence': 5,
    'summary': 'Leads, Opportunities, Activities',
    'description': """
Otros campos para el modulo de ventass
""",
    'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'sale'
    ],
    'data': [
        'views/view.xml',
        
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
