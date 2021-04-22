from moviepy.editor import *

import utils

video = VideoFileClip("caminho do video original")

start_time = input("Informe o tempo inicial do corte: ")

fstart_time = utils.convert_time_to_seconds(start_time)

end_time = input("Informe o tempo final do corte: ")

fend_time = utils.convert_time_to_seconds(end_time)

trimed_video = video.subclip(fstart_time, fend_time)

trimed_video.write_videofile("caminho do vídeo cortado")