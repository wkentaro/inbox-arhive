CC :=gcc
CFLAGS :=`pkg-config opencv --cflags` `pkg-config opencv --libs`
LDFLAGS :=
SOURCES :=$(wildcard *.c)
EXECUTABLE :=$(SOURCES:.c=)
 
all:$(EXECUTABLE)
 
$(EXECUTABLE):$(SOURCES)
	$(CC) $< $(LDFLAGS) $(CFLAGS) -o $@
 
clean:
	rm -rf $(EXECUTABLE)
