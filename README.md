# TrackRight

A full-stack bug tracking application built using **Python** and **Flask**.

## 🚀 About the Project
As a QA professional, I spend my days finding and logging bugs in software. I built **TrackRight** to demonstrate my understanding of the full software development lifecycle—from database architecture to the frontend user interface.

This application demonstrates a full **CRUD** (Create, Read, Update, Delete) workflow for managing tickets.

## ✨ Features
* **Dashboard:** A dashboard showing all active tickets.
* **Ticket Management:** Create, read, update, and delete tickets.
* **Priority System:** A logic system to allow severe tickets to be assigned a higher priority (High/Medium/Low).

## ⚙️ How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/Timedanny/trackright.git](https://github.com/Timedanny/trackright.git)
    ```
2.  Navigate to the project folder:
    ```bash
    cd trackright
    ```
3.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```
4.  Install dependencies:
    ```bash
    pip install Flask
    ```
5.  Initialize the database:
    ```bash
    python init_db.py
    ```
6.  Run the application:
    ```bash
    flask run
    ```

## 🧠 Design Patterns
This project follows the **Model-View-Controller (MVC)** pattern:
* **Model:** `schema.sql` defines the data structure.
* **View:** Jinja templates handle the presentation layer.
* **Controller:** `app.py` manages the business logic and routing.