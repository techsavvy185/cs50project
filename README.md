#  Telephone Directory

A basic project showcasing the integration of Flask (Python), SQL, and HTML/CSS to create a functional telephone directory.

---

##  Video Demo

[Watch here](https://www.youtube.com/watch?v=RHKx3o0N2ac)

---

##  Description

This is a telephone directory that:

* Displays contact details of various people.
* Allows new details to be added using an admin account.
* Uses Bootstrap for styling forms, tables, and interactive elements.
* Enables multiple users to add contacts to the database on the server.
* Can be implemented in an organization's website to manage contact details effectively.

---

##  Technologies Used

* **Flask (Python):** Handles the backend server logic.
* **SQL:** Stores and retrieves contact details.
* **HTML, CSS, Bootstrap:** Used for structuring and styling the web pages.
* **Flask Sessions:** Manages user authentication.
* **Jinja Templating:** Dynamically renders HTML pages.

---

##  Project Functionality

###  Home Page

* The homepage (`index.html`) displays all entries from the database.
* A navigation bar is present on all pages, styled using Bootstrap.
* The login button dynamically changes based on the user's login status.
* The table listing contacts is interactive, responding to mouse hover.

###  Adding Contacts

* Clicking the **Add Contact** button redirects to the `/add` route.
* If a user is not logged in, they are redirected to the login page.
* If logged in, they can fill out a form to add a new contact.
* Data is inserted into the database using SQL queries.

###  User Authentication

* The login page (`login.html`) allows an admin to log in.
* Upon submitting credentials, the backend checks the database for valid users.
* If the login fails, an error message is displayed.
* If successful, the user is redirected to the add contact form.
* The session management system ensures only logged-in users can add data.

###  Logging Out

* The `/logout` route clears session details, logging the user out.
* After logging out, the user is redirected to the homepage.

---

##  Security Measures

* **Session Verification:** Ensures only authorized users can add contacts.
* **Client-Side Form Validation:** Prevents incomplete data entry.
* **Database Querying with Parameterization:** Reduces SQL injection risks.

---

##  Design Choices

* **Responsive Design:** The website adapts to different screen sizes, making it mobile-friendly.
* **Interactive Elements:** Tables highlight rows when hovered over.
* **Consistent Styling:** Bootstrap is used to ensure a professional look and feel.

---

##  Final Thoughts

This project was built as part of my learning experience in CS50x. I appreciate the CS50 team for providing high-quality educational content for free.

Thank you!
