from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'patient.doctor'
    _description = 'Doctor Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    image = fields.Binary(string='Image')
    name = fields.Char(string='Name')
    age = fields.Integer(string='Age', compute='compute_age')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ], string='Gender')
    dob = fields.Date(string='Date of Birth')
    contact = fields.Char(string='Contact')
    specialization = fields.Char(string="Specialization")
    years_of_experience = fields.Integer('Years of Experience')

