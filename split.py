from moviepy.editor import VideoFileClip, clips_array
import os
from dotenv import load_dotenv, set_key, find_dotenv

'''
Script to Automatically create Split Screened TikToks
Progress in Gameplay material is saved in environment file (We don't want to use the same gameplay material for more than one TT)
If Splitscreen works:
TODO: Make gameplay video dependent on Phone that is used, phone as command argument (1,2,3)

'''
load_dotenv()
pubg_progress = int(os.getenv('pubg'))

ROOT = os.path.dirname(os.path.realpath(__file__))

video_dir = os.listdir(os.path.join(ROOT, 'workplace'))

print(f"pubg_progress BEFORE -- {pubg_progress}")

for video_name in video_dir:
    if video_name.endswith('.mp4'):
        video_abs_path = os.path.join(ROOT, 'workplace', video_name)
        tt_clip = VideoFileClip(video_abs_path).set_position(("center","top")).resize(height=512)
        gameplay = VideoFileClip(os.path.join(ROOT, 'gameplay', "pubg.mp4")).subclip(pubg_progress, pubg_progress + tt_clip.duration).resize(
            height=512).set_position(("center","bottom"))
        combined = clips_array([[tt_clip], [gameplay]])
        combined = combined.resize((576,1024))
        combined.write_videofile(os.path.join(ROOT, 'result', f"{video_name}_3.mp4")) # TODO Video name flexibility
        pubg_progress += tt_clip.duration

print(f"pubg_progress AFTER -- {pubg_progress}")
dotenv_file = find_dotenv()
set_key(dotenv_file, "pubg", str(pubg_progress))

