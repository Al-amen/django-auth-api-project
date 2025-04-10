<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django REST Authentication API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            color: #333;
        }
        h1, h2, h3 {
            color: #4CAF50;
        }
        h1 {
            font-size: 2em;
            margin-bottom: 10px;
        }
        h2 {
            margin-top: 20px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        .todo {
            background-color: #ffeb3b;
            padding: 10px;
            margin-top: 20px;
        }
        .setup-instructions {
            background-color: #f1f1f1;
            padding: 15px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>🛡️ Django REST Authentication API</h1>
    <p>This project is a <strong>Django REST Framework (DRF)</strong> based user authentication system with a <strong>custom user model</strong> using <strong>email as the username</strong>. It supports full user registration, login, profile management, password change, and password reset functionalities. JWT is used for secure authentication.</p>
    
    <h2>🚀 Features</h2>
    <ul>
        <li>✅ Custom User Model with Email as Username</li>
        <li>✅ JWT Authentication with <code>SimpleJWT</code></li>
        <li>✅ Register & Login APIs</li>
        <li>✅ User Profile Endpoint</li>
        <li>✅ Change Password Endpoint</li>
        <li>✅ Send Password Reset Email with Token</li>
        <li>✅ Password Reset via UID & Token</li>
        <li>✅ Email Utility Class</li>
        <li>✅ Token Validations & Expiry Handling</li>
    </ul>

    <h2>📂 Project Structure</h2>
    <pre>
. 
├── account/                             # Account-related app
│   ├── models.py                        # Custom User model
│   ├── serializers.py                   # DRF serializers
│   ├── views.py                         # API views (Class-based)
│   ├── urls.py                          # Routes for the account app
│   └── utils.py                         # Utility functions for email sending
├── djangoauthapiproject/                # Project directory
│   ├── settings.py                      # JWT & Email backend setup
│   └── urls.py                          # Include account.urls
├── manage.py                            # Django's command-line utility
└── README.md                            # Project documentation
    </pre>

    <h2>⚙️ Setup Instructions</h2>
    <div class="setup-instructions">
        <p><strong>1. Clone the Repository</strong></p>
        <pre>git clone https://github.com/yourusername/django-auth-api.git
cd django-auth-api</pre>

        <p><strong>2. Create and Activate Virtual Environment</strong></p>
        <pre>python -m venv venv
source venv/bin/activate   # For Linux/macOS
# OR
venv\Scripts\activate      # For Windows</pre>

        <p><strong>3. Install Dependencies</strong></p>
        <pre>pip install -r requirements.txt</pre>

        <p><strong>4. Apply Migrations</strong></p>
        <pre>python manage.py makemigrations
python manage.py migrate</pre>
    </div>

    <h2>📬 Password Reset Flow</h2>
    <ul>
        <li>User submits their email.</li>
        <li>System generates a unique token + UID.</li>
        <li>Sends a secure password reset link via email.</li>
        <li>User clicks the link → resets password using the token.</li>
    </ul>

    <h2>📫 API Endpoints</h2>
    <table>
        <thead>
            <tr>
                <th>Method</th>
                <th>Endpoint</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>POST</td>
                <td>/api/user/register/</td>
                <td>Register a new user</td>
            </tr>
            <tr>
                <td>POST</td>
                <td>/api/user/login/</td>
                <td>Login user and receive JWT token</td>
            </tr>
            <tr>
                <td>GET</td>
                <td>/api/user/profile/</td>
                <td>Get user profile (JWT protected)</td>
            </tr>
            <tr>
                <td>POST</td>
                <td>/api/user/change-password/</td>
                <td>Change password (JWT protected)</td>
            </tr>
            <tr>
                <td>POST</td>
                <td>/api/user/send-reset-password-email/</td>
                <td>Send password reset email</td>
            </tr>
            <tr>
                <td>POST</td>
                <td>/api/user/reset-password/&lt;uidb64&gt;/&lt;token&gt;/</td>
                <td>Reset password using token</td>
            </tr>
        </tbody>
    </table>

    <div class="todo">
        <h3>📌 Todo</h3>
        <ul>
            <li>Add Swagger or ReDoc API documentation</li>
            <li>Add unit tests</li>
            <li>Dockerize the project</li>
            <li>Add frontend integration</li>
        </ul>
    </div>
</body>
</html>
