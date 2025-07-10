# Super Market System

## Description
This project is a back-end system for managing a supermarket's product catalog and inventory. It is built around two core database tables that work together to support all operations:

- Product Table: Stores detailed information about each product.

- Inventory Table: Keeps track of stock levels for each product.

The system supports the full workflow - from initializing the database to handling purchase actions — making it a solid foundation for supermarket inventory and sales management.

## Technologies used
- Python
- FastAPI
- MySQL
  
## Features
📋 Product Management
- Add, update, and delete products
- Store details like name, price, category, brand, etc.

📦 Inventory Control
- Track stock levels for each product
- Add or remove quantities from inventory
- Prevent sales of out-of-stock items

🛒 Purchase Flow
- Handle buying actions
- Automatically update inventory after purchase

🗃️ Database Initialization
- Create product and inventory tables
- Easy setup for testing and development

🔐 Data Validation
- Ensure data integrity for product and inventory records

🌐 RESTful API endpoints
- Access and manipulate products and inventory via HTTP requests

## Installing
To run this project, you'll need firstly to copy it. Open the terminal in the folder you want to install the project and then run this line of code in the terminal

    git clone https://github.com/lucabattesini/super-market-system.git

Now, also with the terminal open in the project folder, install the main requirements running this line of code

    pip install requirements.txt

## Running the project
Now you've already intalled all the requirements, you just need to run this code in your terminal to run it

    uvcorn app:app --reload

## Documentation
As the project was made with FastAPI, all the documentation can be accessed by the following steps

- Run the  project
- Open the HTTP adress in your browser (It'll appear in your terminal)
- Add to address a "/docs" in the end

It'll look like this

    http://127.0.0.1:8000/docs
