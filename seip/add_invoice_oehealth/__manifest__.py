{
    'name': 'Ticket - Recibo de compra',
    'version': '1.0',
    'summary': 'Personalizacion de ANA PEREZ',
    'description': 'Modificacion del recibo de compra',
    'category': 'Personalizacion',
    'author': 'Pablo Osorio',
    'website': 'www.xmarts.com',
    'depends': [
        'sale',
        'oehealth'
                ],
    'data': [
        'reports/report_payment_ticket.xml',
        'views/views.xml'
    ],
    'installable': True,
    'auto_install': False,
}
