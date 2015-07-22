# C+OpenCVでグレースケール変換

## 目標
C言語でOpenCVライブラリを用いて、
["C+OpenCVでビデオキャプチャ"](http://qiita.com/greeeenkew/items/2a62d431e0f69bfed15f#2-2)で
取得したキャプチャ画像にエフェクトを付加する。

## 準備・基本的な使い方など
参考: ["C+OpenCVでビデオキャプチャ"](http://qiita.com/greeeenkew/items/2a62d431e0f69bfed15f#2-2)

## グレースケール変換
```c
IplImage* gray_scale(IplImage *frame) {
    IplImage *src_gray = 0; // 変換用

    // 画像と同じ大きさのメモリを確保する
    src_gray = cvCreateImage(cvSize(frame->width, frame->height), IPL_DEPTH_8U, 1);

    IplImage* detect_frame = cvCreateImage(cvSize((frame->width / SCALE), (frame->height / SCALE)), IPL_DEPTH_8U, 1);
    cvCvtColor(frame, src_gray, CV_BGR2GRAY);
    cvResize(src_gray, detect_frame, CV_INTER_LINEAR);
    cvEqualizeHist(src_gray, src_gray);
    cvReleaseImage(&detect_frame);
    return src_gray;
}
```

## ソース
