# HER Story
## About The Project
HER Story is a full-stack web application built using the Django web framework. It serves as a platform to raise awareness about women's abuse, relevant laws, and ongoing issues. The application allows administrators to manage posts, resources, and user interactions, while offering features for users to engage with stories and resources in a secure environment.
Built With

## Django - The web framework used

* PostgreSQL - Database
* HTML/CSS/JavaScript - Frontend technologies
* Gunicorn - WSGI HTTP Server
* Nginx - Web server (reverse proxy)

## Features

* Post Management: Admins can create and manage posts about real-life stories, legal updates, and other content related to women's abuse.
* Comment System: Authenticated users can leave comments on posts.
* Anonymous Story Sharing: Users can share personal stories anonymously through the "Vent Section". These submissions are reviewed by admins before publication.
* Contact Form: A dedicated section for users to communicate directly with administrators.
* Resource Management: Admins can add and update resources such as emergency contact information and counseling services.

## Project Structure

* Django Views and Templates: Utilize Django's view system and template engine for dynamic page rendering.
* Django Models: Define database structure for posts, comments, stories, and resources using Django's ORM.
* User Authentication: Leverages Django's built-in authentication system for secure user management.
* Admin Panel: Customized Django admin interface for efficient content management.

## Getting Started
To get a local copy up and running, follow these simple steps:

1. Clone the repo

    git clone https://github.com/shalomalena/her-story.git

3. Install dependencies

    pip install -r requirements.txt

4. Set up your PostgreSQL database and update settings accordingly

5. Run migrations

    python manage.py migrate

6. Create a superuser

    python manage.py createsuperuser

7. Start the development server

    python manage.py runserver

## Future Implementations

* Deployment: The application is currently in development and hasn't been deployed. Future plans include deploying the application to a production environment using Gunicorn as the WSGI server and Nginx for reverse proxy and static file serving.

* Enhanced User Profiles: Implement more detailed user profiles with customizable privacy settings.

* Multilingual Support: Add support for multiple languages to reach a broader audience.

* Integration with Support Services: Implement real-time chat or hotline connections to support services.

* Data Visualization: Add charts and graphs to visualize statistics related to women's abuse issues.

* Mobile App: Develop a complementary mobile application for increased accessibility.

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request

## Contact
Your Name - shalomalena5@example.com
Project Link: https://github.com/your_username/her-story

## Acknowledgements

Django Documentation
PostgreSQL Documentation
Bootstrap
Font Awesome





