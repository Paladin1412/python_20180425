// cgi_get.c
// test for cgi get
#include <stdio.h>
#include <stdlib.h>
extern char **environ; // 调用linux系统环境变量,environ是一个全局的外部变量，所以切记使用前要用extern关键字进行声明，然后在使用

int main()
{
		char MimeType[]="text/html";
		fprintf(stdout, "Content-type: %s\r\n\r\n", MimeType); //输出响应头，响应头之后要加两个"\r\n"
		fprintf(stdout, "<html><head><title>CGI小程序</title></head><body>\n");

		char **env;

		// 循环输出系统环境变量
		for(env = environ; *env != NULL; env++)
		{
				fprintf(stdout, "%s<br>\n", *env);
		}

		char *query_string = getenv("QUERY_STRING"); // 获取cgi环境变量QUERY_STRING,也就是GET参数
		fprintf(stdout, "-------<br>query_string: %s<br>-------<br>", query_string);
		fprintf(stdout, "</body></html>\n");
		
		return 0;
}
