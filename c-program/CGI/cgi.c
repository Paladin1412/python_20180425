#include <stdio.h>

int main()
{
	char MimeType[]="text/html";
	fprintf(stdout, "Content-type: %s\r\n\r\n", MimeType);
	fprintf(stdout, "<html><head><title>CGI小程序</title></head>\n");
	fprintf(stdout, "<body>由C编写的CGI小程序</body></html>\n");

	return 0;
}
