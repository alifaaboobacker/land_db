# land-record-api
# Land Record Search API

A simple Flask-based web service that simulates the core functionality of Landeed.com by allowing users to search land records and download a PDF summary.

---

## Features

- Accepts search queries by Parcel ID, Plot Number, or Owner Name.
- Retrieves matching land record from the database.
- Generates a downloadable PDF containing the land record summary using ReportLab.
- Returns the PDF as a response to the API call.

---

## Technology Stack

- Python 3.x
- Flask (Web framework)
- Flask-SQLAlchemy (ORM for database interaction)
- MySQL (Database)
- ReportLab (PDF generation)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/land-record-api.git
cd land-record-api
```
### 2. Create and activate a virtual environment

```bash
python -m venv venv
```
#### Windows
```bash
venv\Scripts\activate
```
#### macOS/Linux
```bash
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure the database
Create a MySQL database named land_db.

Create the land_records table with the following schema:

```bash
CREATE TABLE land_records (
    id INT PRIMARY KEY AUTO_INCREMENT,
    parcel_id VARCHAR(50),
    plot_number VARCHAR(50),
    owner_name VARCHAR(100),
    area VARCHAR(100),
    location VARCHAR(255),
    registration_date DATE
);
```
Insert sample data for testing:

```bash
INSERT INTO land_records (parcel_id, plot_number, owner_name, area, location, registration_date)
VALUES ('PID123', 'PLT456', 'John Doe', '500 sq ft', 'Kochi, Kerala', '2021-06-15');
```

### 5. Update database URI
In app/__init__.py, update the SQLAlchemy database URI to match your MySQL credentials:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/land_db'

### 6. Run the application
```bash
python run.py
```
The server will start on http://127.0.0.1:5000.

### 7. Test the API
Open a browser or use Postman to test:
```bash
http://127.0.0.1:5000/search?q=John%20Doe
```
A PDF file named land_record.pdf containing the matching record details will be downloaded.