"""Corrige contato, capacidade e status no vídeo de referência do apartamento."""
from pathlib import Path
import subprocess
source=Path('media/originais/apto-19-andar/passeio.mp4')
out=Path('dist/assets/apto-19-andar')
subprocess.run([
 'ffmpeg','-loglevel','error','-y','-i',str(source),'-i','media/apto-19-andar-contato.png',
 '-filter_complex','[0:v][1:v]overlay=216:710:format=auto[v]','-map','[v]','-map','0:a?',
 '-c:v','libx264','-preset','medium','-crf','21','-pix_fmt','yuv420p','-c:a','copy',
 '-movflags','+faststart',str(out/'referencia.mp4')
],check=True)
subprocess.run(['ffmpeg','-loglevel','error','-y','-ss','30','-i',str(out/'referencia.mp4'),'-frames:v','1','-q:v','2',str(out/'referencia.jpg')],check=True)
