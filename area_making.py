import cv2
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def selectFile():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select a video",
        filetypes=[("Video Files", "*.mp4")]
    )
    
    root.destroy()  # Close the Tkinter root window
    return file_path

# Select a file
video_path = selectFile()

# Check if a file was selected
if video_path:
    print(f"Selected file: {video_path}")
    
    # Open the video with OpenCV
    video = cv2.VideoCapture(video_path)
    
    if not video.isOpened():
        print("Error: Could not open video.")
    else:
        # Prepare Matplotlib for displaying frames
        fig, ax = plt.subplots()
        ret, frame = video.read()
        
        if not ret:
            print("Error: Could not read video frames.")
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for Matplotlib
            im = ax.imshow(frame)

            def update_frame(_):
                video
                ret, frame = video.read()
                if not ret:
                    print("End of video.")
                    video.release()
                    plt.close(fig)  # Close the figure when the video ends
                    return im,

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
                im.set_array(frame)
                return im,

            ani = FuncAnimation(
                fig,
                update_frame,
                interval=50,  # Update frames at ~20 FPS
                cache_frame_data=False  # Disable frame caching to suppress warnings
            )
            plt.axis("off")  # Hide axis
            plt.show()
else:
    print("No video file selected.")
