# FTDB - File Uploader and Database Explorer

## How to Run

### 1. Clone the Repository:

```bash
git clone https://github.com/dope232/ftdb
```
### Running the Application

    Install Required Packages:

    Navigate to the project directory and install the required packages using the requirements.txt file.

    ```bash
cd ftdb
pip install -r requirements.txt

```

Run the Application:

Execute the ftdb.py file to start the application.

    ```bash
python -m streamlit run --server.headless true ftdb.py


```
### Getting the Database Details 
        Explore your database details by clicking on the corresponding options in the application interface:
           - Server: Right-click on the "Server" in the Object Explorer and select "Properties" to view details.
           - Tables: Navigate to the "Tables" section and right-click on a table to view its properties.
           - Schema: Similarly, navigate to the "Schema" section and right-click to view schema details.

          

           ![image](https://github.com/dope232/ftdb/assets/110282397/1f8e5ace-77e1-4e97-aed5-c81f8bfb5f90)

**Note:** : Ensure that you have PostgreSQL and PgAdmin installed and properly configured. You also  won't be able to retrieve your database password using PgAdmin.

