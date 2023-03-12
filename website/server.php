<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $username = file_get_contents('php://input');
  file_put_contents('user_input.txt', $username);
  $password = file_get_contents('php://input');
  file_put_contents('user_input.txt', $password);
}

?>