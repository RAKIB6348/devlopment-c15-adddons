from odoo import api, fields, models,_
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'patient.patient'
    _description = 'Patient Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sl_no = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                    index=True, default=lambda self: _('New'))
    ref = fields.Char(string='Reference', required=True, copy=False, readonly=True,
                        index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sl_no', _('New')) == _('New'):
            vals['sl_no'] = self.env['ir.sequence'].next_by_code('patient.patient') or _('New')
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('patient.ref') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ], string='Gender')
    contact = fields.Char(string='Contact')
    image = fields.Binary(string='Image')
    note = fields.Text(string='Description')


    #depends on age
    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError(_("Age cannot be zero. Please enter a valid age."))
