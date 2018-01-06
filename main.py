#!/usr/bin/env python
# -*- coding: utf-8 -*
# gohook @ Python
# Functions: WebHook自动部署代码
# Created By HavenShen on 2016-04-05,Version 0.1

import comm_log
import subprocess
import json
import time
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

# 监听端口
define("port", default=8765, help="run on the given port", type=int)
# 日志输出
define("log", default=comm_log.get_logging('webhook'))
# 希望自动部署项目路径
file_path = '/var/www/Lazy-page'


def pull():
    cmd = ['git', 'pull', 'origin', 'master']
    p = subprocess.Popen(cmd, cwd=file_path)
    p.wait()


def check_branch():
    cmd = ['git', 'branch']
    p = subprocess.Popen(cmd, cwd=file_path, stdout=subprocess.PIPE)
    p.wait()
    branch = p.stdout.read()
    if branch.find("* master") != -1:
        return True
    return False


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('get done.')

    def post(self):
        print('\n\n', time.strftime('%Y-%m-%d %H:%M:%S'))
        data = tornado.escape.json_decode(self.request.body)
        options.log.info(self.request.headers.get('X-Coding-Event'))
        if data['token'] == '':
            right_branch = check_branch()
            if right_branch:
                pull()
                options.log.info('git pull done.')
            else:
                options.log.info('branch error.')
        else:
            options.log.info('git pull error.[token is false]')

        self.write('post done.')


class RobotsHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Disallow: /')

    def post(self):
        self.write('get done.')


application = tornado.web.Application([
    (r"/hook", MainHandler),
    (r"/robots.txt", RobotsHandler),
])

if __name__ == "__main__":
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
