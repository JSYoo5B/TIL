O_TARGET	:= file_write_in_module.ko
obj-m		:= file_write_in_module.o

KERNEL_DIR	:= /lib/modules/$(shell uname -r)/build
PWD		:= $(shell pwd)

default :
	$(MAKE)   -C   $(KERNEL_DIR)   SUBDIRS=$(PWD)   modules

clean :
	$(MAKE)   -C   $(KERNEL_DIR)   SUBDIRS=$(PWD)   clean

