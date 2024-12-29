## Inbox4us - Technical Test Requirements for Odoo Hotel Booking Module
### Overview
- Name module: change name to hotel_management
- Use odoo version 17.0 edition.
- Postman collection: hotel_management\Ibox4us Hotel Management.postman_collection.json
- Hotel Report:
    1. Can see guest check-in date, group by month, room details
    2. Number of guests registered can be viewed after booking, customer details
    3. Use cron update every day
### Instructions
- Fork the Repository: Fork the provided repository to your personal GitHub account.
- Clone the Repository: Clone the forked repository to your local development environment.
- Implement the Features: Complete the following tasks in your local repository.
- Commit and Push: Commit your changes and push them to your forked repository.

### Requirements
#### 1. Write REST API for Authentication using JWT
Implement user registration and login endpoints.
Use JWT for token-based authentication.

```
File: controllers/auth_controller.py
```

- Register
```bash
curl -X POST http://localhost:8069/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@inbox4us.xyz",
    "password": "password"
    }'
```

- Login 
```bash
curl -X POST http://localhost:8069/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
        "email": "john@inbox4us.xyz",
        "password": "password"
    }'
```

#### 2. Write API for Making a Booking
Implement an endpoint to create a new booking.
```
File: controllers/booking_controller.py
```

- Create Booking
```bash
curl -X POST http://localhost:8069/api/v1/booking \
  -H "Content-Type: application/json
  --header 'Authorization: Bearer <REPLACE_ACCESSTOKEN>' \
  -d '{
    "room_id": 1,
    "customer_id": 1,
    "checkin_date": "2022-01-01",
    "checkout_date": "2022-01-05"
  }'
```

#### 3. Build Reports in Odoo to Track Bookings and Customer Registrations
Objective
Develop a reporting feature in Odoo to display insights on:

- The number of bookings made within a specific period.
- The number of customers registered in the system over time

#### 4. Nice to Have (Optional)
- Handle Booking Status: Implement logic to manage booking statuses (checkin, checkout, booked).
- Conflict Resolution: Add logic to handle booking overlaps and display user-friendly errors.
- Adding Validation for Parameters Using Decorators: Implement parameter validation using decorators to ensure correct data is provided in the API requests.
- Write postman collection for testing the API.
- Apply Best Practices: Write clean, maintainable code following industry best practices.
- Document Each Function: Provide documentation for each function, explaining its purpose, parameters, and return values.