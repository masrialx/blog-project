# Blogging Platform API

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Blogging Platform API is a RESTful API built with Django and Django REST Framework. It allows users to create, read, update, and delete blog posts, comments, and user profiles. This project aims to provide a platform for users to share their thoughts and engage with a community of readers.

## Features
- **User Authentication**: Secure user registration and authentication.
- **Blog Post Management**: Create, read, update, and delete blog posts.
- **Comment System**: Users can comment on blog posts.
- **Category and Tag Support**: Organize posts by categories and tags.
- **User Profiles**: Manage user profiles, including bio and profile picture.
- **Like System**: Users can like blog posts.

## Technologies Used
- **Django**: A high-level Python web framework that encourages rapid development.
- **Django REST Framework**: A powerful toolkit for building Web APIs.
- **SQLite**: A lightweight database for local development.
- **Markdown**: For formatting blog post content.
- **Docker** (optional): For containerization.

## Getting Started

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)
- Django 3.2 or later
- Django REST Framework
- SQLite (or other database systems if preferred)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/masrialx/blogging-platform.git
   cd blogging-platform
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

2. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Access the API at `http://127.0.0.1:8000/api/`.

## API Endpoints
### User Authentication
- `POST /api/register/` - Register a new user.
- `POST /api/login/` - Log in a user.

### Blog Posts
- `GET /api/posts/` - List all blog posts.
- `POST /api/posts/` - Create a new blog post.
- `GET /api/posts/{id}/` - Retrieve a specific blog post.
- `PUT /api/posts/{id}/` - Update a specific blog post.
- `DELETE /api/posts/{id}/` - Delete a specific blog post.

### Comments
- `GET /api/comments/` - List all comments.
- `POST /api/comments/` - Create a new comment.
- `DELETE /api/comments/{id}/` - Delete a specific comment.

### User Profiles
- `GET /api/profiles/` - Retrieve user profile information.
- `PUT /api/profiles/{id}/` - Update user profile.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

