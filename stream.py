import numpy as np
from numpy import genfromtxt
import pandas as pd

class Stream(object):
	"""
	Initialize a stream by reading data from file.
	Input data file formats: ARFF or Sparse (.data)
	"""
	def __init__(self, filename, initialSize):
		self.initialData = None
		self.initialDataLabels = []
		self.data = None
		self.dataLabels = []
		if filename.endswith('.csv'):
			self.__readDataArrCSV(filename, initialSize)
		else:
			self.__readDataArrNotCSV(filename, initialSize)

	"""
	Read data from file in CSV or Sparse format.
	Return maximum number of variables.
	"""
	def __readData(self, filename, initialSize):
		with open(filename) as f:
			data = f.readlines()

		maxvar = 0
		for i in data:
			d = {}
			if filename.endswith('.csv'):
				features = i.strip().split(',')
				d[-1] = features[-1]
				for j in xrange(len(features)-1):
					d[j] = float(features[j])
				maxvar = len(features)-1
			else:
				features = i.strip().split(' ')
				for fea in features:
					val = fea.strip().split(':')
					if len(val) < 2:
						d[-1] = float(val[0])
					else:
						d[int(val[0])-1] = float(val[1])
					#get maximum number of features
					if maxvar < int(val[0]):
						maxvar = int(val[0])

			if len(self.initialData) < initialSize:
				self.initialData.append(d)
			else:
				self.data.append(d)

		return maxvar


	"""
	Read data from file in CSV or Sparse format.
	Data will be stored in 2D array format
	Return maximum number of variables.
	"""
	def __readDataArrNotCSV(self, filename, initialSize):
		with open(filename) as f:
			data = f.readlines()

		maxvar = 0

		for i in data:
			singleInstArr = None
			label = None
			features = i.strip().split(' ')
			singleInstDict = {}
			for fea in features:
				val = fea.strip().split(':')
				if len(val) < 2:
					label = float(val[0])
				else:
					singleInstDict[int(val[0])-1] = float(val[1])
				#get maximum number of features
				if maxvar < int(val[0]):
					maxvar = int(val[0])
			singleInstArr = np.array([[float(v)] for k,v in singleInstDict.items() if k!=-1])

			if self.initialData is None:
				self.initialData = singleInstArr
				self.initialDataLabels.append(label)
			elif self.initialData.shape[1] < initialSize:
				self.initialData = np.append(self.initialData, singleInstArr, axis=1)
				self.initialDataLabels.append(label)
			elif self.data is None:
				print("Finished Reading the Initial Data")
				self.data = singleInstArr
				self.dataLabels.append(label)
			else:
				self.data = np.append(self.data, singleInstArr, axis=1)
				self.dataLabels.append(label)

		return maxvar

	def __readDataArrCSV(self, filename, initialSize):
		data = pd.read_csv(filename, sep=',',header=None)
		self.initialData = np.transpose(data.values[0:initialSize, :-1]).astype(np.float32)

		self.initialDataLabels = data.values[0:initialSize, -1].tolist()

		self.data = np.transpose(data.values[initialSize:, :-1]).astype(np.float32)

		self.dataLabels = data.values[initialSize:, -1].tolist()
