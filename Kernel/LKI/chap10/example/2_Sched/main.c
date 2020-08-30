/*******************************************************************************/
/*                                                                             */
/* Project      : my_scheduler                                                 */
/* File         : main.c                                                       */
/* Author       : Kim yu_mi (raspberi.kim@gmail.com)                           */
/* Company      : Dankook Univ. Embedded System Lab.                           */
/* Notes        : main function source for my_scheduler			       */
/*                my_scheduler�� �������� ����κ����� �����ٷ��Դϴ�.     */
/*		  main.c������ �����ٸ� �� 3������ �ٸ� �Լ��� �����մϴ�.     */
/* Date         : 2008/07/05                                                   */
/*                                                                             */
/*******************************************************************************/

#include <unistd.h>
#include <stdio.h>
#include "schedule.h"

// �����ٸ� ����� �Ǵ� �½�ũ
void test_func_one(void* context)
{
	int i = 0;
	while (1) 
	{
		i++;
		printf("TASK 1 : %5d\n", i);
		sleep(1);
		if ( i == 15 ){
			break;
		}
	}
}

void test_func_two(void* context)
{
	int i = 500;
	while (1) 
	{
		i = i+10;
		printf("\t\t\tTASK 2 : %3d\n", i);
		sleep(1);
		if ( i == 600 ){
			break;
		}
	}
}

void test_func_three(void* context)
{
	int i = 1000;
	while (1)
	{
		i++;
		printf("\t\t\t\t\t\tTASK 3 : %4d\n", i);

		sleep(1); 
		sleep(1);

		if ( i == 1005){
			break;
		}
	}
}

// my_scheduler�� main �Լ�
int main(void )
{
	thread_init();

	thread_create(test_func_one, NULL);
	thread_create(test_func_two, NULL);
	thread_create(test_func_three, NULL);

	thread_wait();

	return 0;
}

