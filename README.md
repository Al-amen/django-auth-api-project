# 🛡️ Django REST Authentication API

This project is a **Django REST Framework (DRF)** based user authentication system with a **custom user model** using **email as the username**. It supports full user registration, login, profile management, password change, and password reset functionalities. JWT is used for secure authentication.

## 🚀 Features

- ✅ Custom User Model with Email as Username
- ✅ JWT Authentication with `SimpleJWT`
- ✅ Register & Login APIs
- ✅ User Profile Endpoint
- ✅ Change Password Endpoint
- ✅ Send Password Reset Email with Token
- ✅ Password Reset via UID & Token
- ✅ Email Utility Class
- ✅ Token Validations & Expiry Handling

## 📂 Project Structure

```plaintext
.
├── account/
│   ├── models.py            # Custom User model
│   ├── serializers.py       # DRF serializers
│   ├── views.py             # API views
│   ├── urls.py              # Routes
│   ├── utils.py             # Email utility
├── djangoauthapiproject/
│   ├── settings.py          # JWT & Email setup
│   └── urls.py              # Include account.urls
├── manage.py
└── README.md

⚙️ Setup Instructions
  1.Clone the Repository
    git clone https://github.com/Al-Amen/django-auth-api.git
    cd django-auth-api
  2.Create and Activate Virtual Environment
    python -m venv venv
    source venv/bin/activate   # For Linux/macOS
    venv\Scripts\activate      # For Windows
  3.Install Dependencies
    pip install -r requirements.txt
  4.Apply Migrations
    python manage.py makemigrations
    python manage.py migrate

📬 Password Reset Flow
    User submits their email.
    System generates a unique token + UID.
    Sends a secure password reset link via email.
    User clicks the link → resets password using the token.

📫 API Endpoints
    Method	    Endpoint	        Description
    POST	/api/user/register/  	Register a new user
    POST	/api/user/login/	    Login user and receive JWT token
    GET	   /api/user/profile/	    Get user profile (JWT protected)
    POST	/api/user/change-password/	Change password (JWT protected)
    POST	/api/user/send-reset-password-email/	Send password reset email
    POST	/api/user/reset-password/<uidb64>/<token>/	Reset password using token


    

  
