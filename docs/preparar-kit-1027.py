from pathlib import Path
import subprocess
src=Path('media/originais/kit-1027');out=Path('dist/assets/kit-1027')
for name in ['ambientes','passeio']:
 subprocess.run(['ffmpeg','-loglevel','error','-y','-i',str(src/f'{name}.mp4'),'-i','media/kit-1027-contato.png','-filter_complex','[0:v][1:v]overlay=232:800:format=auto[v]','-map','[v]','-map','0:a?','-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',str(out/f'{name}.mp4')],check=True)
 subprocess.run(['ffmpeg','-loglevel','error','-y','-ss','3','-i',str(out/f'{name}.mp4'),'-frames:v','1','-q:v','2',str(out/f'{name}.jpg')],check=True)
