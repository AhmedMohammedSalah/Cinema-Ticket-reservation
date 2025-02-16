# Cinema Ticket Reservation System

## Overview
The Cinema Ticket Reservation System is a comprehensive Django-based web application that provides a complete solution for managing movie screenings, guest information, and ticket reservations. Built with Django REST Framework, it offers both a user-friendly web interface and a robust REST API for system integration.

## Key Features

### Movie Management
- Create, update, and delete movie listings
- Store movie details including:
  - Hall number
  - Movie title
  - Screening date and time
- View all upcoming movies

### Guest Management
- Register and manage guest information
- Store guest details:
  - Full name
  - Contact phone number
- View guest reservation history

### Reservation System
- Create and manage ticket reservations
- Link guests to specific movie screenings
- View all active reservations
- Search and filter reservations

### RESTful API
- Full CRUD operations for all models
- Multiple view implementations:
  - Function-based views (FBV)
  - Class-based views (CBV)
  - Mixins
  - Generics
  - ViewSets
- Special API endpoints:
  - Find movies by criteria
  - Create new reservations
  - Get reservation details

### User Interface
- Responsive design using Bootstrap
- Intuitive navigation
- Crispy forms for better form handling
- Modern and clean interface

## Technology Stack
- **Backend**: Django 4.2.1
- **API**: Django REST Framework 3.14.0
- **Frontend**: Bootstrap 5, Crispy Forms
- **Database**: SQLite (default)

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedMohammedSalah/Cinema-Ticket-reservation.git
   cd Cinema-Ticket-reservation
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r src/requirements.txt
   ```

4. Run database migrations:
   ```bash
   python src/manage.py migrate
   ```

5. Create superuser (optional):
   ```bash
   python src/manage.py createsuperuser
   ```

6. Start development server:
   ```bash
   python src/manage.py runserver
   ```

## Usage

### Web Interface
Access the web interface at:
```
http://127.0.0.1:8000/
```

### API Endpoints
Base URL: `http://127.0.0.1:8000/api/`

| Endpoint              | Method | Description                     |
|-----------------------|--------|---------------------------------|
| `/movies/`            | GET    | List all movies                |
| `/movies/<id>/`       | GET    | Get specific movie details    |
| `/guests/`            | GET    | List all guests               |
| `/guests/<id>/`       | GET    | Get specific guest details    |
| `/reservations/`      | GET    | List all reservations        |
| `/reservations/<id>/` | GET    | Get specific reservation      |
| `/findmovie/`          | POST   | Search for movies             |
| `/newreservation/`    | POST   | Create new reservation        |

## Contributing
Contributions are welcome! Please follow these guidelines:
1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request with detailed description

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
