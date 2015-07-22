/* mat.cpp */
#include <opencv2/opencv.hpp>

int main()
{
    int height = 350;
    int width = 480;
    cv::Mat image(height, width, CV_8UC1);
    cv::imshow("image", image);
    cv::waitKey(0);
}
