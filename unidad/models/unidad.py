# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class unidad(models.Model): 
    _name = 'ej.unidad' 
    _rec_name = 'abbr'
    abbr = fields.Text(string='abbr', required=True) 
    descripcion = fields.Text(string='descripcion', required=True)