'''
C:\Of\tools\d
black phone:
ffmpeg -i "C:\Of\tools\9.mp4" -s 560x988 -b:v 3.5M -b:a 192k -r 30 -crf 18 -vf eq=brightness=0.02 -vf eq=contrast=0.8 "C:\Of\tools\9_1.mp4"

pink phone:
ffmpeg -i "C:\Of\tools\28.mp4" -s 568x1002 -b:v 4.0M -b:a 256k -r 32 -crf 20 -vf eq=brightness=0.24 -vf eq=contrast=1.2 "C:\Of\tools\28_2.mp4"

3rd config
ffmpeg -i "C:\Of\tools\d7.mp4" -s 550x960 -b:v 3.0M -b:a 320k -r 34 -crf 22 -vf eq=brightness=0.12 -vf eq=contrast=-1.6 "C:\Of\tools\d7_1.mp4"


#ffmpeg -i "C:\Of\tools\d4_1.mp4" -r 30 -crf 18 "C:\Of\tools\d4_2.mp4"

2nd black phone:


ffmpeg -i "C:\Of\tools\d1.mp4" -i "C:\Of\tools\pubg1.mp4" -filter_complex 
"[0:a]volume=1.0[a0];[1:a]volume=0.1[a1];[0]scale=288:512[v0];[1]scale=288:512[v1];
[v0][v1]xstack=inputs=2:shortest=1:layout=0_0|0_h0[v]; [a0][a1]amix=inputs=2[a]" -map "[v]" -map "[a]" -shortest output.mp4


ffmpeg -i "C:\Of\tools\d1.mp4" -i "C:\Of\tools\gameplay\pubg1.mp4" -filter_complex "[0:a]volume=1.0[a0];[1:a]volume=0.1[a1];[0]scale=576:512[v0];[1]scale=576:512[v1]; [v0][v1]xstack=inputs=2:shortest=1:layout=0_0|0_h0[v]; [a0][a1]amix=inputs=2:duration=first[a]" -map "[v]" -map "[a]" -shortest d1_33.mp4


'''


import os
from subprocess import call
import platform   # for cross-platform implementation
import time

def create_splitscreen_for_whole_dir():

    ROOT = os.path.abspath(os.path.dirname(__file__))
    cmd = 'python3' if platform.system() != 'Windows' else 'py -3'

    

    for file in os.listdir(ROOT):
        if file.endswith('mp4'):
            if not os.path.exists(os.path.join(ROOT,file[:-4] +"_3.mp4")):
                start = time.time()
                print(f"START Processing {file} ")
                split_screen_command = f'ffmpeg -i "C:\\Of\\tools\\{file}" -i "C:\\Of\\tools\\gameplay\\pubg1.mp4" -filter_complex "[0:a]volume=1.0[a0];[1:a]volume=0.1[a1];[0]scale=576:512[v0];[1]scale=576:512[v1]; [v0][v1]xstack=inputs=2:shortest=1:layout=0_0|0_h0[v]; [a0][a1]amix=inputs=2:duration=first[a]" -map "[v]" -map "[a]" -shortest {file[:-4]}_3.mp4'
                call(f'{split_screen_command}', shell=True, cwd=ROOT) 
                print(f"FINISHED Processing {file} in {time.time() - start} seconds")
                time.sleep(1)
if __name__ == "__main__":
    create_splitscreen_for_whole_dir()
