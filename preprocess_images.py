import cv2
import os

input_dir = 'images'
output_dir = 'images_preprocessed'

def preprocess_images(input_dir, output_dir):
    #Create folder for output
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #Go through every image in input_dir and crop it
    for filename in os.listdir(input_dir):
        actual_image = cv2.imread(os.path.join(input_dir, filename))
        if actual_image is not None:
            new_image = actual_image[111:433, 48:371]
            cv2.imwrite(output_dir + "/" + filename, new_image)

def main():
    preprocess_images('images', 'images_preprocessed')

if __name__ == "__main__":
    main()