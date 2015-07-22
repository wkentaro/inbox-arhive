OpenCVのC++コードをMacでmakeする際のMakefile
===

コード
---

```mf
# コンパイラ
CC :=g++
# インクルードファイル等
CFLAGS :=`pkg-config opencv --cflags` `pkg-config opencv --libs`
LDFLAGS :=
# ディレクトリ内の全てのC++ファイルをコンパイル
SOURCES :=$(wildcard *.cpp)
# C++ファイルの.cppをとったものを実行ファイルの名前とする
EXECUTABLE :=$(SOURCES:.cpp=)

all:$(EXECUTABLE)

$(EXECUTABLE):$(SOURCES)
	$(CC) $< $(LDFLAGS) $(CFLAGS) -o $@

clean:
	rm -rf $(EXECUTABLE)
```

使用例
---

```bash
$ ls
Makefile  mat.cpp
$ make
g++ mat.cpp  `pkg-config opencv --cflags` `pkg-config opencv --libs` -o mat
$ ./mat
```
