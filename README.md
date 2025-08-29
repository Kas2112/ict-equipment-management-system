# ICT Equipment Management System

## Backend

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Configure your MySQL database in `equipment_mgmt/settings.py`.
3. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
5. Start backend server:
    ```bash
    python manage.py runserver
    ```

## Frontend

1. Install dependencies:
    ```bash
    npm install
    ```
2. Start frontend:
    ```bash
    npm start
    ```

## Usage

- Access the frontend at `http://localhost:3000`.
- Access the Django admin at `http://localhost:8000/admin`.
- API available at `http://localhost:8000/api/`