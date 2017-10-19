#-*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'
    namec = fields.Char(string='Nombre del cliente', readonly=True, copy=False, required=False, default=lambda self: self._get_default_name())
    contacto_id = fields.Many2one('res.partner','Contacto')
    iva = fields.Float('IVA %',default=19.0)
    iva_materiales = fields.Float('IVA materiales %',default=19.0)
    f_prestaciones_MO = fields.Float('F. prestación MO %',defaut=60.0)
    fc_materiales = fields.Float('Materiales (FC)',default=0.0)
    fc_herramientas = fields.Float('Herramientas (FC)',default=0.0)
    fc_recursos = fields.Float('RRHH (FC)',default=0.0)
    mg_materiales = fields.Float('Materiales (MG)',default=0.0)
    mg_herramientas = fields.Float('Herramientas (MG)',default=0.0)
    mg_recursos = fields.Float('RRHH (MG)',default=0.0)
    @api.model
    def _get_default_name(self):
        if self.partner_id:
            return self.partner_id.id
        return ''
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id:
            self.update({'namec':self.partner_id.name})
        return super(SaleOrderInherited, self).onchange_partner_id()            