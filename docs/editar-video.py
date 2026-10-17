"""Prepara os dois vídeos com proporções próprias, sem cortar a imagem útil."""
from pathlib import Path
import subprocess

originals = Path('media/originais')
output = Path('dist/assets/kit-928')

# Cropdetect confirmado em múltiplos quadros: imagem útil 478x638, y=106.
subprocess.run([
    'ffmpeg', '-loglevel', 'error', '-y', '-i', str(originals / 'passeio-1.mp4'),
    '-vf', 'crop=478:638:0:106,setsar=1', '-c:v', 'libx264', '-preset', 'medium',
    '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart',
    str(output / 'ambientes.mp4'),
], check=True)
# O segundo arquivo já tem imagem útil em toda a altura; preservar integralmente.
subprocess.run([
    'ffmpeg', '-loglevel', 'error', '-y', '-i', str(originals / 'passeio-2.mp4'),
    '-c', 'copy', '-movflags', '+faststart', str(output / 'passeio.mp4'),
], check=True)
for name in ('ambientes', 'passeio'):
    subprocess.run([
        'ffmpeg', '-loglevel', 'error', '-y', '-ss', '3', '-i', str(output / f'{name}.mp4'),
        '-frames:v', '1', '-q:v', '2', str(output / f'{name}.jpg'),
    ], check=True)
