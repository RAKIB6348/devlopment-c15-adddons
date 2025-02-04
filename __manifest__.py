{
    'name': 'odoo15 development',
    'version' :  '15.1.1.1.2',
    'category' : 'Tutorials',
    'summary' : 'odoo15 developemnt tutorials by odoo mates',
    'sequence' : 10,
    'depends' : ['mail'],
    'data' : [
        # security
        'security/ir.model.access.csv',

        # data
        'data/sequence.xml',
        'data/patient_ref_sequence.xml',
        'data/appointment_sequence.xml',
        'data/appointment_ref_sequence.xml',

        # views
        'views/menu.xml',
        'views/tutorial_patient.xml',
        'views/tutorial_appointment.xml',
        'views/tutorial_doctor.xml',

    ],
    'installable' : True,
    'application' : True,
}