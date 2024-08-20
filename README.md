# AMS Database Management

This repository manages the PostgreSQL database for the AMS (Appointment Management System) project. It includes the database schema, migration scripts, and related Python code for database interactions.


## Initial Folder Structure

```
AMS-DATABASE-MANAGEMENT/
├── alembic/                   # Alembic migration folder
│   ├── versions/              # Database migration scripts
│   ├── alembic.ini            # Alembic configuration file
│   ├── env.py                 # Alembic environment configuration
│   ├── script.py.mako         # Mako template for Alembic scripts
│   └── README.md              # Documentation for using Alembic
├── config/                    # Configuration files
│   └── database_config.py     # Database configuration settings
├── connections/               # Database connection management
│   └── init_db.py             # Script to initialize database connection
├── db/                        # Database scripts and helpers
│   └── database.py            # Core database interaction logic
├── models/                    # ORM models
│   └── user.py                # Example user model
├── utils/                     # Utility functions
│   └── converters.py          # Helper functions (e.g., int to datetime converter)
├── .gitignore                 # Files and directories to ignore in git
├── README.md                  # Project documentation (this file)
```

## Setup and Installation

### Prerequisites

- **Python 3.8+**
- **PostgreSQL**

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd AMS-DATABASE-MANAGEMENT
   ```

2. **Set up the virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database connection:**

   Modify the `sqlalchemy.url` in `alembic/alembic.ini` to point to your PostgreSQL instance.



5. **Generate the migration:**

   ```bash
   alembic revision --autogenerate -m "Describe your change"
   ```


6. **Apply the migration::**

   ```bash
   alembic upgrade head
   ```


7. **downgrade the migration::**

   ```bash
   alembic downgrade base
   ```


