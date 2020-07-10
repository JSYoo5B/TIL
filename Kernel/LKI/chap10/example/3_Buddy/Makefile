TARGET = buddy

CC = gcc
CFLAGS = -W -Wall
CFLAGS_BIN = -g -W -Wall
OBJECT = main.o list.o buddy.o
LIBS =

.SUFFIXES : .o .c
.c.o :
	$(CC) $(CFLAGS) -c -o $@ $<

all : $(TARGET)

$(TARGET) : $(OBJECT)
	$(CC) $(CFLAGS_BIN) -o $@ $^ $(LIBS)

clean :
	rm -rf *.o $(TARGET)

