# helix_py
Double Helix in Python

This is a test project we are using to showcase how Django and React is used to build a webapp

## Prerequisites

- Python 3.8+
- Node.js (v16+ recommended) & npm or yarn
- pip (Python package manager)

## Requiremnents
```bash
pip install django
pip install djangorestframework django-cors-headers
pip install numpy
```

## Backend (Django) Setup

1. **Install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Run the backend server:**
   ```bash
   python manage.py runserver
   ```

## Frontend (React) Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Run the frontend development server:**
   ```bash
   npm start
   # or
   yarn start
   ```

## Development Workflow

- The Django backend will typically run on [http://localhost:8000](http://localhost:8000)
- The React frontend will typically run on [http://localhost:3000](http://localhost:3000)
- You may need to configure CORS or proxy settings for API requests.

## Building for Production

- **Frontend:**  
  In the `frontend` directory, run:
  ```bash
  npm run build
  # or
  yarn build
  ```
  This will create a production-ready build in `frontend/build/`.

- **Backend:**  
  Collect static files (if serving React build via Django):
  ```bash
  python manage.py collectstatic
  ```

---

Feel free to adjust directory names or commands if your project structure is different!

