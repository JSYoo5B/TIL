/*******************************************************************************/
/*                                                                             */
/* Project      : my_scheduler                                                 */
/* File         : schedule.c                                                   */
/* Author       : Kim yu_mi (raspberi.kim@gmail.com)                           */
/* Company      : Dankook Univ. Embedded System Lab.                           */
/* Notes        : inner function source for my_scheduler		       */
/*                my_scheduler�� �������� ����κ����� �����ٷ��Դϴ�.     */
/*		  schedule.c������ main�Լ����� ���ǵ� �Լ�����                */
/*                �����ٸ��� ���� ���ε����� �����߽��ϴ�.                     */
/* Date         : 2008/07/05                                                   */
/*                                                                             */
/*******************************************************************************/

#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <setjmp.h>
#include <malloc.h>
#include <memory.h>
#include <sys/time.h>
#include "schedule.h"

// task switching�� ����Ǿ�� �ϴ� ����
struct frame {			
	unsigned long flags;
	unsigned long ebp;
	unsigned long edi;
	unsigned long esi;
	unsigned long edx;
	unsigned long ecx;
	unsigned long ebx;
	unsigned long eax;
	unsigned long retaddr;
	unsigned long retaddr2;
	unsigned long data;
};

typedef struct sch_handle_tag
{
	int child_task;

	TaskInfo running_task;
	TaskInfo root_task;
}SchHandle;

// global schedule handler
SchHandle gh_sch;

// task data struct
TaskInfo  task_get_runningtask();
void task_insert(TaskInfo taskinfo);
void task_delete(TaskInfo taskinfo);
void task_next();
void scheduler();
void parent_task();

/* thread_create : task�� �����ϴ� �Լ��� taskinfo ����ü�� �Ҵ��ϰ� �����Ѵ�. */
TaskInfo thread_create(TaskFunc callback, void *context)
{
	TaskInfo taskinfo;
	// task�� ���� ���� �Ҵ�
	taskinfo = malloc(sizeof(*taskinfo));
	memset(taskinfo, 0x00, sizeof(*taskinfo));

	{
		struct frame *f = (struct frame *)&taskinfo->stack[THREAD_STACKSIZE - sizeof(struct frame)/4];
		// taskinfo�� �Ҵ�� ���� �� stack�κ� ���ʿ� frame�� ���� �������� �Ҵ�
		// �̿� task�� ����Ǹ鼭 stack������ Ȱ��
		int i;
		for(i = 0; i < THREAD_STACKSIZE; ++i) {	// stack overflow check
			taskinfo->stack[i] = i;
		}
		memset(f, 0, sizeof(struct frame));
		f->retaddr = (unsigned long)callback;
		f->retaddr2 = (unsigned long)thread_kill;
		f->data    = (unsigned long)context;
		taskinfo->sp      = (unsigned long)&f->flags;
		f->ebp     = (unsigned long)&f->eax;
	}
	// task ������ ���� gh_sch�� child task�� �þ����� ǥ��
	gh_sch.child_task ++;
	// gh_sch.child_task ������ task_id �Ҵ�
	taskinfo->task_id = gh_sch.child_task;		
	// task ������ TASK_READY�� ���¸� ������
	taskinfo->status = TASK_READY;				
	// taskinfo����ü���� linkedlist�� �� thread�� taskinfo ����ü�� ����
	task_insert(taskinfo);	

	return taskinfo;
}

/* thread_init : �ʱ�ȭ �Լ��� main�Լ��� ó���� ȣ���Ͽ�, */
/* global scheduler handeler�� �ʱ�ȭ�ϰ�, parent_task�� �����Ѵ�. */
void thread_init()
{

	gh_sch.root_task = NULL;
	gh_sch.running_task = NULL;

	gh_sch.child_task = 0;

	thread_create(parent_task, NULL);
}

/* thread_switch : �������̴� task�� �ٸ� ������� task���� cpu����� �纸�ϰ� �ϴ� �Լ���,
   ���� cpu���������� ���� �������̴� task�� stack�κп� �������� ����ǰ� �Ǹ�,
   ������ ����� ������ ���õ� task�� taskinfo�� stack������ �������ͷ� �÷�����.*/
static unsigned long spsave, sptmp;
void thread_switch()
{
	asm(    "push %%rax\n\t"
		"push %%rbx\n\t"
		"push %%rcx\n\t"
		"push %%rdx\n\t"
		"push %%rsi\n\t"
		"push %%rdi\n\t"
		"push %%rbp\n\t"
		"push %%rbp\n\t"
		"mov %%rsp, %0" 
		: "=r" (spsave) 
	);

	gh_sch.running_task->sp = spsave;

	scheduler();	
	sptmp = gh_sch.running_task->sp;

	asm(	"mov %0, %%rsp\n\t" 
		"pop %%rbp\n\t"
		"pop %%rbp\n\t"
		"pop %%rdi\n\t"
		"pop %%rsi\n\t"
		"pop %%rdx\n\t"
		"pop %%rcx\n\t"
		"pop %%rbx\n\t"
		"pop %%rax\n\t"
		::"r" (sptmp)
	);
}

