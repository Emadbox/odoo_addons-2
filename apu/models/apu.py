# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class apu(models.Model): 
    _name = 'ej.apu' 
    descripcion = fields.Text(string='descripcion', required=True) 
 
    rendimiento = fields.Float(string='rendimiento', required=True) 
 
    unidad_id = fields.Many2one('ej.unidad', string='Unidad')