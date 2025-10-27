<?php
session_start();
require_once 'confit.php';

if (isset($_POST['register'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = password_hash($_POST['password'],PASSWORD_DEFAULT);
    $role = $_POST['role'];

    $checkEmail = $conn->guery("SELECT email FROM user WHERE email = '$email'");
    if ($checkEmail->num_rows>0){
        $_SESSION['register_eroor'] = 'Email is already registerd!';
        $_SESSION['active_form'] = 'register';
    }else{
        $conn->query("INSERT INTO user (name, email, password, role) VAKUES ('$name', '$email', '$password', '$role')");

    }
    header("Location:Admun.php");
    exit();

}
if (isset($_POST['login'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];
    
    $result =  $conn ->query("SELECT * FROM user WHERE eamil = '$email' ");
    if ($result->num_rows>0){
        $user = $result->fetch_assoc();
        if (password_verify($password, $user['password'])){
            $_SESSION["name"] = $user['name'];
            $_SESSION["email"] = $user['eamil'];

            if($user['role'] == 'admin') {
                header("Location: admin_page.php");
            }else{
                header("Location: user_page.php");
            }
            exit();

        }
    }
    $_SEEIOPN['login_error'] = 'Incorrect email or password';
    $_SEEIOPN['active_form'] = 'login';
    header("Location: Admun.php");
    exit();
}


?>