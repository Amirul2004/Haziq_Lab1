import requests
import time
import logging
import json
import tkinter as tk
from tkinter import Label

# Set up logging
logging.basicConfig(filename="sql_injection_test.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Ask user to enter a target website URL
target_url = input("Enter the target URL: ").strip()
php_url = "http://localhost/save_data.php"  # Ensure this matches your actual PHP file path

# Function to handle retries in case of timeouts or server failures
def make_request(url, data, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.post(url, data=data, timeout=10)
            return response
        except requests.exceptions.Timeout:
            logging.warning(f"Timeout error on attempt {attempt + 1}. Retrying in {delay} seconds...")
            time.sleep(delay)
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            break
    return None

# Function to check responses and assign risk level
def classify_risk(response_text, test_type):
    if not response_text:
        return False
    
    if test_type == "Boolean-Based":
        if "Welcome" in response_text or "Dashboard" in response_text:
            return True  # Vulnerable
        return False

    elif test_type == "Classic":
        sql_errors = ["SQL syntax", "mysql_fetch", "MySQL server version", "You have an error in your SQL syntax"]
        if any(error in response_text for error in sql_errors):
            return True  # Vulnerable
        return False
    
    return False

# Boolean-Based SQL Injection Test
def test_boolean_based_injection():
    logging.info("\n🔍 Testing Boolean-Based SQL Injection...")
    payloads = ["' OR 1=1 --", "' OR 1=2 --"]
    
    for payload in payloads:
        response = make_request(target_url, data={"username": payload, "password": "password"})
        if response and classify_risk(response.text, "Boolean-Based"):
            return True  
    return False

# Classic (Error-Based) SQL Injection Test
def test_classic_injection():
    logging.info("\n🔍 Testing Classic SQL Injection (Error-Based)...")
    classic_payload = "'"
    
    response = make_request(target_url, data={"username": classic_payload, "password": "password"})
    if response and classify_risk(response.text, "Classic"):
        return True  
    return False

# Function to determine overall risk level
def calculate_risk():
    found_boolean = test_boolean_based_injection()
    found_classic = test_classic_injection()

    if found_classic and found_boolean:
        return "HIGH RISK", 3, found_classic, found_boolean
    elif found_classic:
        return "MEDIUM RISK", 2, found_classic, found_boolean
    elif found_boolean:
        return "LOW RISK", 1, found_classic, found_boolean
    return "SECURE", 0, found_classic, found_boolean

# Function to send results to the database
def send_to_database(url, risk_label, risk_level):
    data = {
        "risk_label": risk_label,
        "risk_level": risk_level
    }
    
    try:
        response = requests.post(php_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            print("✅ Data successfully sent to the database!")
        else:
            print(f"❌ Failed to send data. Server response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

# GUI to Display Results
def show_results():
    risk_label, risk_level, classic_sql, boolean_sql = calculate_risk()
    
    # Send results to the database
    send_to_database(php_url, risk_label, risk_level)

    # Create a new window
    window = tk.Tk()
    window.title("SQL Injection Test Summary")
    window.geometry("600x500")
    window.configure(bg="#1E1E1E")  

    # Risk Level Display
    color_map = {3: "red", 2: "orange", 1: "yellow", 0: "green"}
    risk_display = Label(window, text=risk_label, font=("Arial", 18, "bold"), fg=color_map[risk_level], bg="#1E1E1E")
    risk_display.pack(pady=20)

    # Additional Info
    tests_summary = f"""
    ✅ Tests Completed: 2/2
    - Classic SQL Injection: {"✔️ Found" if classic_sql else "❌ Not Found"}
    - Boolean-Based SQL Injection: {"✔️ Found" if boolean_sql else "❌ Not Found"}
    """
    summary_label = Label(window, text=tests_summary, font=("Arial", 12), fg="white", bg="#1E1E1E", justify="left")
    summary_label.pack(pady=10)

    window.mainloop()

# Run the tests and show results
if __name__ == "__main__":
    time.sleep(2)
    show_results()
