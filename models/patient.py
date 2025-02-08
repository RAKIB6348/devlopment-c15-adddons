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
        if not vals.get('note'):
            # override create method
            vals['note'] = "New Created Patient"
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
    registration_date = fields.Date(string="Registration Date")
    age_group = fields.Selection([('major','Major'),
                                  ('minor', 'Minor'),
                                  ],string='Age Group', compute='set_age_group')
    email_id = fields.Char(string='Email')
    doctor_id = fields.Many2one('patient.doctor', string='Doctor')
    user_id = fields.Many2one('res.users', string='PRO')

    # address information
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip')
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')


    #depends on age
    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError(_("Age cannot be zero. Please enter a valid age."))

    # depends on age
    @api.depends('age')
    def set_age_group(self):
        for rec in self:
            if rec.age <= 18:
                rec.age_group = 'minor'
            else:
                rec.age_group = 'major'

    
    # overrride write method
    # def write(self, vals_to):
    #     if not self.age:
    #         vals_to['contact'] = '0123456789'
    #     return super(HospitalPatient, self).write(vals_to)


# inherit view and add field
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user = fields.Many2one('res.users', string='Confirmed By')

    def action_cancel(self):
        super(SaleOrder, self).action_cancel()
        self.confirmed_user = self.env.user.id