from odoo import api, fields, models,_


class HospitalPatient(models.Model):
    _name = 'patient.patient'
    _description = 'Patient Record'

    sl_no = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                    index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sl_no', _('New')) == _('New'):
            vals['sl_no'] = self.env['ir.sequence'].next_by_code('patient.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ], string='Gender')
    contact = fields.Char(string='Contact')
    image = fields.Binary(string='Image')
