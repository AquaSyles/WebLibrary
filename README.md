# WebLibrary

WebLibrary is a web-based application designed to manage and organize a library of books.

## Features

- **Book Management**: Add, edit, and remove books from the library.
- **Search Functionality**: Search for books by title, author, or genre.
- **User Authentication**: Secure login and registration system.
- **Responsive Design**: Mobile-friendly user interface.

## Technology Stack

- **HTML**: Structure and content of the web pages.
- **Python**: Backend logic and server-side operations.
- **JavaScript**: Client-side scripting and interactivity.
- **CSS**: Styling and layout of the web pages.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/AquaSyles/WebLibrary.git
   cd WebLibrary
   ```

2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   . venv/bin/activate  # On Windows, use `. venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create the .env file (use any SECRET_KEY you want):
   ```sh
   cd WebLibrary
   echo 'SECRET_KEY="fsq790j8ze0#al3pcs(j0y+fn4d^j9*4-vr*=x%$no_d^m41vi"' > .env # Make sure it's UTF-8, as this might not be the case on Windows, so you can just write the SECRET_KEY manually.
   ```

5. Make migrate for Django's ORM to set up the database:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the application:
   ```sh
   python manage.py runserver
   ```
