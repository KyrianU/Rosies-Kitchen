# Testing 

to return to the readme file please click here [README](README.md)

### User Stories 

####  As a User, I would like to be able to navigate the website
- As a user, I am able to navigate through the site and view desired content without issues


#### As as user, I would like to have access to an informative landing page 
- As a user, I would like to be able to be well informed about what the restaurant is all about.

#### Opening time 
- As a user, I would like to know the opening time in order to make a reservation accordingly 
![Opening times](documentations/features/footer.png)

#### Menu
- As a User, I would like to have a view of the menu 
![Menu](documentations/features/menu.png)

#### Register 
- As a user, I want to register and account in order to make a reservation 
![Register](documentations/images/register.png)
![Register](documentations/images/register-success.png)

#### Make a reservation 
- As as user, once I have been able to register and account, I would like to be able to start making 
reservations 
![Booking](documentations/features/reservation.png)

#### As a user, I would like to manage my bookings
- As a user, I would like to have access to all my bookings and have the option to either amend or cancel 
any bookings I may have 
![My Reservations](documentations/images/my_reservation.png)

#### As a user, I want to be able to amend my reservation
- As a user, I want to be able to amend a reservation for my convenience
![Edit Reservation](documentations/images/edit-reservation.png)

#### As a user, I want to be able to delete my reservation
- As a user, I want to be able to delete a reservation if the time and date is not longer
suitable for the user
![Delete Reservatiion](documentations/images/delete_reservation.png)

## Admin login
- As an admin, I want to be able to log in the admin panel and delete accounts of my choice
![Admin panel](documentations/images/admin%20login.png)
![Admin panel](documentations/images/adminpanel.png)


# Bugs 

## Fixed Bugs
- Users were unable to edit or delete their reservation, this was due to a typing error in the reservation view.
- Users were able to view and make amendments for other users reservations
- Fixed the bug that was enabling user to book a date that's in the past 
- Fixed issue regarding the Date picker, typing error in the forms.py file in the reservation app

## Unfixed Bugs
- Seats option allows you to pick an infinite number, but only allows you to pick 1-4 seats
- Users are able to set duplicate reservation for the same time and day 
