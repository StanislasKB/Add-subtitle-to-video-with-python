from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import pysrt


def time_to_seconds(time_obj):
    return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000


def create_subtitle_clips(subtitles, videosize,fontsize=24, font='Arial', color='yellow', debug = False):
    subtitle_clips = []

    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time

        video_width, video_height = videosize
        
        text_clip = TextClip(subtitle.text, fontsize=fontsize, font=font, color=color, bg_color = 'black',size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
        subtitle_x_position = 'center'
        subtitle_y_position = video_height* 4 / 5 

        text_position = (subtitle_x_position, subtitle_y_position)                    
        subtitle_clips.append(text_clip.set_position(text_position))

    return subtitle_clips

def add_subtitles(video_path, subtitles_path):
    video = VideoFileClip(video_path)
    subtitles = pysrt.open(subtitles_path)

    begin,end= video_path.split(".mp4")
    output_video_file = begin+'_subtitled'+".mp4"

    print ("Output file name: ",output_video_file)
    subtitle_clips = create_subtitle_clips(subtitles,video.size)
    final_video = CompositeVideoClip([video] + subtitle_clips)
    final_video.write_videofile(output_video_file)

# Appeler la fonction avec les chemins appropriés
add_subtitles("Introduction_4.mp4", "Introduction.vtt")
