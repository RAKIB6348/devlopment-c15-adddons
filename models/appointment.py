from odoo import api, fields, models,_

class HospitalAppointment(models.Model):
    _name = 'patient.appointment'
    _description = 'Appointment Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    app_sl = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                    index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('app_sl', _('New')) == _('New'):
            vals['app_sl'] = self.env['ir.sequence'].next_by_code('patient.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res