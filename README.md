# Event Countdown Timer

A simple Django web application that allows users to add events with a date and time and displays a live countdown until the event.

## Features

- Add new events
- Store event details in the database
- Display event name, date, and time
- Live countdown timer
- Shows `EXPIRED` when the event time has passed
- Simple and responsive user interface

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite

## Project Structure

```text
Event_Countdown_Timer/
│
├── Event_Countdown_Timer/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
└── README.md

How to Run
1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal in the project folder.
4. Activate the virtual environment.
5. Run the following command:
python manage.py runserver
6. Open this address in your browser:
http://127.0.0.1:8000/

Main Functionality
Users can add an event by providing:
- Event name
- Event date
- Event time

The application then displays the event and continuously updates the remaining days, hours, minutes, and seconds.

Author
Ajay Raj Chauhan
