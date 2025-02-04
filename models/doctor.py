from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Record'

    image = fields.Binary(string='Image')
    name = fields.Char(string='Name')
    age = fields.Integer(string='Age', compute='compute_age')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ], string='Gender')
    dob = fields.Date(string='Date of Birth')
    contact = fields.Char(string='Contact')
