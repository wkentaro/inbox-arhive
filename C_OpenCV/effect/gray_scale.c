/*
 * Author:    Kentaro Wada
 * Mail:      www.kentaro.wada@gmail.com
 * URL:       http://wkentaro.com
 * Created:   2014-07-01
 * Filename:  gray_scale.c
 */
#include <cv.h>
#include <ctype.h>
#include <highgui.h>

IplImage* gray_scale(IplImage *frame) {
    IplImage *src_gray = 0; // 変換用

    // 画像と同じ大きさのメモリを確保する
    src_gray = cvCreateImage(cvSize(frame->width, frame->height), IPL_DEPTH_8U, 1);

    IplImage* detect_frame = cvCreateImage(cvSize((frame->width), (frame->height)), IPL_DEPTH_8U, 1);
    cvCvtColor(frame, src_gray, CV_BGR2GRAY);
    cvResize(src_gray, detect_frame, CV_INTER_LINEAR);
    cvEqualizeHist(src_gray, src_gray);
    cvReleaseImage(&detect_frame);
    return src_gray;
}

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
