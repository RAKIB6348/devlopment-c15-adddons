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

    note = fields.Text(string='Description')

    # address information
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip')
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')

    # Degree Information
    degree_name = fields.Char(string="Degree Name")
    university = fields.Char(string="University")
    passing_year = fields.Char(string="Year of Completion")

