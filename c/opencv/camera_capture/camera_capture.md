# C+OpenCVでカメラキャプチャ
## 目標
C言語でOpenCVライブラリを用いて、ビデオキャプチャを行う。

## 準備
### 環境
* MacOSX Marvericks(10.9)
* Homebrew

### インストール
```bash
brew install opencv
```

## 使い方
### ヘッダーファイル
```c
#include <cv.h>
#include <ctype.h>
#include <highgui.h>
```

### コンパイル
```bash
gcc ${filename} `pkg-config opencv --cflags` `pkg-config opencv --libs`
```

${filename}の位置にコンパイルしたいファイル名を入力するとa.outという実行ファイルができる。
実行する場合は以下で実行できる。

```bash
./a.out
```

## 使用例
### カメラキャプチャ
```c:camera_capture.c
#include <cv.h>
#include <ctype.h>
#include <highgui.h>

int main() {
    int c = 0; // キーボード入力用
    CvCapture *capture=0; // カメラキャプチャ用
    IplImage *frame=0; // キャプチャ画像用

    // カメラキャプチャ取得用
    capture = cvCreateCameraCapture(0);

    // キャプチャ画像を表示するためのウィンドウを作成
    cvNamedWindow("Capture", CV_WINDOW_AUTOSIZE);

    while (1) {
        // キャプチャ画像を取得
        frame = cvQueryFrame(capture);

        // 取得したキャプチャ画像を表示
        cvShowImage("Capture", frame);

        // キーボード入力を待つ
        c = cvWaitKey (2);
        if (c == '\x1b') { // Escキー
            break;
        }
    }
}
```

## ソースコードなど
https://github.com/greeeenkew/c-opencv/tree/master/camera_capture
