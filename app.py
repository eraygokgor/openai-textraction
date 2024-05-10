import subprocess
import sqlite3

sqlite3.connect('database.db')

def streamlit_app_runner(filename='ui.py'):
    subprocess.run(['streamlit', 'run', filename])
# if __name__ == '__main__':
    # streamlit_app_runner()
