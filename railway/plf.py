"""
读取列车运行数据并整合
车次|始发日期|起点站|终点站|日均定员|客座率
@author Panchao
"""

import os

import xlrd
import xlwt
from xlutils.copy import copy

from JData.logger import Logger

runLog = Logger('logs/run.log')
errorLog = Logger('logs/error.log')


def each_file(filePath):
	""" 遍历指定目录下所有的文件 """

	allFiles = []
	listDir = os.listdir(filePath)
	for dir in listDir:
		if os.path.isfile(os.path.join(filePath, dir)):
			allFiles.append(os.path.join(filePath, dir))
		else:
			allFiles += each_file(os.path.join(filePath, dir))
	return allFiles


def read_data(file):
	""" 按车次整合数据 """

	if os.path.isfile(file) is False:
		exit('file '+file+' not found')
	suffix = file.split('.')[-1]
	if suffix != ('xls' or 'xlsx'):
		exit('file type error, must .xls or .xlsx file')
	fileName = os.path.split(file)[1]

	runTime = fileName.split('.')[0]
	data = xlrd.open_workbook(file)
	sheet = data.sheet_by_name(u'Sheet1')
	# 总行数
	rowNumbers = sheet.nrows

	data = []

	for i in range(rowNumbers):
		if i > 1:
			rowValue = sheet.row_values(i)
			if '日均定员' in rowValue[0]:
				trainInfo = rowValue[0].split()
				# 车次
				trainNumber = trainInfo[0]
				if len(trainInfo) != 10:
					errorLog.error('运行时间 ' + runTime + ' 车次 ' + trainNumber + ' 客座率数据有误')
					continue
				# 车站范围
				train_range = trainInfo[1].split('—')
				# 始发站
				start_station = train_range[0]
				# 终点站
				end_station = train_range[1]
				# 日均定员
				person_average = trainInfo[6]
				# 客座率
				plf = trainInfo[-2]
				data.append([trainNumber, runTime, start_station, end_station, person_average, plf])
			if '客票席位汇总数据' in rowValue[0]:
				break

	return data


def write_file(values, file='plf.xls', startRow=0):
	""" 写入整合好的数据到文件 """

	old_data = xlrd.open_workbook(file)
	write = copy(old_data)
	write_sheet = write.get_sheet(0)

	# 列标题
	row_title = ['车次', '始发日期', '起点站', '终点站', '日均定员', '客座率']

	if startRow is 0:
		for x in range(len(row_title)):
			write_sheet.write(0, x, row_title[x])

	for i in range(len(values)):
		write_sheet.write(startRow + i + 1, 0, values[i][0])
		write_sheet.write(startRow + i + 1, 1, values[i][1])
		write_sheet.write(startRow + i + 1, 2, values[i][2])
		write_sheet.write(startRow + i + 1, 3, values[i][3])
		write_sheet.write(startRow + i + 1, 4, values[i][4])
		write_sheet.write(startRow + i + 1, 5, values[i][5])

	write.save(file)


if __name__ == '__main__':

	data_dir = 'data/201601-03'
	save_file = 'plf.xls'
	rowCounts = 0

	runLog.info('Run plf start, good luck!')

	if not os.path.isfile(save_file):
		runLog.info('not found ' + save_file + ' file, is helping you create')
		write = xlwt.Workbook()
		write_sheet = write.add_sheet('data', cell_overwrite_ok=True)
		write.save(save_file)
		runLog.info('create file ' + save_file + ' success!')

	files = each_file(data_dir)
	for i in range(len(files)):
		runLog.info('reading file ' + files[i] + '....')
		results = read_data(files[i])
		if i > 0:
			rowCounts += len(results)
		print(rowCounts)
		write_file(results, save_file, rowCounts)
		runLog.info('writing finished, total ' + str(len(results)))

	runLog.info('Run plf end, congratulation!')
