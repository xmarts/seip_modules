from odoo import api, fields, models, _
from . import amount_to_text

class OeHealthInherithPayment(models.Model):
    _inherit = 'account.payment'
    _description = 'Anexo a pagos'

    hospital_origen = fields.Many2one('oeh.medical.health.center', string='Hospital Origen', default=lambda self: self.env.user.hospital_usuario)
    expediente = fields.Char(string='Expediente', compute="_get_expediente")
    amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True, help='Amount of the invoice in letter')

    @api.one
    @api.depends('amount')
    def _get_amount_to_text(self):
        self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount, 'MXN') 

    @api.model
    def oeh_payments_searchs(self):
        if self.env.user.id==1:
            action = {
                'type': 'ir.actions.act_window',
                'view_mode': 'tree,form',
                'name': _('Pagos OeHealth'),
                'res_model': 'account.payment',
            }
            return action
        else:
            action = {
                'type': 'ir.actions.act_window',
                'view_mode': 'tree,form',
                'name': _('Pagos OeHealth'),
                'res_model': 'account.payment',
                'domain': [('hospital_origen', '=', self.env.user.hospital_usuario.id)],
            }
            return action

    @api.one
    @api.depends('partner_id','expediente')
    def _get_expediente(self):
        cr = self.env.cr
        pid = self.partner_id.id
        sql = "select identification_code from oeh_medical_patient where partner_id='"+str(pid)+"'"
        cr.execute(sql)
        id_returned = cr.fetchone()
        for t in id_returned:
            self.expediente = str(t)

class OeHealthInherithPayment(models.Model):
    _inherit = 'account.invoice'
    _description = 'Anexo a facturas'

    hospital_origen = fields.Many2one('oeh.medical.health.center', string='Hospital Origen', default=lambda self: self.env.user.hospital_usuario)
    expediente = fields.Char(string='Expediente', compute="_get_expediente")
    amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True, help='Amount of the invoice in letter')

    @api.one
    @api.depends('amount_total')
    def _get_amount_to_text(self):
        self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount_total, 'MXN') 

    @api.model
    def oeh_invoices_searchs(self):
        if self.env.user.id==1:
            action = {
                'type': 'ir.actions.act_window',
                'view_mode': 'tree,form',
                'name': _('Facturas OeHealth'),
                'res_model': 'account.invoice',
            }
            return action
        else:
            action = {
                'type': 'ir.actions.act_window',
                'view_mode': 'tree,form',
                'name': _('Facturas OeHealth'),
                'res_model': 'account.invoice',
                'domain': [('hospital_origen', '=', self.env.user.hospital_usuario.id)],
            }
            return action

    @api.one
    @api.depends('partner_id','expediente')
    def _get_expediente(self):
        cr = self.env.cr
        pid = self.partner_id.id
        sql = "select identification_code from oeh_medical_patient where partner_id='"+str(pid)+"'"
        cr.execute(sql)
        id_returned = cr.fetchone()
        for t in id_returned:
            self.expediente = str(t)