// ���� ����� task�� �����ϴ� �Լ�
void scheduler(void)		
{
	TaskInfo task;
	// gh_sch�� running_task�� ����Ű�� �ִ� taskinfo ����
	task = task_get_runningtask();

	switch ( task->status ) {		
		// task���°� TASK_RUN�̳� TASK_SLEEP�̸� ���õ�
		case TASK_RUN:
		case TASK_SLEEP:
			break;
		// task���°� TASK_KILL�̸� delete�ϰ�, swiching�Լ� �ٽ� ȣ��
		case TASK_KILL:	
			task_delete(task);
			scheduler();
			break;
		// task���°� TASK_YIELD�̸� ���¸� TASK_RUN���� �ٲٰ� ���õ�
		case TASK_YIELD:
			task->status = TASK_RUN;
			break;
		// task���°� TASK_READY�̸� ���׸� TASK_RUN���� �ٲٰ� ���õ�
		case TASK_READY:
			task->status = TASK_RUN;
			break;
	}
	// gh_sch�� running_task�� linkedlist�� ���� task�� ����
	task_next();
}

void thread_wait(void)
{
	parent_task(NULL);
}

// task ���¸� TASK_KILL�� ���� ��, thread_yield
void thread_kill(void)
{
	TaskInfo task;
	task = task_get_runningtask();
	task->status = TASK_KILL;
	thread_switch();
}

void thread_uninit(void)
{
	return;
}

// child thread�� ���̻� ���������� thread_switch
void parent_task(void *context)
{
	// signal ó���� ���� ������ ���� ����ü
	struct sigaction act;
	sigset_t masksets;
	pid_t pid;

	// signal set �ʱ�ȭ
	sigemptyset( &masksets );
	// signal handler�� thread_switch() ���
	act.sa_handler = thread_switch;
	act.sa_mask = masksets;
	act.sa_flags = SA_NODEFER;

	// signal ���� �� ���� action ����
	sigaction( SIGUSR1, &act, NULL );
	
	if( ( pid = fork() ) ==  0 ) {
		while(1) {
			sleep(1);
			kill( getppid(), SIGUSR1 );
		}
	} else{
		while (1) {
			// child_task�� 1�� ������ ��, ��, parent_task�� ������ ��
			if ( gh_sch.child_task == 1 ){
				kill( pid, SIGINT );
				break;
			}
		};
	}
}
// linkedlist�� ���ο� taskinfo ����
void task_insert(TaskInfo taskinfo)	
{
	if ( gh_sch.root_task == NULL ) {
		gh_sch.root_task = taskinfo;
		gh_sch.running_task = taskinfo;
	} else {
		TaskInfo temp;
		temp = gh_sch.root_task;
		while ( temp->next != NULL ) {
			temp = temp->next;
		}
		temp->next = taskinfo;
		taskinfo->prev = temp;
	}
}

// linkedlist���� gh_sch.running_task�� ����Ű�� �ִ� task ����
TaskInfo task_get_runningtask(void)		
{
	return gh_sch.running_task;
}

// linkedlist���� gh_sch.running_task�� ����Ű�� �ִ� task�� ���� task ����
void task_next(void)	
{
	TaskInfo temp;
	temp = gh_sch.running_task;
	// gh_sch.running_task�� null�� �ƴϸ�
	if ( temp->next != NULL ) {	
		gh_sch.running_task = temp->next;
	}
	// gh_sch.running_task�� null�̸�, parent task�� ����Ŵ
	else {
		gh_sch.running_task = gh_sch.root_task;
	}
}

// linkedlist���� task�� ����
void task_delete(TaskInfo taskinfo)
{
	TaskInfo temp = taskinfo->prev;
	if ( gh_sch.root_task == taskinfo ) {
		gh_sch.root_task = NULL;
		gh_sch.running_task = NULL;
		gh_sch.child_task = 0;
	} else {
		temp->next = taskinfo->next;

		if ( taskinfo == gh_sch.running_task ) {
			if ( temp->next != NULL ) {
				(taskinfo->next)->prev = temp;
				gh_sch.running_task = temp->next;
			} else 
				gh_sch.running_task = temp;
		} 
		gh_sch.child_task--;
	}
	free(taskinfo);
}
