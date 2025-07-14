from ultralytics import YOLO

# use model
model = YOLO('model.pt')
<<<<<<< HEAD
=======


# using camera
while True:
    model.predict(source=0, imgsz=640, conf=0.6, show=True )

>>>>>>> f7a5ccbf94eeedd90d9250e01124850a1d500afb


<<<<<<< HEAD
# using camera
model.predict(source=0, imgsz=640, conf=0.6, show=True )
=======
>>>>>>> f7a5ccbf94eeedd90d9250e01124850a1d500afb


# using image
# model.predict(source='assests/example_2.jpg', imgsz=640, conf=0.6, save=True)
