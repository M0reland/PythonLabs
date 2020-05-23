import argparse
import os
import subprocess
from random import randint
from pathlib import Path

mus_ext = ['.mp3', '.wav', '.aif', '.mid']


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', '-s', required=True)
    parser.add_argument('--destination', '-d', default='mix.mp3')
    parser.add_argument('--count', '-c', default=-1, type=int)
    parser.add_argument('--frame', '-f', default=10, type=int)
    parser.add_argument('--log', '-l', action='store_const', const=True)
    parser.add_argument('--extended', '-e', action='store_const', const=True)
    return parser


def mus_file():
    files = os.walk(args.source).__next__()[2]
    i = args.count if args.count != -1 else len(files)
    for f in files:
        if (i > 0) and (Path(f).suffix.lower() in mus_ext):
            i -= 1
            yield f


def commands(i, m):
    name = 'temp{:05}.mp3'.format(i)
    rndm_start = '00:00:{0:02}'.format(randint(20, 50))
    duration = '{2:02}:{1:02}:{0:02}'.format(args.frame % 60, (args.frame // 60) % 60,
                                             args.frame // 3600)
    if args.extended:
        return ['ffmpeg', '-ss', rndm_start, '-t', duration,
                '-i', os.path.join(args.source, m), '-af',
                'afade=t=in:st=0:d={0:01},afade=t=out:st={1:01}:d={0:01}'.format(
                    args.frame * 0.2, args.frame * 0.8),
                os.path.join(args.source, name)]
    else:
        return ['ffmpeg', '-ss', rndm_start, '-t', duration,
                '-i', os.path.join(args.source, m), '-acodec', 'copy',
                os.path.join(args.source, name)]


def cut(musics):
    temporary = []
    for i, m in enumerate(musics):
        # print(commands(i,m))
        stdout, stderr = subprocess.Popen(commands(i, m), stdout=subprocess.PIPE,
                                          stderr=subprocess.STDOUT).communicate()
        if args.log:
            print('--- processing file {}: {}'.format(i + 1, m))
        temporary.append('temp{:05}.mp3'.format(i))
    return temporary


def concatenate(musics):
    if args.log:
        print('--- merging the fragments together...')
    with open('files.txt', 'w') as f:
        f.write('\n'.join(["file '{}'".format(
            os.path.join(args.source, m)) for m in musics]))

    cmd = ['ffmpeg', '-f', 'concat', '-safe', '0',
           '-i', 'files.txt', '-acodec', 'copy',
           os.path.join(args.source, args.destination)]
    stdout, stderr = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT).communicate()
    os.remove('files.txt')


def delete(musics):
    if args.log:
        print('--- deleting temporary files...')
    for m in musics:
        os.remove(os.path.join(args.source, m))


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    try:
        os.remove(os.path.join(args.source, args.destination))
        music2cut = [m for m in mus_file()]
        fragments = cut(music2cut)
        concatenate(fragments)
        delete(fragments)
        if args.log:
            print('--- done')
    except OSError as err:
        print('There was an error:', err.args)
