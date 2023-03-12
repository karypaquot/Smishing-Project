function saveUserInput() {
    var username = document.getElementById("username").nodeValue;
    var password = document.getElementById("password").nodeValue;

  fetch('server.php', {
    method: 'POST',
    body: username, password
  })
  .then(response => {
    if (response.ok) {
      console.log('Data saved successfully');
    } else {
      console.error('Error saving data');
    }
  })
  .catch(error => {
    console.error(error);
  });
}