# Flask — Compact Guide for Developers & Interviews

This README summarizes the essential Flask concepts, patterns, and interview-focused points. Use it as a quick reference for building small apps and answering common interview questions.

## Quick Overview
- **What is Flask?** A lightweight WSGI web framework built on Werkzeug (HTTP utilities) and Jinja2 (templating).
- **When to use?** Great for APIs, microservices, prototypes, and apps where you want explicit control over components.

## Core Concepts (You Should Know)
- **Application (`Flask`)**: The central WSGI app. Create with `app = Flask(__name__)`.
- **Routing**: `@app.route('/path')` maps URLs to view functions. Routes can include variable rules like `<int:id>`.
- **Request Context**: `request` is a context-local proxy that exposes incoming request data.
- **Response**: View functions return strings, tuples `(body, status)`, Response objects, or `render_template(...)` output.
- **Templates**: Use Jinja2 with `render_template('file.html', **context)` for separation of presentation and logic.
- **Static Files**: Serve from `static/` or use `url_for('static', filename='...')` to reference them.
- **URL Building**: `url_for('endpoint', **params)` builds URLs by endpoint name (avoid hardcoding paths).
- **Redirects**: `redirect(url_for(...))` issues an HTTP redirect response.
- **HTTP Methods**: Use `methods=['GET','POST','PUT','DELETE']` on routes to accept specific verbs.

## Useful Flask Patterns
- **Application Factory**: Create app in a function (`def create_app(config=None):`) and initialize extensions inside it — useful for testing and multiple configs.
- **Blueprints**: Modularize large apps by grouping related routes and templates into blueprints.
- **Config Management**: Use `app.config.from_object()` / `from_envvar()` or environment variables for different environments.

## Request & Response Details (Interview Bits)
- **`request` proxy**: Access form data (`request.form`), query params (`request.args`), JSON (`request.get_json()`), headers and files.
- **`g` and `current_app`**: `g` stores request-scoped globals; `current_app` references the app within a request context.
- **Session**: `session` uses signed cookies for lightweight client-side sessions.
- **Error Handling**: Register error handlers with `@app.errorhandler(404)` or `app.register_error_handler`.
- **before_request / after_request**: Hooks to run code before/after a request (authentication, DB connections, cleanup).

## Jinja2 Quick Notes
- `{{ var }}` prints a value.
- `{% if %}` / `{% for %}` handles logic and loops.
- Block inheritance: `{% extends 'base.html' %}` and define `{% block content %}` in children.
- Autoescaping is enabled by default for HTML templates (helps prevent XSS).

## Building REST APIs
- Use `jsonify()` to return JSON responses with the correct MIME type.
- Use proper HTTP status codes (200, 201, 204, 400, 404, 500).
- For larger APIs, consider Flask-RESTful or Flask-Smorest for schema validation and resource routing.

## Extensions You Should Know
- `Flask-SQLAlchemy` — ORM integration.
- `Flask-Migrate` — Alembic migrations.
- `Flask-Login` — Authentication helpers.
- `Flask-WTF` — Forms and CSRF protection.
- `Flask-CORS` — Cross-origin resource sharing.

## Deployment & Production
- Don't use `app.run()` for production. Use a WSGI server like `gunicorn` or `uWSGI`.
- Configure logging, reverse proxy (nginx), and environment-specific configs.
- Use `Flask`'s `PRODUCTION` vs `DEBUG` settings carefully — never enable debugger in production.

## Testing
- Use `app.test_client()` to make requests to your app in unit tests.
- Use the application factory pattern to create isolated app instances for tests.

## Common Interview Questions (short answers)
- Q: How does Flask routing work? — A: `@app.route` registers a function as the endpoint for a URL and HTTP methods.
- Q: What is `app` vs `current_app`? — A: `app` is the Flask instance you create; `current_app` is a proxy usable inside request contexts to refer to the active app.
- Q: How to store user sessions? — A: Use Flask's `session` (signed cookies) or server-side stores via extensions.
- Q: How to serve static files? — A: Place them in `static/` and use `url_for('static', filename=...)`.
- Q: What is a Blueprint? — A: A modular collection of routes/templates/static files you register on an app; great for organizing large apps.

## Quick Commands
- Create virtualenv and install Flask:

```
python -m venv env
env\Scripts\activate
pip install flask
```

- Run app for development:

```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

## Where to Learn More
- Official docs: https://flask.palletsprojects.com/
- Flask Mega-Tutorial by Miguel Grinberg (for full-app patterns)

---