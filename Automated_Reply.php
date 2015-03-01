<?php
header('Content-Type: text/html');
?>
<Response>
  <Message>Thank you your message, I'll get back to you as soon as possible</Message>
  <Message to="<?=$_REQUEST['PhoneNumber']?>">
<?=htmlspecialchars(substr($_REQUEST['From'] . ": " . $_REQUEST['Body'], 0, 160))?>
  </Message>
</Response>

