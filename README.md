# Job-Finder

Jop-Finder is a website built using Django, a Python web framework, designed to help users search and find job opportunities. It provides a user-friendly interface for job seekers to explore and apply for relevant job listings.

## Technologies Used

The following technologies have been utilized in the development of Jop-Finder:

- **Python**: The core programming language used for building the backend logic and handling server-side operations.
- **Django**: A high-level Python web framework that provides a robust set of tools and libraries for building web applications. Django is used for handling URL routing, managing database models, and implementing business logic.
- **JavaScript**: Used for client-side interactivity and enhancing the user experience.
- **jQuery**: A fast and concise JavaScript library that simplifies HTML document traversal, event handling, and AJAX interactions.
- **HTML**: The markup language used for structuring the web pages and defining the content.
- **CSS**: Cascading Style Sheets are used for styling the web pages and defining the visual presentation.
- **SCSS**: A CSS preprocessor that extends the capabilities of CSS, offering features like variables, mixins, and nested rules.
- **Docker**: A containerization platform used to package the application and its dependencies into isolated containers, ensuring consistent deployment and scalability.
- **Redis**: An open-source in-memory data structure store used for caching and improving the performance of database queries.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs, enabling the creation of RESTful APIs to support frontend interactions.
- **Ajax**: Asynchronous JavaScript and XML is used for making asynchronous requests to the server and updating parts of the web page without reloading the entire page.
- **Celery**: A distributed task queue system that allows the execution of tasks asynchronously and in the background.
- **Postman**: A popular API development and testing tool used for testing and debugging the API endpoints.

## Installation

To set up and run Jop-Finder locally, follow these steps:

1. Clone the repository using the following command:

   ```
   git clone https://github.com/Omarmoatz/Jop-Finder.git
   ```

2. Navigate to the project directory:

   ```
   cd Jop-Finder
   ```

3. Create a virtual environment to isolate the project's dependencies:

   ```
   python3 -m venv myenv
   ```

4. Activate the virtual environment:

   - For Linux/Mac:

     ```
     source myenv/bin/activate
     ```

   - For Windows:

     ```
     myenv\Scripts\activate
     ```

5. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Set up the database by running the migrations:

   ```
   python manage.py migrate
   ```

7. Start the development server:

   ```
   python manage.py runserver
   ```

8. Open your web browser and access the application at `http://localhost:8000`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.


## Acknowledgments

We would like to express our gratitude to the open-source community and the developers of the technologies used in this project. Their contributions and efforts are greatly appreciated.

## Preview

![](screencapture.png)
