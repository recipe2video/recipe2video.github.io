"""
Dependencies:
    - ffmpeg: https://ffmpeg.org/download.html
    - cv2: 'pip install opencv-python'
    - youtube-dl: https://github.com/ytdl-org/youtube-dl (Install commands below)
"""

import cv2
import os
import glob

def install_youtube_dl():
    # Installing latest youtube-dl
    os.system("sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl")
    os.system("sudo chmod a+rx /usr/local/bin/youtube-dl")


def to_youtube_link(video_id, timestamp):
    """
    Simple function to format video_id, timestamp pair to YouTube link.
    """
    return f"https://www.youtube.com/watch?v={video_id}&t={timestamp}s"


def download_frames(video_id, timestamp, output_dir='r2vq_framedata', keep_vid=False):
    """
    Downloads YouTube video using youtube-dl, and normalizes to 10fps with ffmpeg.
    Then, saves relevant image trigrams as .jpg files to output_dir.
    If keep_vid set to False, deletes original video.
    """
    timestamps = [timestamp + x for x in range(3)]
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    # Download video
    vid_url = f"https://www.youtube.com/watch?v={video_id}"
    vid_output = f"'{output_dir}/{video_id}.%(ext)s'"
    os.system(' '.join(("youtube-dl -f 160 -o", vid_output, vid_url)))
    youtube_dl_path = glob.glob(f'{output_dir}/{video_id}.*')[0]
    # Convert to 10fps
    ffmpeg_path = os.path.join(output_dir, f'{video_id}_10fps.mp4')
    os.system('ffmpeg -i {} -filter:v fps=fps=10 {}'.format(youtube_dl_path, ffmpeg_path))
    os.remove(youtube_dl_path)
    # Downloading relevant frames
    cap = cv2.VideoCapture(ffmpeg_path)
    frame_num = 0
    try:
        while True:
            ret, frame = cap.read()
            frame_num += 1
            if not ret:
                break
            if int(frame_num / 10) in timestamps:
                dest = f'{output_dir}/frame{timestamps.index(int(frame_num/10))}.jpg'
                cv2.imwrite(dest, frame)
    finally:
        cap.release()
    if not keep_vid:
        os.remove(ffmpeg_path)

if __name__ == '__main__':
    download_frames('xHr8X2Wpmno', 170)
