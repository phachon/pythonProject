"""
将客座率数据转换成矩阵形式
@author Panchao
"""

import os

import xlrd
import xlwt
from xlutils.copy import copy

from JData.logger import Logger

runLog = Logger('logs/run.log')
errorLog = Logger('logs/error.log')


def read_data(file):
	""" 读取plf数据 """

	if os.path.isfile(file) is False:
		exit('file '+file+' not found')
	suffix = file.split('.')[-1]
	if suffix != ('xls' or 'xlsx'):
		exit('file type error, must .xls or .xlsx file')

	data = xlrd.open_workbook(file)
	sheet = data.sheet_by_name(u'data')
	# 总行数
	rowNumbers = sheet.nrows

	train_numbers = []
	runTimes = []
	data = []

	for i in range(rowNumbers):
		rowValue = sheet.row_values(i)
		if len(rowValue) is 0:
			continue
		if rowValue[0] == '车次':
			continue
		train_number = rowValue[0]
		runTime = rowValue[1]
		plf = rowValue[5]

		if train_number not in train_numbers:
			train_numbers.append(train_number)

		if runTime not in runTimes:
			runTimes.append(runTime)

		row = train_numbers.index(train_number) + 1
		line = runTimes.index(runTime) + 1

		data.append([line, row, plf])

	for x in range(len(runTimes)):
		data.append([x+1, 0, runTimes[x]])
	for y in range(len(train_numbers)):
		data.append([0, y+1, train_numbers[y]])

	runLog.info("读取数据完成, 总共 " + str(len(data)))
	return data


def write_file(data, file='plf_matrix.xls'):
	""" 写入数据 """

	old_data = xlrd.open_workbook(file)
	write = copy(old_data)
	write_sheet = write.get_sheet(0)

	for i in range(len(data)):
		write_sheet.write(data[i][0], data[i][1], data[i][2])
		runLog.info("写入第" + str(i) + "条数据")
	write.save(file)

if __name__ == '__main__':

	old_file = '2015plf.xls'
	save_file = '2015plf_matrix.xls'

	if not os.path.isfile(save_file):
		runLog.info('not found ' + save_file + ' file, is helping you create')
		write = xlwt.Workbook()
		write_sheet = write.add_sheet('data', cell_overwrite_ok=True)
		write.save(save_file)
		runLog.info('create file ' + save_file + ' success!')

	data = read_data(old_file)
	write_file(data, save_file)

	runLog.info('Run plf_to_matrix end, congratulation!')

