"""Prepara os vídeos do Edifício Pegasus, Guilhermina.

Fontes revisadas em quadros a cada dois segundos: sem telefone ou texto
promocional incorporado e sem faixas pretas adicionadas. Preserva imagem e
áudio, move o índice MP4 para o início para reprodução na web e gera capas.
Executar na raiz do projeto; não usa dependências Python externas.
"""
from pathlib import Path
import hashlib
import shutil
import subprocess

source = Path('media/originais/pegasus-guilhermina')
output = Path('dist/assets/pegasus-guilhermina')
share = Path.home() / 'Downloads/Pegasus Guilhermina - Videos para WhatsApp'
output.mkdir(parents=True, exist_ok=True)
share.mkdir(parents=True, exist_ok=True)

for number, poster_second in ((1, 4), (2, 10)):
    name = f'video-{number}'
    final = output / f'{name}.mp4'
    subprocess.run([
        'ffmpeg', '-loglevel', 'error', '-y', '-i', str(source / f'{name}.mp4'),
        '-c', 'copy', '-movflags', '+faststart', str(final),
    ], check=True)
    subprocess.run([
        'ffmpeg', '-loglevel', 'error', '-y', '-ss', str(poster_second),
        '-i', str(final), '-frames:v', '1', '-q:v', '2', str(output / f'{name}.jpg'),
    ], check=True)
    subprocess.run([
        'ffmpeg', '-v', 'error', '-i', str(final), '-fps_mode', 'passthrough', '-enc_time_base', '1:90000', '-f', 'null', '-',
    ], check=True)
    destination = share / f'Pegasus Guilhermina - 3 dormitorios - Video {number}.mp4'
    shutil.copy2(final, destination)
    assert hashlib.sha256(final.read_bytes()).digest() == hashlib.sha256(destination.read_bytes()).digest()
