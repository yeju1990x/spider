# -*- coding: utf-8 -*-


class OutputerService(object):
    def __init__(self):
        self.magnets = []

    def save_content(self, content):
        for line in content:
            if line not in self.magnets:
                self.magnets.append(line)
