import subprocess,os,glob,struct

outdir = "amiga/sfx"
sampling_rate = 16000

for wav_file in glob.glob(os.path.join("../sound/*.wav")):
    raw_file = os.path.join(outdir,os.path.splitext(os.path.basename(wav_file))[0]+".raw")
    cmd = ["sox","--volume","5.0",wav_file,"--channels","1","--bits","8","-r",str(sampling_rate),"--encoding","signed-integer",raw_file]
    subprocess.check_call(cmd)
    with open(raw_file,"rb") as f:
        contents = f.read()
    with open(raw_file,"wb") as f:
         f.write(struct.pack(">H",sampling_rate))
         f.write(contents)

