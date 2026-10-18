"""Une os dois trechos do Pegasus e remove o início repetido do segundo.

Comparação dos quadros finais do primeiro com o início do segundo confirmou
sobreposição de aproximadamente 3,33 s. O segundo retoma em 3,366667 s,
logo após o último quadro já exibido. Mantém 848×480 e áudio dos dois trechos.
Executar na raiz do projeto com FFmpeg disponível.
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
final = output / 'passeio-completo.mp4'
subprocess.run([
    'ffmpeg', '-loglevel', 'error', '-y',
    '-i', str(source / 'video-1.mp4'), '-i', str(source / 'video-2.mp4'),
    '-filter_complex',
    '[0:v]setpts=PTS-STARTPTS[v0];[0:a]asetpts=PTS-STARTPTS[a0];'
    '[1:v]trim=start=3.366667,setpts=PTS-STARTPTS[v1];'
    '[1:a]atrim=start=3.366667,asetpts=PTS-STARTPTS[a1];'
    '[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]',
    '-map', '[v]', '-map', '[a]', '-r', '30',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', str(final),
], check=True)
subprocess.run([
    'ffmpeg', '-loglevel', 'error', '-y', '-ss', '4', '-i', str(final),
    '-frames:v', '1', '-q:v', '2', str(output / 'passeio-completo.jpg'),
], check=True)
subprocess.run(['ffmpeg', '-v', 'error', '-i', str(final), '-f', 'null', '-'], check=True)
destination = share / 'Pegasus Guilhermina - Passeio completo.mp4'
shutil.copy2(final, destination)
assert hashlib.sha256(final.read_bytes()).digest() == hashlib.sha256(destination.read_bytes()).digest()
print('Vídeo completo preparado e decodificado; cópia WhatsApp conferida.')
