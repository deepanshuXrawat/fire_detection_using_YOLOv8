from ultralytics import YOLO

# use model
model = YOLO('model.pt')


# using camera
model.predict(source=0, imgsz=640, conf=0.6, show=True )


# using image
# model.predict(source='assests/example_2.jpg', imgsz=640, conf=0.6, save=True)
