import cv2
import os
import json
from pathlib import Path
from uuid import uuid4
from tqdm import tqdm

class Frame2Vid:
    def __init__(self, metadata_path, output_dir, format='mp4'):
        """
        Initialize the Frame2Vid class.

        :param input_folder: Path to the folder containing the frames.
        :param output_file: Path where the output video should be saved.
        :param format: Output video format, default is 'mp4'.
        """
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
        self.metadata_path = metadata_path
        self.metadata = metadata
        self.input_folder = metadata['frames_folder']
        _input_folder = Path(self.input_folder)
        assert _input_folder.exists(), "Input folder does not exist."
        total_frames = len(list(_input_folder.glob('*')))
        assert total_frames == metadata['total_frames'], "Total frames in metadata.json and input folder do not match."
        self.output_dir = output_dir
        self.format = format
        self.framerate = metadata["fps"]
        self.new_filename = str(uuid4()) + '.' + self.format

    def create_video(self):
        """
        Create a video from frames in the input folder.
        """
        # Define the codec
        if self.format == 'mp4':
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        elif self.format == 'mkv':
            fourcc = cv2.VideoWriter_fourcc(*'mkv1')
        else:
            raise Exception("Invalid video format. Please use 'mp4' or 'mkv'.")

        # Initialize video writer
        output_file = os.path.join(self.output_dir, self.new_filename)
        frames = sorted(os.listdir(self.input_folder))

        # get framesize from first frame
        frame = cv2.imread(os.path.join(self.input_folder, frames[0]))
        height, width, layers = frame.shape
        shape_tuple = (width, height)

        out = cv2.VideoWriter(output_file, fourcc, self.framerate, shape_tuple)

        
        for frame_name in tqdm(frames, desc='Creating video'):
            frame = cv2.imread(os.path.join(self.input_folder, frame_name))
            out.write(frame)

        out.release()

        self.metadata["imported_video"] = output_file
            
        with open(self.metadata_path, 'w') as f:
            json.dump(self.metadata, f, indent=4)
