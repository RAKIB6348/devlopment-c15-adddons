from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'patient.patient'
    _description = 'Patient Record'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ], string='Gender')
    contact = fields.Char(string='Contact')
    image = fields.Binary(string='Image')