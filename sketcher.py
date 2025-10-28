import cv2

def sketch_image(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # blurr the image
    blurred_image = cv2.GaussianBlur(gray_image, (21, 21), 0)
    #divide the gray image by the blurred image
    portrait_image = cv2.divide(gray_image, blurred_image, scale=255.0)
    cv2.imshow('sketch', portrait_image)
    cv2.imwrite(output_image_path, portrait_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_path = 'landscape.jpg'  # specify your input image path
    output_path = 'sketch.jpg'  # specify your output image path
    sketch_image(input_path, output_path)