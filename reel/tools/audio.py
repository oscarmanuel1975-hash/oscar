import numpy as np, wave
sr=44100; D=33.0; N=int(sr*D)
L=np.zeros(N); Rr=np.zeros(N)
def place(sig,t0,pan=0.0,g=1.0):
    i=int(t0*sr)
    if i>=N: return
    n=min(len(sig),N-i)
    L[i:i+n]+=sig[:n]*g*(1-pan)/1.0*0.7071*(1+(-pan)); Rr[i:i+n]+=sig[:n]*g*0.7071*(1+pan)
def tone(f,dur,partials,decays,amp=1.0,att=0.004):
    t=np.arange(int(dur*sr))/sr; s=np.zeros_like(t)
    for (r,a),d in zip(partials,decays): s+=a*np.sin(2*np.pi*f*r*t)*np.exp(-t/d)
    e=np.minimum(1,t/att); return s*e*amp
MB=([(1,1),(2,.35),(3,.18),(4,.08)],[.55,.35,.22,.12])        # music box
BL=([(1,1),(2.76,.5),(5.4,.25),(8.93,.12)],[1.1,.7,.4,.2])    # bell
def mf(n): # note name -> Hz
    names={'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
    k=names[n[0]]+12*(int(n[1])+1)-69+ (1 if len(n)>2 and n[1]=='#' else 0)
    return 440*2**(k/12)
bpm=112; beat=60/bpm
P1=[('E5',1),('E5',1),('E5',2),('E5',1),('E5',1),('E5',2),('E5',1),('G5',1),('C5',1.5),('D5',.5),('E5',4)]
P2=[('F5',1),('F5',1),('F5',1.5),('F5',.5),('F5',1),('E5',1),('E5',1),('E5',.5),('E5',.5),('G5',1),('G5',1),('F5',1),('D5',1),('C5',4)]
mel=P1+P2
T0=3.4; t=T0
for n,d in mel:
    place(tone(mf(n),max(1.2,d*beat*1.2),*MB,amp=.30),t,pan=-.1); 
    place(tone(mf(n)*2,0.9,*MB,amp=.07),t,pan=.15)
    t+=d*beat
mel_end=t
# pad chords
chords=[('C',[48,52,55]),('C',[48,52,55]),('C',[48,52,55]),('C',[48,52,55]),('F',[41+12,45+12,48+12]),('C',[48,52,55]),('G',[43+12,47+12,50+12]),('C',[48,52,55])]
def midi(m): return 440*2**((m-69)/12)
for i,(nm,notes) in enumerate(chords):
    t0=T0+i*4*beat; dur=4*beat+0.6
    tt=np.arange(int(dur*sr))/sr
    env=np.minimum(1,tt/0.5)*np.minimum(1,(dur-tt)/0.6)
    for m in notes:
        s=(np.sin(2*np.pi*midi(m)*tt)+.4*np.sin(2*np.pi*midi(m)*2*tt))*env*.045
        place(s,t0,pan=0.0)
    place(np.sin(2*np.pi*midi(notes[0]-12)*tt)*env*.07,t0)
# intro pad + twinkles 0..3.4
tt=np.arange(int(4.5*sr))/sr; env=np.minimum(1,tt/1.5)*np.minimum(1,(4.5-tt)/1.0)
for m in [48,55,64]: place(np.sin(2*np.pi*midi(m)*tt)*env*.05,0)
for i,(n,tm) in enumerate([('E6',.5),('G6',.95),('C7',1.4),('E6',2.0),('D7',2.5),('G6',2.95)]):
    place(tone(mf(n),1.5,*BL,amp=.16),tm,pan=(-1)**i*.4)
# outro: arpeggio sparkle over C chord
t=mel_end-0.2
for k,n in enumerate(['C5','E5','G5','C6','E6','G6','C7']):
    place(tone(mf(n),2.2,*BL,amp=.12),t+k*0.16,pan=(-1)**k*.3)
tt=np.arange(int((D-t)*sr))/sr
env=np.minimum(1,tt/0.4)*np.clip((D-t-tt)/2.0,0,1)
for m in [48,52,55,60]: place(np.sin(2*np.pi*midi(m)*tt)*env*.05,t)
# sleigh bells (noise hats) every 8th from T0 to mel_end
rng=np.random.default_rng(3)
def shaker(dur=.09,amp=.05):
    n=int(dur*sr); x=rng.standard_normal(n); x=np.diff(x,prepend=0); x=np.diff(x,prepend=0)
    return x*np.exp(-np.arange(n)/sr/.025)*amp
t=T0
while t<mel_end-0.3:
    place(shaker(amp=.045),t,pan=.25); place(shaker(amp=.025),t+beat/2,pan=-.25); t+=beat
# whoosh
def whoosh(dur=.6,amp=.12,up=True):
    n=int(dur*sr); x=rng.standard_normal(n); out=np.zeros(n); y=0
    env=np.sin(np.pi*np.arange(n)/n)**2
    for i in range(n):
        a=0.02+0.30*(i/n if up else 1-i/n)
        y+=a*(x[i]-y); out[i]=y
    return out*env*amp*3
for tm in [3.3,8.95,13.1,18.1]: place(whoosh(.55),tm,pan=0)
# SFX
place(tone(mf('C6'),1.2,*BL,amp=.3),4.95); place(tone(mf('G6'),1.0,*BL,amp=.2),4.99)   # hat lands
place(tone(mf('E6'),.8,*BL,amp=.2),5.6)                                                     # bubble pop
for tm,n in zip([10.0,10.35,10.7,11.05],['C6','E6','G6','B6']): place(tone(mf(n),1.0,*BL,amp=.26),tm)
for n in ['C6','E6','G6','C7']: place(tone(mf(n),1.8,*BL,amp=.22),11.4)
place(tone(mf('B6'),.9,*BL,amp=.3),14.2); place(tone(mf('E7'),1.6,*BL,amp=.26),14.3)   # cha-ching
place(shaker(.5,.25),18.55)
# second pass of the chorus under sponsor + sleigh scenes
t=23.4
for n,d in P1:
    place(tone(mf(n),max(1.2,d*beat*1.2),*MB,amp=.30),t,pan=-.1); place(tone(mf(n)*2,0.9,*MB,amp=.07),t,pan=.15); t+=d*beat
tt=np.arange(int(9.2*sr))/sr; env=np.minimum(1,tt/0.6)*np.clip((9.2-tt)/1.2,0,1)
for m in [48,52,55]: place(np.sin(2*np.pi*midi(m)*tt)*env*.05,23.4)
place(np.sin(2*np.pi*midi(36)*tt)*env*.07,23.4)
# sleigh: dense bells panning left->right, whoosh, sponsor chime
tm=27.2
while tm<31.3:
    place(shaker(.11,.07),tm,pan=-.8+1.6*(tm-27.0)/4.3); tm+=0.11
place(whoosh(4.2,.10),27.0,pan=0)
for n in ['C6','E6','G6','C7']: place(tone(mf(n),1.8,*BL,amp=.2),24.0)
for k,n in enumerate(['G5','C6','E6','G6','C7']): place(tone(mf(n),2.0,*BL,amp=.14),31.0+k*.12,pan=.3)
# reverb-ish
def rev(x):
    y=x.copy()
    for d,g in [(0.173,.30),(0.271,.22),(0.397,.15)]:
        k=int(d*sr); y[k:]+=x[:-k]*g
    return y
L2,R2=rev(L),rev(Rr)
fade=np.clip((D-np.arange(N)/sr)/1.2,0,1); L2*=fade; R2*=fade
st=np.stack([L2,R2],1); st/=np.max(np.abs(st))/0.89
with wave.open('assets/music.wav','wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype('<i2').tobytes())
print('ok',mel_end)
