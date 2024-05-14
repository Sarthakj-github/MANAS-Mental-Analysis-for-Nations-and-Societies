<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $recipient = "jainsarthak97162@gmail.com";
    $subject = "Form Submission";
    $name = $_POST['name'];
    $phone = $_POST['phone'];
    $email = $_POST['email'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];
    
    // Compose the email message
    $email_message = "Name: $name\n";
    $email_message .= "Phone: $phone\n";
    $email_message .= "Email: $email\n";
    $email_message .= "Subject: $subject\n\n";
    $email_message .= "Message:\n$message";
    
    // Email headers
    $headers = "From: $email";

    // Send email
    if (mail($recipient, $subject, $email_message, $headers)) {
        echo "Thank you! Your message has been sent.";
    } else {
        echo "Oops! Something went wrong and we couldn't send your message.";
    }
}
?>
