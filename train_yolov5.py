import os

# Define the path to the YOLOv5 directory
yolov5_path = r'C:\Users\jrola\Documents\yolo 5\yolov5'

# Check if the YOLOv5 path exists
if not os.path.exists(yolov5_path):
    raise FileNotFoundError(f'The YOLOv5 directory does not exist at the specified path: {yolov5_path}')

# Change the working directory to the YOLOv5 path
os.chdir(yolov5_path)

# Define training parameters
image_size = 640  # Image size
batch_size = 30   # Batch size
epochs = 50       # Number of epochs

# Use the correct path for data.yaml
data_file = r'C:\Users\jrola\Documents\Traffic Road Object Detection project\data.yaml'
weights_file = 'yolov5s.pt'  # Ensure this file is in the yolov5 directory

def train_yolov5():
    command = f'python train.py --img {image_size} --batch {batch_size} --epochs {epochs} --data "{data_file}" --weights {weights_file}'
    os.system(command)

# Run the training function
if __name__ == '__main__':
    train_yolov5()
