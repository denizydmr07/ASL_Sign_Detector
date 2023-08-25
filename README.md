## Real-Time Sign Language Object Detection with YOLOv5s and OpenCV

This project demonstrates real-time [ASL (American Sign Language)](https://en.wikipedia.org/wiki/American_Sign_Language) object detection using the [pretrained YOLOv5s model from ultralytics](https://github.com/ultralytics/yolov5). I trained the model in the [Google Colab](https://colab.research.google.com/) and on the [ASL dataset from Roboflow by David Lee](https://public.roboflow.com/object-detection/american-sign-language-letters/1) and the model is capable of detecting various signs in real-time using a webcam feed.

### Results

| Precision | Recall | mAP50 | mAP50-90 |
| --------- | ------ | ----- | -------- |
| 0.912 | 0.907 | 0.947 | 0.690 |

### Example

![GIF](gif/asl_gif.gif)

### Usage

Clone the repository:
```bash
git clone https://github.com/denizydmr07/Real_Time_ASL_Sign_Detector.git
cd Real_Time_ASL_Sign_Detector
```
Install the requirements.txt
```bash
pip install -r requirements.txt
```
Run the main.py
```bash
python main.py
```
### Alternative Usage

You can download the "best.pt" and use it like
```python
model = torch.hub.load("ultralytics/yolov5", model="custom", path="best.pt", force_reload = True) # custom model
results = model(frame)
result = results.render()[0]
```
to make predictions.
 
