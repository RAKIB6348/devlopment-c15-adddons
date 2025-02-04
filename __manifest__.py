{
    'name': 'odoo15 development',
    'version' :  '15.1.1.1.2',
    'category' : 'Tutorials',
    'summary' : 'odoo15 developemnt tutorials by odoo mates',
    'sequence' : 10,
    'depends' : [],
    'data' : [
        # security
        'security/ir.model.access.csv',

        # data
        'data/sequence.xml',

        # views
        'views/menu.xml',
        'views/tutorial_patient.xml',

    ],
    'installable' : True,
    'application' : True,
}