
## Installation & Setup
### 1. Clone the Repository
```sh
git clone https://github.com/8787233419/travel-app-assignment.git
cd travel
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)
```sh
python manage.py createsuperuser
```

### 6. Run the Development Server
```sh
python manage.py runserver
```
Open **http://127.0.0.1:8000/** in your browser.

## Setting Up HTML Templates in Django
1. **Create a `templates/` directory** inside your Django app (e.g., `api/templates/`).
2. Inside `settings.py`, set the `TEMPLATES` directory:
   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [BASE_DIR / 'templates'],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```
3. Store your templates inside `templates/`, e.g., `templates/home.html`, `templates/base.html`, etc.

## API Endpoints (If Using REST API)



| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/login/` | POST | List available travel options |
| `/api/loogut/` | POST | List available travel options |
| `/api/register/` | POST | List available travel options |
| `/api/travel-options/` | GET | List available travel options |
| `/api/book-travel/<id>/` | POST | Book a travel option | 
| `/api/my-bookings/` | GET | View user's bookings |
| `/api/cancel-booking/<id>/` | POST | Cancel a booking |


