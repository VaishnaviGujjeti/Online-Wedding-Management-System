# Online-Wedding-Management-System
## Features
- Browse wedding service categories (e.g., venues, catering) via `/categories/`.
- View services for a specific category (e.g., `/categories/1/` for category ID 1).
- Filter services by city (e.g., Mumbai, Delhi).
- Book services with date selection (requires login; shows a "Please Log In" modal for unauthenticated users on the booking page and hides it after login; pre-selects the service when clicking "Book Now"; only accepts dates at least 7 days in the future (e.g., on May 15, 2025, the earliest date is May 22, 2025); shows a "Confirmed Booking" modal pop-up and a success message on the home page after booking; validates event date selection; JavaScript for modal and date validation moved to script.js and optimized).
- Submit inquiries via a contact form (validates email address client-side).
- User authentication (login/register).
- Responsive design with Bootstrap.

## Development Notes
- To avoid "Page Not Found" errors, ensure URL names in templates match `urls.py`, test URLs individually, enable `DEBUG = True`, and apply migrations promptly.
- To debug modal issues, check authentication status with `{{ user.is_authenticated }}`, verify Bootstrap JS is loaded, and use console logs in `script.js` to confirm modal triggering.
- Ensure `{% load static %}` is included in templates using `{% static %}` tags, even in parent templates like `base.html`.
- Added Bootstrap to static files (`static/bootstrap/`) and updated `base.html` to use local files instead of CDN for reliability.
- Added `request.session.flush()` in `logout_view` to ensure proper logout and session clearing.
- Added form error display in `booking.html` and debug logs in `booking` view to troubleshoot form submission issues.
- Added a "Confirmed Booking" modal pop-up on the home page using Bootstrap, triggered via `script.js` when `booking_confirmed=true` is in the URL.
- Fixed `TemplateSyntaxError` in `home.html` by removing duplicate `{% extends %}` and `{% block content %}` tags (reapplied fix due to file reversion).
- Updated `home.html` to replace Bootstrap 4 `jumbotron` with Bootstrap 5-compatible styling (`container`, `py-5`, `lead`, `btn-lg`).
