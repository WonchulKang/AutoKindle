#!/usr/bin/env python
# -*- coding:utf-8 -*-

import glob

class DirWatcher :

	def __init__(self, watchPath, pattern) :
		if watchPath[-1] == '/' :
			watchPath = watchPath[:-1]
		self.watchPath = watchPath
		self.watchPattern = pattern.upper()

	def getInfo(self) :
		print "Watching Path : %s" % self.watchPath
		print "Watching Pattern : %s" % self.watchPattern

	def getAllFile(self) :
		return glob.glob("%s/*" % self.watchPath)

	def getFilteredFile(self) :
		oldList = self.getAllFile()
		newList = []
		for item in oldList :
			itemFind = item.upper()
			if itemFind.find(self.watchPattern) != -1 :
				newList.append(item)
		return newList
