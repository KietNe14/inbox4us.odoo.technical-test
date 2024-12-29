from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hotel Booking'

    customer_id = fields.Many2one('hotel.customer', string='Customer', required=True)
    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    check_in_date = fields.Date(string='Check-in Date', required=True)
    check_out_date = fields.Date(string='Check-out Date', required=True)
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    report_id = fields.Many2one('hotel.booking.report', string='Report')

    @api.depends('room_id', 'check_in_date', 'check_out_date')
    def _compute_total_amount(self):
        for booking in self:
            if booking.check_in_date and booking.check_out_date:
                num_nights = (booking.check_out_date - booking.check_in_date).days
                booking.total_amount = booking.room_id.price_per_night * num_nights


    # check check-in and check-out date
    @api.constrains('check_in_date', 'check_out_date')
    def _check_dates(self):
        for booking in self:
            if booking.check_in_date >= booking.check_out_date:
                raise models.ValidationError('Check-out date must be greater than check-in date!')
    
    # when booking created, change room status to 'booked'
    def create(self, vals):
        booking = super(HotelBooking, self).create(vals)
        booking.room_id.status = 'booked'
        return booking
    
    def write(self, vals):
        if self.check_out_date < datetime.now().date():
            self.room_id.status = 'available'
        return super(HotelBooking, self).write(vals)
    
     # When booking is deleted, set the room status to 'available'
    def unlink(self):
        for booking in self:
            booking.room_id.status = 'available'
        return super(HotelBooking, self).unlink()
    
    # cron job to update room status
    def cron_update_room_status(self):
        bookings = self.search([('check_out_date', '<', datetime.now().date())])
        for booking in bookings:
            booking.room_id.status = 'available'