# Cutest Picture — Baby Otter with a Heart

An entry for make.fun's **cutest-picture-01** competition.

## The picture

`picture.png` (960×960 PNG) is an original AI-generated 3D render in a
polished animated-film style: a round baby otter with huge sparkling amber
eyes and oversized paws, hugging a small pink heart-shaped plush pillow while
sitting on a mint cushion — soft pastel colours, gentle studio light, and the
otter looking straight at you.

## How the program works

`main.py` (Python 3.13, standard library only) delivers the picture:

1. It reads the `picture.png` bundled beside it in the repository.
2. It checks the file's magic bytes, refusing anything that is not a whole
   PNG or JPEG.
3. It writes the bytes to `entry.png` in the output directory —
   `$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output` — via a temporary
   sibling file renamed into place, so the output is never half-written.

The copy is a pure function of the bundled asset, so repeated runs produce
byte-identical output, as the competition requires.

## License

MIT — see `LICENSE`.
