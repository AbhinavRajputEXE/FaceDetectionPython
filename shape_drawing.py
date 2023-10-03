import cv2
import numpy as np

# Initialize variables
is_drawing = False
current_shape = 'Line'
start_x, start_y = -1, -1

# Define the mouse event callback function
def draw_event(event, x, y, flags, param):
    global start_x, start_y, is_drawing

    # When the left mouse button is pressed, start drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        is_drawing = True
        start_x, start_y = x, y

    # When the left mouse button is released, stop drawing and draw the shape
    elif event == cv2.EVENT_LBUTTONUP:
        is_drawing = False
        if current_shape == 'Line':
            cv2.line(img, (start_x, start_y), (x, y), (255, 0, 0), 2)
        elif current_shape == 'Rectangle':
            cv2.rectangle(img, (start_x, start_y), (x, y), (0, 255, 0), 2)
        elif current_shape == 'Circle':
            radius = int(np.sqrt((x - start_x)**2 + (y - start_y)**2))
            cv2.circle(img, (start_x, start_y), radius, (0, 0, 255), 2)
        elif current_shape == 'Ellipse':
            center = ((start_x + x) // 2, (start_y + y) // 2)
            axes = ((x - start_x) // 2, (y - start_y) // 2)
            cv2.ellipse(img, center, axes, 0, 0, 360, (255, 255, 0), 2)

# Define the main function
def main():
    global img, current_shape

    # Create a black image
    img = np.zeros((600, 800, 3), np.uint8)

    # Create a window and set the mouse event callback function
    cv2.namedWindow('Drawing Board')
    cv2.setMouseCallback('Drawing Board', draw_event)

    # Loop until the user presses the ESC key
    while True:
        # Show the image in the window
        cv2.imshow('Drawing Board', img)

        # Wait for a key press
        k = cv2.waitKey(1) & 0xFF

        # Change the current shape based on the key pressed
        if k == ord('l'):
            current_shape = 'Line'
        elif k == ord('r'):
            current_shape = 'Rectangle'
        elif k == ord('c'):
            current_shape = 'Circle'
        elif k == ord('e'):
            current_shape = 'Ellipse'
        elif k == 27:  # ESC key
            break

    # Destroy all windows
    cv2.destroyAllWindows()

# Call the main function if this file is run as the main program
if __name__ == '__main__':
    main()