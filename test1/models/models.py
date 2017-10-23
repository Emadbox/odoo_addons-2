# -*- coding: utf-8 -*-

from odoo import models, fields, api

class test1(models.Model):
    _name = 'test1.test1'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    description2 = fields.Text()
    description3 = fields.Text()
    description4 = fields.Text()
    anexo = fields.Text()
    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100