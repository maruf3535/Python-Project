import moviepy.editor as mve


mp4_file_path = r'D:\music\video\qwalli\nusrat fateh ali khan'
file_names = [r'\Khawaja Eh Khajagaan Hamiye Bekasaan - Ustad Nusrat Fateh Ali Khan - OSA Worldwide.mkv']

# file_names = r'\Jab Karam Hota Hai Halat Badal Jate Hain - Sufiyana Qawwali - Nusrat Fateh Ali Khan'

mp3_file_path = r'D:\music\audio\qwalli\nusrat fateh ali khan'

# read video file
for file_name in file_names:
    # video = mve.VideoFileClip(mp4_file_path + file_name + '.mp4')
    video = mve.VideoFileClip(mp4_file_path + file_name)

    # convert video data to audio
    convert = video.audio

    # save the audio file
    convert.write_audiofile(mp3_file_path + file_name + '.mp3')




# video = mve.VideoFileClip(mp4_file_path + file_names + '.mp4')

# # convert video data to audio
# convert = video.audio

# # save the audio file
# convert.write_audiofile(mp3_file_path + file_names + '.mp3')