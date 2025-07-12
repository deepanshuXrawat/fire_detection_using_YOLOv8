from ultralytics import YOLO

# use model
model = YOLO('best.pt')

# using image
# model.predict(source='example_1.jpg', imgsz=640, conf=0.6, save=True)

# using camera
model.predict(source=0, imgsz=640, conf=0.6, show=True)

# using phone camera
# model.predict(source='http://192.168.0.104:4747/video', imgsz=640, conf=0.6, show=True)