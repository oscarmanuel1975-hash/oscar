"""Librería mínima para sintetizar música y efectos sin usar pistas con derechos.
Uso en un script del proyecto:
    import sys; sys.path.insert(0, '<ruta a esta carpeta>')
    from synth_lib import *
    m = Mix(duracion=33)
    m.place(tone(note('E5'), 1.2, MUSIC_BOX, amp=.3), t0=3.4)
    m.save('assets/music.wav')
La duración de la mezcla debe ser igual a la del vídeo.
"""
import numpy as np, wave
SR = 44100
MUSIC_BOX = ([(1, 1), (2, .35), (3, .18), (4, .08)], [.55, .35, .22, .12])
BELL = ([(1, 1), (2.76, .5), (5.4, .25), (8.93, .12)], [1.1, .7, .4, .2])

def note(name):
    """'C5' o 'F#4' -> Hz."""
    base = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}[name[0]]
    sharp = 1 if len(name) > 2 and name[1] == '#' else 0
    octave = int(name[-1])
    return 440 * 2 ** ((base + sharp + 12 * (octave + 1) - 69) / 12)

def tone(freq, dur, timbre, amp=1.0, att=.004):
    parciales, decaimientos = timbre
    t = np.arange(int(dur * SR)) / SR
    s = sum(a * np.sin(2 * np.pi * freq * r * t) * np.exp(-t / d) for (r, a), d in zip(parciales, decaimientos))
    return s * np.minimum(1, t / att) * amp

def pad(freqs, dur, amp=.05, att=.5, rel=.6):
    t = np.arange(int(dur * SR)) / SR
    env = np.minimum(1, t / att) * np.clip((dur - t) / rel, 0, 1)
    return sum(np.sin(2 * np.pi * f * t) + .4 * np.sin(4 * np.pi * f * t) for f in freqs) * env * amp

def shaker(dur=.09, amp=.05, seed=3):
    rng = np.random.default_rng(seed)
    n = int(dur * SR); x = np.diff(np.diff(rng.standard_normal(n), prepend=0), prepend=0)
    return x * np.exp(-np.arange(n) / SR / .025) * amp

def whoosh(dur=.6, amp=.12, up=True, seed=5):
    rng = np.random.default_rng(seed)
    n = int(dur * SR); x = rng.standard_normal(n); out = np.zeros(n); y = 0.0
    env = np.sin(np.pi * np.arange(n) / n) ** 2
    for i in range(n):
        y += (0.02 + 0.30 * (i / n if up else 1 - i / n)) * (x[i] - y); out[i] = y
    return out * env * amp * 3

class Mix:
    def __init__(self, duracion):
        self.D = duracion; self.N = int(SR * duracion)
        self.L = np.zeros(self.N); self.R = np.zeros(self.N)
    def place(self, sig, t0, pan=0.0, gain=1.0):
        """pan de -1 (izquierda) a 1 (derecha)."""
        i = int(t0 * SR)
        if i >= self.N: return
        n = min(len(sig), self.N - i)
        self.L[i:i + n] += sig[:n] * gain * .7071 * (1 - pan)
        self.R[i:i + n] += sig[:n] * gain * .7071 * (1 + pan)
    def save(self, path, reverb=True, fade_out=1.2):
        L, R = self.L.copy(), self.R.copy()
        if reverb:
            for ch in (L, R):
                src = ch.copy()
                for d, g in [(.173, .30), (.271, .22), (.397, .15)]:
                    k = int(d * SR); ch[k:] += src[:-k] * g
        fade = np.clip((self.D - np.arange(self.N) / SR) / fade_out, 0, 1)
        st = np.stack([L * fade, R * fade], 1)
        st /= max(1e-9, np.max(np.abs(st))) / 0.89   # deja margen para no saturar
        with wave.open(path, 'wb') as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
            w.writeframes((st * 32767).astype('<i2').tobytes())
        return path

if __name__ == '__main__':
    import sys
    m = Mix(9)
    for k, n in enumerate(['C5', 'E5', 'G5', 'C6']):
        m.place(tone(note(n), 1.5, MUSIC_BOX, amp=.3), .5 + k * .5)
    m.place(pad([note('C3'), note('E3'), note('G3')], 8), 0)
    m.place(whoosh(.5), 2.7)
    m.place(tone(note('C7'), 1.5, BELL, amp=.2), 6)
    print(m.save(sys.argv[1] if len(sys.argv) > 1 else 'demo.wav'))
