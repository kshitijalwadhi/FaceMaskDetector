# FaceMaskDetector

## Description
Implemented a python script to detect whether a person is wearing face mask or not using OpenCV and Keras/TensorFlow.

## Directory layout
```go
 FaceMaskDetector
    +--- dataset
        +--- with_mask
            |
        +--- without_mask
            |
    +--- face_detector // pre trained model for face detection
        +--- deploy.prototxt
        +--- res10_300x300_ssd_iter_140000.caffemodel
    +--- examples // examples images
        | // image files in this folder
    +--- image_script.py // mask detection on images
    +--- mask_detector.model // trained model for mask detection
    +--- MaskDetector.ipynb // jupyter notebook of training mask_detector.model
    +--- maskDL.mp4 // example video file for mask detection
    +--- video_script.py // script to perform mask detection from webcam feed
    +--- video_script_file.py // script to perform mask detection from video file
    +--- video_speed.py // speeds up mask detection by alternating frames
    +--- webcam_test.py // tests if webcam working or not
```


## Screenshots
### Example 1
![picture alt](.\screenshots/output_image_1.png)
### Example 2
![picture alt](.\screenshots/output_image_2.png)
