#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'NOHI'

import os, sys, time, subprocess

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def log(s):
    print('[Monitor] %s' % s)


class MyFileSystemEventHander(FileSystemEventHandler):

    def __init__(self, fn):
        super(MyFileSystemEventHander, self).__init__()
        self.restart = fn

    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log('Python source file changed: %s' % event.src_path)
            self.restart()


command = ['echo', 'ok']
process = None


def kill_process():
    global process
    if process:
        log('Kill process [%s]...' % process.pid)
        process.kill()
        process.wait()
        log('Process ended with code %s.' % process.returncode)
        process = None


def start_process():
    global process, command
    log('Start process %s...' % ' '.join(command))
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)


def restart_process():
    kill_process()
    start_process()


def start_watch(path, callback):
    observer = Observer()
    observer.schedule(MyFileSystemEventHander(restart_process), path, recursive=True)
    observer.start()
    log('Watching directory %s...' % path)
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    argv = sys.argv[1:]
    if not argv:
        print('Usage: ./pymonitor your-script.py')
        exit(0)
    if argv[0] != 'python3':
        argv.insert(0, 'python3')
    command = argv

    pwd = os.getcwd()
    os.chdir(pwd + '/www')
    pwd = os.getcwd()
    print("当前目录: " + pwd)
    # father_path_method1 = os.path.dirname(pwd)
    # print("当前目录的父目录_方式一： " + father_path_method1)
    # sys.path.insert(0, father_path_method1)

    current_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    print("parent_dir： " + parent_dir)
    print("current_dir： " + current_dir)
    print("current_path： " + current_path)
    sys.path.insert(0, parent_dir)
    print('sys.path[%s]' % (sys.path))
    path = os.path.abspath('')
    start_watch(path, None)
