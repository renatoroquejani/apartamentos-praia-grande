"""Atualiza somente a faixa de contato do primeiro vídeo da Kitnet 2014."""
from pathlib import Path
import subprocess

source = Path('media/originais/kit-2014')
output = Path('dist/assets/kit-2014')
subprocess.run([
    'ffmpeg', '-loglevel', 'error', '-y', '-i', str(source/'passeio.mp4'),
    '-i', 'media/kit-2014-contato.png', '-filter_complex',
    '[0:v][1:v]overlay=224:755:format=auto[v]', '-map', '[v]', '-map', '0:a?',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-pix_fmt', 'yuv420p',
    '-c:a', 'copy', '-movflags', '+faststart', str(output/'passeio.mp4'),
], check=True)
subprocess.run([
    'ffmpeg', '-loglevel', 'error', '-y', '-i', str(source/'vista.mp4'),
    '-c', 'copy', '-movflags', '+faststart', str(output/'vista.mp4'),
], check=True)
for name in ['passeio', 'vista']:
    subprocess.run([
        'ffmpeg', '-loglevel', 'error', '-y', '-ss', '3', '-i', str(output/f'{name}.mp4'),
        '-frames:v', '1', '-q:v', '2', str(output/f'{name}.jpg'),
    ], check=True)
