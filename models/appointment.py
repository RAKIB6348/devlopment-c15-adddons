from odoo import api, fields, models,_

class HospitalAppointment(models.Model):
    _name = 'patient.appointment'
    _description = 'Appointment Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_name'

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
    patient_name = fields.Char(string='Patient Name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ],string='Gender')
    appointment_date = fields.Date(string='Appointment Date', tracking=True)
    booking_date = fields.Date(string='booking_date Date', tracking=True)
    contact = fields.Char(string='Contact', tracking=True)
    email_id = fields.Char(string='Email', tracking=True)
    note = fields.Text(string='Description')
    doctor_id = fields.Many2one('patient.doctor', string='Doctor')


    # address information
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip')
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')

    state = fields.Selection([
        ('draft', 'DRAFT'),
        ('confirmed', 'CONFIRMED'),
        ('approved', 'APPROVED'),
        ('cancel', 'CANCELLED')], string='Status',
        copy=False, index=True, readonly=True,
        store=True, tracking=True,)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority",)

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'


    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_approve(self):
        for rec in self:
            rec.state = 'approved'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'