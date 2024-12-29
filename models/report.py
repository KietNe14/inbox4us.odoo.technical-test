from odoo import models, fields, api
from datetime import datetime, timedelta

class BookingReport(models.Model):
    _name = 'hotel.booking.report'
    _description = 'Hotel Booking Report'
    
    check_in_date = fields.Date(string="Date")
    booking_count = fields.Integer(string="Number of Bookings", compute='_compute_booking_count')
    booking_ids = fields.One2many('hotel.booking', 'report_id', string='Bookings')

    @api.depends('booking_ids')
    def _compute_booking_count(self):
        for report in self:
            report.booking_count = len(report.booking_ids)

    @api.model
    def generate_booking_report(self):
        """
        Generate the report data for bookings.
        """

        today = datetime.now().date()
        last_record = self.search([], order='check_in_date desc', limit=1)
        if last_record:
            start_date = today
        else:
            # If no records exist, start from the beginning of the year
            start_date = today.replace(month=1, day=1)
        
        bookings = self.env['hotel.booking'].search([
            ('check_in_date', '>=', start_date),
        ])
        for booking in bookings:
            report = self.search([('check_in_date', '=', booking.check_in_date)])
            if report:
                booking.write({'report_id': report.id})
            else:
                report = self.create({
                    'check_in_date': booking.check_in_date,
                })
                booking.write({'report_id': report.id})
                

class CustomerRegistrationReport(models.Model):
    _name = 'hotel.customer.report'
    _description = 'Customer Registration Report'
    
    date = fields.Date(string="Date")
    customer_count = fields.Integer(string="Number of Registrations", compute='_compute_customer_count')
    customer_ids = fields.One2many('hotel.customer', 'report_id', string='Customers')

    @api.depends('customer_ids')
    def _compute_customer_count(self):
        for report in self:
            report.customer_count = len(report.customer_ids)

    @api.model
    def generate_customer_report(self):
        """
        Generate the report data for customer registrations.
        """
        today = datetime.now().date()
        
        # get date start from the last record
        last_record = self.search([], order='date desc', limit=1)
        if last_record:
            start_date = today
        else:
            # If no records exist, start from the beginning of the year
            start_date = today.replace(month=1, day=1)

        # search customers
        customers = self.env['hotel.customer'].search([('create_date', '>=', start_date)])
        for customer in customers:
            report = self.search([('date', '=', customer.create_date)])
            if report:
                customer.write({'report_id': report.id})
            else:
                report = self.create({
                    'date': customer.create_date,
                })
                customer.write({'report_id': report.id})