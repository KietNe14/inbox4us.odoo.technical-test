from odoo import models, fields


class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'Hotel Customer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    booking_ids = fields.One2many('hotel.booking', 'customer_id', string='Bookings')
    report_id = fields.Many2one('hotel.customer.report', string='Report')
