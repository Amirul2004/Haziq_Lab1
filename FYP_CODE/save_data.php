<?php
// Database connection settings
$host = "localhost";
$dbname = "fyp_db";  // Change this to your actual database name
$username = "FYP_user";      // Change this to your database username
$password = "admin123";  // Change this to your database password

// Connect to MySQL
$conn = new mysqli($host, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Read JSON input from Python
$data = json_decode(file_get_contents("php://input"), true);

// Check if data is received
if (isset($data["risk_label"]) && isset($data["risk_level"])) {
    $risk_label = $data["risk_label"];
    $risk_level = (int)$data["risk_level"];

    // Insert data into your table (change `scan_results` to your actual table name)
    $sql = "INSERT INTO scan_results (risk_label, risk_level) VALUES (?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("si", $risk_label, $risk_level);

    if ($stmt->execute()) {
        echo "✅ Data successfully saved to the database!";
    } else {
        echo "❌ Error: " . $stmt->error;
    }

    $stmt->close();
} else {
    echo "❌ Invalid data received.";
}

// Close connection
$conn->close();
?>
