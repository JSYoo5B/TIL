/*
 * File 	: syscall_hook.c
 * Author	: Seungjae Baek (baeksj@dankook.ac.kr)
 * Company  	: Dankook Univ. Embedded System Lab.
 */

#include <linux/kernel.h>
#include <linux/module.h>
#include <asm/unistd.h>
#include <linux/syscalls.h>
#include <linux/hugetlb.h>

unsigned long **sys_call_table;
unsigned long **locate_sys_call_table(void)
{
	unsigned long temp;
	unsigned long *p;
	unsigned long **sys_table;

	for ( temp = 0xffffffff81000000; temp < 0xffffffffa1000000; temp+= sizeof(void*)){
		p = (unsigned long *)temp;
		if( p[__NR_close] == (unsigned long)sys_close){
			sys_table = (unsigned long **)p;
			return &sys_table[0];
		}
	}
	return NULL;
}

asmlinkage long (*original_call)(const char __user *, int, umode_t);
asmlinkage long sys_our_open(const char __user *filename, int flags, umode_t mode){
	printk("<0>[PID:%ld][%s] open [%s]\n", current->pid, current->comm, filename);
	return (original_call(filename, flags, mode));
}

int syscall_hooking_init(void)
{
	unsigned long cr0;

	if( (sys_call_table = locate_sys_call_table()) == NULL){
		printk("<0> Can't find sys_call_table\n");
		return -1;
	}
	printk("<0> sys_call_table is at [%p]\n", sys_call_table);

	cr0 = read_cr0();
	write_cr0(cr0 & ~0x00010000);
	set_memory_rw(PAGE_ALIGN((unsigned long )sys_call_table) - PAGE_SIZE, 3);

	original_call = (void *)sys_call_table[__NR_open];
	sys_call_table[__NR_open] = (void *)sys_our_open;

	write_cr0(cr0);
	
	printk("<0> Hooking done!\n");
	return 0;
}

void syscall_hooking_cleanup(void)
{
	unsigned long cr0 = read_cr0();
	write_cr0(cr0 & ~0x00010000);

	sys_call_table[__NR_open] = original_call;
	write_cr0(cr0);
	printk("<0> Module cleanup\n");
}

module_init(syscall_hooking_init);
module_exit(syscall_hooking_cleanup);
MODULE_LICENSE("GPL");
