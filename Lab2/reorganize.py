#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import os
import datetime
import shutil


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True)
    parser.add_argument('--days', type=int, required=True)
    parser.add_argument('--size', type=int, required=True)

    return parser


def makedir(path):
    if not os.path.exists(os.path.join(args.source, path)):
        os.mkdir(os.path.join(args.source, path))


def copy_files(path, files):
    [shutil.copy(os.path.join(args.source, f), os.path.join(args.source, path, f))
     for f in files]


def date(file):
    t = os.path.getmtime(os.path.join(args.source, file))
    return datetime.datetime.fromtimestamp(t)


def size(file):
    return os.stat(os.path.join(args.source, file)).st_size


def process():
    today = datetime.datetime.now()
    files = os.walk(args.source).__next__()[2]
    [print('{} Date: {} Size: {}b Days difference: {}'
           .format(f, date(f), size(f), (today - date(f)).days)) for f in files]
    small_files = [f for f in files if size(f) < args.size]
    archive_files = [f for f in files if (today - date(f)).days > args.days]
    try:
        if archive_files:
            path = 'Archive'
            print('Files {} shall be moved to ..\\Archive\\'.format(archive_files))
            makedir(path)
            copy_files(path, archive_files)
        if small_files:
            path = 'Small'
            print('Files {} shall be moved to ..\\Small\\'.format(small_files))
            makedir(path)
            copy_files(path, small_files)
        list_of_deleted_files = small_files + [file for file in archive_files if not (file in small_files)]
        if list_of_deleted_files:
            print('Files {} shall be deleted from {}'
                  .format(list_of_deleted_files, args.source))
            [os.remove(os.path.join(args.source, f)) for f in list_of_deleted_files]
            print('Files were deleted successfully.')
    except (IOError, OSError) as err:
        print('There was an error:', err.args)
    else:
        print("Files were reorganized successfully.")


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    process()
