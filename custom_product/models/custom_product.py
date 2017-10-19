#-*- coding: utf-8 -*-
from odoo import api, fields, models

class ProductInherited(models.Model):
    _inherit = 'product.template'
    material_ids = fields.Many2many('ej.material','Materiales')          