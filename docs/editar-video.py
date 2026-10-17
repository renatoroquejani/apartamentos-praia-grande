from pathlib import Path
import subprocess
root=Path('dist/assets/kit-928')
originals=Path('media/originais')
black=[(2.2,2.7),(6.566667,7.066667),(10.933333,11.433333),(15.3,15.8),(19.666667,20.166667),(24,24.5),(28.366667,28.866667),(32.733333,33.233333),(37.1,37.6),(41.466667,41.966667)]
expr='not('+ '+'.join(f'between(t,{a},{b})' for a,b in black)+')'
filters=(f"[0:v]select='{expr}',setpts=N/(30*TB),scale=480:854:force_original_aspect_ratio=decrease,pad=480:854:(ow-iw)/2:(oh-ih)/2,setsar=1,format=yuv420p[v0];"
 f"[0:a]aselect='{expr}',asetpts=N/SR/TB,aresample=48000,aformat=channel_layouts=stereo[a0];"
 "[1:v]fps=30,scale=480:854:force_original_aspect_ratio=decrease,pad=480:854:(ow-iw)/2:(oh-ih)/2,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v1];"
 "[1:a]aresample=48000,aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS[a1];"
 "[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]")
cmd=['ffmpeg','-hide_banner','-loglevel','warning','-y','-i',str(originals/'passeio-1.mp4'),'-i',str(originals/'passeio-2.mp4'),'-filter_complex',filters,'-map','[v]','-map','[a]','-c:v','libx264','-preset','medium','-crf','22','-c:a','aac','-b:a','128k','-movflags','+faststart','-metadata:s:v:0','rotate=0',str(root/'passeio-completo.mp4')]
subprocess.run(cmd,check=True)
subprocess.run(['ffmpeg','-loglevel','error','-y','-ss','3','-i',str(root/'passeio-completo.mp4'),'-frames:v','1','-q:v','2',str(root/'passeio-completo.jpg')],check=True)
