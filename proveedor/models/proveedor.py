# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class proveedor(models.Model): 
    _name = 'ej.proveedor' 
    razon_social = fields.Char(string='Razón social', required=True) 
    descuento_compra = fields.Float(string='Descuento compra', required=False, default=0.0)
    ref_externa = fields.Char(string='Referencia externa', required=False)
    marca = fields.Char(string='Marca', required=False)
    material_id = fields.Many2one('ej.material', 'Materiales')