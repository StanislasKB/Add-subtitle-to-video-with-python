from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
import webvtt
from datetime import datetime

# def str_to_time(time_str):
#     time_obj = datetime.strptime(time_str, "%H:%M:%S.%f")
#     hours = time_obj.hour
#     minutes = time_obj.minute
#     seconds = time_obj.second
#     milliseconds = time_obj.microsecond // 1000  
#     return {'hours': hours, 'minutes': minutes, 'seconds': seconds, 'milliseconds': milliseconds}

# class Temps:
#     def __init__(self, heures, minutes, secondes, millisecondes):
#         self.heures = heures
#         self.minutes = minutes
#         self.secondes = secondes
#         self.millisecondes = millisecondes

# def str_to_time_obj(time_str):
#     time_obj = datetime.strptime(time_str, "%H:%M:%S.%f")
#     hours = time_obj.hour
#     minutes = time_obj.minute
#     seconds = time_obj.second
#     milliseconds = time_obj.microsecond // 1000  
#     return Temps(hours, minutes, secondes, millisecondes)


def time_to_seconds(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M:%S.%f")
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second + time_obj.microsecond // 1000


def create_subtitle_clips(subtitles, videosize,fontsize=24, font='Arial', color='white', debug = False):
    subtitle_clips = []

    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time

        video_width, video_height = videosize
        
        text_clip = TextClip(subtitle.text, fontsize=fontsize, font=font, color=color, bg_color = 'black',size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
        subtitle_x_position = 'center'
        subtitle_y_position = 'bottom' 

        text_position = (subtitle_x_position, subtitle_y_position)                    
        subtitle_clips.append(text_clip.set_position(text_position))

    return subtitle_clips

def add_subtitles(video_path, subtitles_path):
    video = VideoFileClip(video_path)
    subtitles = webvtt.read(subtitles_path)

    begin,end= video_path.split(".mp4")
    output_video_file = begin+'_subtitled'+".mp4"

    print ("Output file name: ",output_video_file)

    # Create subtitle clips
    subtitle_clips = create_subtitle_clips(subtitles,video.size)

    # Add subtitles to the video
    final_video = CompositeVideoClip([video] + subtitle_clips)

    # Write output video file
    final_video.write_videofile(output_video_file)

# Appeler la fonction avec les chemins appropriés
add_subtitles("Ansible on Jenkins.mp4", "Ansible on Jenkins.vtt")
