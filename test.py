import cv2
import os

# Set the folder path
folder_path = r"C:\Users\harsh\Desktop\Python Projects\LCANET\data\s1"

# Initialize variables to track the total frames and number of videos
total_frames = 0
video_count = 0
max_frames = 0
max_frames_video = None

# Iterate over each file in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a .mpg file
    if file_name.endswith(".mpg"):
        # Create the full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Load the video using OpenCV
        video = cv2.VideoCapture(file_path)
        
        # Get the total number of frames
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Release the video capture object
        video.release()
        
        # Update the total frames and video count
        total_frames += frame_count
        video_count += 1
        
        # Update if this video has more frames than the current max
        if frame_count > max_frames:
            max_frames = frame_count
            max_frames_video = file_name

# Calculate the average frames if there are any .mpg videos
if video_count > 0:
    average_frames = total_frames / video_count
    print(f"The average number of frames per .mpg video is {average_frames:.2f}.")
    print(f"The video with the most frames is '{max_frames_video}' with {max_frames} frames.")
else:
    print("No .mpg files found in the specified folder.")
