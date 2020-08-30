/*******************************************************************************/
/*                                                                             */
/* Project      : my_scheduler                                                 */
/* File         : schedule.h                                                   */
/* Author       : Kim yu_mi (raspberi.kim@gmail.com)                           */
/* Company      : Dankook Univ. Embedded System Lab.                           */
/* Notes        : header file source for my_scheduler	     		       */
/* Date         : 2008/07/05                                                   */
/*                                                                             */
/*******************************************************************************/

#ifndef SCHEDULER_H
#define SCHEDULER_H

#define THREAD_STACKSIZE 1024

// task�� ����
typedef enum  {
	TASK_READY = 0,
	TASK_RUN,
	TASK_YIELD,
	TASK_SLEEP,
	TASK_KILL
}TaskStatus;

// �� task�� ���� ����ü
typedef struct task_info_tag {
	unsigned long stack[THREAD_STACKSIZE];
	unsigned long sp;

	int task_id;

	TaskStatus status;

	struct task_info_tag *next;
	struct task_info_tag *prev;
}*TaskInfo;

typedef void (*TaskFunc)(void *context);

TaskInfo thread_create(TaskFunc callback, void *context);

void thread_init(void);
void thread_wait(void);
void thread_uninit(void);
void thread_switch(void);
void thread_kill(void);

#endif

