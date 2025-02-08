from odoo import api, fields, models
import datetime

class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wiz'
    _description = 'Create Appointment Wiz'

    pat_name = fields.Char(string='Name')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ],string='Gender')
    appointment_date = fields.Date(string='Appointment Date')
    booking_date = fields.Date(string='Booking Date')

    @api.model
    def default_get(self, vals):
        res = super(CreateAppointmentWizard, self).default_get(vals)
        res['booking_date'] = datetime.date.today()
        return res

    def action_create(self):
        vals = {
            'patient_name' : self.pat_name,
            'gender' : self.gender,
            'appointment_date' : self.appointment_date,
            'booking_date' : self.booking_date
        }
        self.env['patient.appointment'].create(vals)