from moviepy.editor import *

video = VideoFileClip("Introduction_4.mp4").subclip(50,60)

# Make the text. Many more options are available.
txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
             .set_position(('center','bottom'))
             .set_duration(10) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile("myHolidays_edited.mp4",codec='libx264', audio_codec='aac') # Many options...