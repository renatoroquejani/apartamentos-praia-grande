"""Prepara o vídeo do apartamento de 3 dormitórios sem recomprimir a imagem.

Fonte revisada: sala e vista para o mar, sem faixas pretas ou telefone incorporado.
"""
from pathlib import Path
import shutil
import subprocess

source = Path('media/originais/apto-11-andar/passeio.mp4')
output = Path('dist/assets/apto-11-andar')
output.mkdir(parents=True, exist_ok=True)
subprocess.run([
    'ffmpeg', '-loglevel', 'error', '-y', '-i', str(source),
    '-c', 'copy', '-movflags', '+faststart', str(output/'passeio.mp4'),
], check=True)
subprocess.run([
    'ffmpeg', '-loglevel', 'error', '-y', '-ss', '3',
    '-i', str(output/'passeio.mp4'), '-frames:v', '1', '-q:v', '2',
    str(output/'passeio.jpg'),
], check=True)
subprocess.run([
    'ffmpeg', '-v', 'error', '-i', str(output/'passeio.mp4'),
    '-f', 'null', '-',
], check=True)
share = Path.home()/'Downloads/Apartamento 3 dormitorios - 11 andar - Video para WhatsApp'
share.mkdir(parents=True, exist_ok=True)
shutil.copy2(output/'passeio.mp4', share/'Apartamento 3 dormitorios - 11 andar - Passeio.mp4')
