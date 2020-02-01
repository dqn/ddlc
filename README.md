# ddlc

Decode DDLC `.chr` files

## Check type of the files

### Monika

```bash
$ file characters/monika.chr
characters/monika.chr: PNG image data, 800 x 800, 8-bit/color RGB, non-interlaced
```

### Natsuki

```bash
$ file characters/natsuki.chr
characters/natsuki.chr: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 528x647, frames 3
```

### Sayori

```bash
$ file characters/sayori.chr
characters/sayori.chr: Ogg data, Vorbis audio, mono, 44100 Hz, ~110000 bps, created by: Xiph.Org libVorbis I (1.3.3)
```

### Yuri

```bash
$ file characters/yuri.chr
characters/yuri.chr: ASCII text, with very long lines, with no line terminators
```

## Decode

### Monika

```bash
$ python monika.py
# Output: decode/monika.txt
```

### Natsuki

```bash
$ python natsuki.py
# Output: decode/natsuki.png
```

### Sayori

```bash
$ python sayori.py
# Output: decode/sayori.png
```

### Yuri

```bash
$ python yuri.py
# Output: decode/yuri.txt
```
