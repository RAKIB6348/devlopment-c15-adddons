from odoo import api, fields, models,_

class HospitalAppointment(models.Model):
    _name = 'patient.appointment'
    _description = 'Appointment Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    app_sl = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                    index=True, default=lambda self: _('New'))
    ref = fields.Char(string='Reference', required=True, copy=False, readonly=True,
                    index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('app_sl', _('New')) == _('New'):
            vals['app_sl'] = self.env['ir.sequence'].next_by_code('patient.appointment') or _('New')
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('appointment.ref') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res

    image = fields.Binary(string='Image')
    patient_name = fields.Char(string='Patient Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ],string='Gender')
    appointment_date = fields.Date(string='Appointment Date')
    booking_date = fields.Date(string='booking_date Date')
    contact = fields.Char(string='Contact')