# Countdown Timer
This Django app allows users to register, log in, and create event timers that countdown
to a specified completion time.

## Features

- User authentication (register, login, logout).
- Create and manage countdown timers for events.
- Display active timers with real-time countdowns to completion.
- Secure access to create/edit timers (only logged-in users can create/edit their timers).

## Prerequisites

Make sure you have the following installed:

- Python 3.7+
- Django 4.0+
- pip (Python package installer)
- virtualenv (optional but recommended for isolated environments)

## Getting Started

Follow these instructions to set up the project on your local machine

1. Clone the Repository
```commandline
git clone https://github.com/yourusername/event-timer-django-app.git
```
2. Set Up a Virtual Environment (Optional but Recommended)
```commandline
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install Dependencies
```commandline
pip install -r requirements.txt
```
4. Set Up the Database
```commandline
python manage.py migrate
```
5. Run the Development Server
```commandline
python manage.py runserver
```
6. Access the app at [localhost:3000](http://localhost:3000)

Usage

- User Authentication

  - Register: Users can create an account by signing up.
  - Login: Registered users can log in to manage their event timers.
  - Logout: Users can log out from the app.


- Creating Timers

  - After logging in, users can create a new event timer by specifying:
  - Event Name: The name of the event.
  - Completion time: The time the event will take to complete.
  - The app will display a countdown to the event in real-time on the dashboard.


- Dashboard

  - The dashboard displays a list of created timers for the logged-in user.
  - Users can view, start, reset or delete their timers.