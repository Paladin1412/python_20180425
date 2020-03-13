#!/usr/bin/env php
<?php
// cgi.php
// 由于php脚本不是可执行文件，这里用shell的方式来执行php脚本

fwrite(STDOUT, "Content-type: text/html\r\n\r\n");
fwrite(STDOUT, "<html><head></head><body><b>PHP编写的CGI程序演示 ". date("Y/m/d H:i:s") ."</b></body></html>\n");
?>
