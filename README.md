# Spotted App Backend

## Overview
The Spotted app is a Django-based application for collecting and managing car data. Users can upload information about cars they spot, including brand, model, color, year, and a picture of the car.

## Features
- User Authentication: Register, login, logout, and password reset functionalities.
- Car Data Management: Users can create, read, update, and delete information about cars.
- Image Upload: Users can upload pictures of cars, which are stored either locally or in a cloud storage.
- User-specific Access: Users can only access and modify their own car uploads.

## Technologies Used
- Django: A high-level Python Web framework.
- Django REST Framework: A powerful and flexible toolkit for building Web APIs.
- dj-rest-auth: Django REST framework-based authentication.

## Setup and Installation
1. Clone the repository
2. Install required packages:
`pip install -r requirements.txt`
3. Run migrations to create database schema:
```
python manage.py makemigrations 
python manage.py migrate
```
4. Start the server:
`python manage.py runserver`

## API Endpoints
- `/api/cars/` - CRUD operations for car data.
- `/dj-rest-auth/registration/` - User registration.
- `/dj-rest-auth/login/` - User login.
- `/dj-rest-auth/logout/` - User logout.

## Testing
Use tools like Postman for testing the API endpoints. Ensure to authenticate using the provided token in the Authorization header.
`key:Authorization, value:Token {token}`

## Future Enhancements
- Integration with cloud storage for scalable image handling.
- Advanced user role management and permissions.
- Performance optimizations and scalability improvements.

