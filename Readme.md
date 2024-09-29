# Expense Tracker 

A simple command-line expense tracker application built in Python. This application allows users to manage their finances by adding, deleting, and viewing expenses. It also provides summaries of total expenses. This is one of the python project from [roadmap.sh](https://roadmap.sh/projects/expense-tracker).

## Features 

- Add expenses with a description and amount. 
- Update and delete expenses. 
- View all expenses in a tabular format. 
- Get a summary of total expenses. 
- Get a summary of expenses for a specific month. 
- Data is stored in a CSV file for easy access and manipulation.

## Requirements 

- Python 3.x 
- `pandas` library (optional, depending on your future implementation)

## Installation 

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AmirArdalanN/expense-tracker.git   
   cd expense-tracker
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   1. macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

   2. Windows:

      ```bash
      venv\Scripts\activate
      ```

      

4. **Install required packages:**

   ```bash
   pip install pandas  # Include any other packages if needed
   ```

## Usage

Run the application using the command line. Here are some examples of how to use the expense tracker:

- **Add an expense:**

  ```bash
  python expense_tracker.py add --description "Lunch" --amount 20
  ```

- **List all expenses:**

  ```bash
  python expense_tracker.py list
  ```

- **Delete an expense by ID:**

  ```bash
  python expense_tracker.py delete --id 1
  ```

- **Get a summary of all expenses:**

  ```bash
  python expense_tracker.py summary
  ```

- **Get a summary of expenses for a specific month (e.g., August):**

  ```bash
  python expense_tracker.py summary --month 8
  ```

## Data Storage

The application stores expenses in a CSV file located in the `data/` directory. The file is created automatically if it does not exist.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Feel free to submit issues and pull requests. Contributions are welcome!

## Acknowledgements

- [Python](https://www.python.org/) for the programming language.
- [CSV](https://docs.python.org/3/library/csv.html) module for handling CSV file operations.