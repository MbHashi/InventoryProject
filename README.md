# Inventory Management System

### Welcome to the Inventory Management System project! This is a web-based application designed to help businesses manage their inventory, sales, purchases, and more. The system is built using Django for the backend and will have a responsive frontend for seamless user experience.

## Current Features

### Backend:
**Django Framework:** The backend is built using Django 5.1, providing a robust and scalable environment.
**Database Integration:** Successfully connected Django to a MariaDB database.
**Models:**
   • *Category:* Represents different categories of items.
   • *Item:* Represents individual items, associated with a category, including fields for quantity and price.

### Frontend:
**Coming Soon!**


## Getting Started

### Prerequisites:
• Python 3.11
• Django 5.1
• MariaDB
• Git
• Docker 

### Setup Instructions
   **1.	Create a virtual environment:**
  ``` 
    git clone git@github.com:MbHashi/InventoryProject.git
    cd InventoryProject
  ```

   **2. Install dependencies:**
   ```
    ip install -r requirements.txt
   ```


   **3.	Set up the database:**
      Ensure that MariaDB is installed and running. Then create the necessary database and user:
**SQL Commands:**
   ```
    CREATE DATABASE inventorydb;
    CREATE USER 'inventory_user'@'localhost' IDENTIFIED BY 'YourPassword';
    GRANT ALL PRIVILEGES ON inventorydb.* TO 'inventory_user'@'localhost';
    FLUSH PRIVILEGES;
   ```


   **4.	Run migration:**
   ```
    python manage.py migrate
   ```


  **5. Start the development server:**
   ```
    python manage.py runserver
   ```


###Deployment

Instructions for deploying this project will be provided once the system is ready for production.
