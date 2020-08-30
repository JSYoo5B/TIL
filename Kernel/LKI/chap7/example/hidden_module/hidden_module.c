/*
 * File 	: hidden_module.c
 * Author	: Seungjae Baek (baeksj@dankook.ac.kr)
 * Company  	: Dankook Univ. Embedded System Lab.
 */
#include <linux/kernel.h>
#include <linux/module.h>

int hidden_module_init(void)
{
	printk(KERN_EMERG "Hello Module~! I'm in Kernel\n");
	list_del_init(&__this_module.list);
	return 0;
}

void hidden_module_cleanup(void)
{
	printk("<0>Bye Module~!\n");
}

module_init(hidden_module_init);
module_exit(hidden_module_cleanup);

MODULE_LICENSE("GPL");
