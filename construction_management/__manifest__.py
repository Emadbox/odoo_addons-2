# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name": "Odoo Construction Management",
    "version": "1.0",
    "depends": ['base', 'project', 'stock',
                'account', 'hr', 'purchase', 'account_asset','sale','account_budget',
                #'project_issue',
                #'website_project_issue_sheet',
                'note',
                ],
    "author": "Browseinfo",
    "summary": "Real Estate Management, Construction Project management, Building Construction",
    "description": """
    BrowseInfo developed a new odoo/OpenERP module apps.
    This module use for Real Estate Management, Construction management, Building Construction,
    """,
    "website": "www.browseinfo.in",
    "data": [
        "security/ir.model.access.csv",
        'view/project.xml',
        "view/main_menu.xml",
        'view/bill_of_quantity_view.xml',
        'view/cost_code_view.xml',
        'view/cost_header_view.xml',
        'view/work_package_view.xml',
        'view/construction_management.xml',
        'report/construction_report.xml',
        'report/project_project_report.xml',
        'report/project_note_report.xml',
        'report/project_job_orders.xml',
        # Sub Task
        'view/sub_task.xml',
    ],
    "images": 'static/main_screenshot.png',
    "price": 55,
    "currency": 'EUR',
    "auto_install": False,
    "installable": True,
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
