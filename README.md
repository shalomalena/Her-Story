# HER Story 

This project is a full-stack web application built using the Django web framework. It serves as a platform to raise awareness about women's abuse, relevant laws, and ongoing issues. The application allows an admin to manage posts, resources, and user interactions, while offering features for users to engage with stories and resources in a secure environment.

## Technologies Used
- **Backend**: Powered by Django, leveraging its robust ORM for database management and its built-in admin panel to manage posts, user submissions, and resources.
- **Frontend**: Built with HTML, CSS, and JavaScript, providing a clean and responsive user interface for interacting with the platform.
- **Database**: PostgreSQL is used for reliable data storage and management of user submissions, posts, and resources.
- **Web Server**: Deployed using Gunicorn as the WSGI server, with Nginx handling reverse proxy duties and static file serving.
- **Authentication**: User authentication and admin management are handled using Django’s built-in authentication system, ensuring secure login and comment features.
- **Deployment**: Hosted on a production server, configured using Gunicorn and Nginx for performance and scalability.

## Features
- **Post Management**: Admins can post real-life stories, legal updates, and other content related to women’s abuse. These posts appear on the home page in reverse chronological order.
- **Comment System**: Users can leave comments on posts, which requires them to submit their email.
- **Anonymous Story Sharing (Vent Section)**: Users can share their personal stories of abuse, which are sent to the admin for review. Once approved, these stories are posted anonymously.
- **Contact Form**: A contact section allows users to directly communicate with the admin for any concerns or questions.
- **Resource Management**: Admins can add and update resources like emergency contact information and counseling services, which are displayed to users for easy access.

## Project Structure
- **Django Views and Templates**: Django's view system and template engine are used for rendering pages dynamically based on the content and data stored in the database.
- **Django Models**: Database models define the structure for posts, comments, stories, and resources, leveraging Django’s ORM for data management.

