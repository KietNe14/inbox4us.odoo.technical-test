{
    'name': 'Hotel Management',
    'version': '17.0',
    'summary': 'Manage hotel room bookings and customers',
    'depends': ['base', 'auth_signup'],
    'external_dependencies': {
        'python': ['jwt'],
    },
    'data': [
        'security/hotel_security.xml',
        'security/ir.model.access.csv',
        'data/hotel_room.xml',
        'data/hotel_customer.xml',
        'data/ir_cron.xml',
        'views/hotel_menu_views.xml',
        'views/hotel_booking_views.xml',
        'views/hotel_customer_views.xml',
        'views/hotel_room_views.xml',
        'views/report.xml',
    ],
    'installable': True,
    'application': True,
}