all: gray_scale
CVFLAGS = `pkg-config opencv --cflags` `pkg-config opencv --libs`

gray_scale: gray_scale.c
	gcc -o $@ $< ${CVFLAGS}
