import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from skimage import io
from skimage.metrics import structural_similarity as ssim
from skimage.transform import resize

# Create a function to load the images
def load_images():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open a file dialog to select the first image
    image_path1 = filedialog.askopenfilename(title="Import first FingerPrint Image")

    # Open a file dialog to select the second image
    image_path2 = filedialog.askopenfilename(title="Import Second FingerPrint Image")

    return image_path1, image_path2

# Load the two fingerprint images interactively
image_path1, image_path2 = load_images()

# Check if the user canceled image selection
if not image_path1 or not image_path2:
    messagebox.showinfo("Info", "Image selection canceled.")
else:
    fingerprint1 = io.imread(image_path1, as_gray=True)  # Load in grayscale
    fingerprint2 = io.imread(image_path2, as_gray=True)

    # Resize images to have the same dimensions
    fingerprint1 = resize(fingerprint1, fingerprint2.shape, anti_aliasing=True)

    # Compare the two fingerprint images with specified data_range
    similarity = ssim(fingerprint1, fingerprint2, data_range=fingerprint2.max() - fingerprint2.min())

    # Define a threshold for matching
    matching_threshold = 0.9

    # Compare the SSIM value to the threshold and show the result in a dialog box
    if similarity > matching_threshold:
        messagebox.showinfo("Result", "FingerPrints are the same!")
    else:
        messagebox.showinfo("Result", "FingerPrints are not the same!")

#CodeBy: github.com/mehditohidi
