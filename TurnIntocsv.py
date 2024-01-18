import os

def generate_ffmpeg_command(input_filename, output_filename):
    return f"ffmpeg -f concat -safe 0 -i {input_filename} -c copy {output_filename}"

# 输入文件名列表的文本文件
input_file_list = 'output.txt'

# 输出文件名
output_filename = 'output.mp4'

# 生成 FFmpeg 命令
ffmpeg_command = generate_ffmpeg_command(input_file_list, output_filename)

# 执行 FFmpeg 命令
os.system(ffmpeg_command)
