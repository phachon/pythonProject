import csv
import mysql.connector

file = open('data/JData_Action_201604.csv', encoding='utf-8')

csv_reader = csv.reader(file)

for row in csv_reader:
	user_id = row[0]
	sku_id = row[1]
	time = row[2]
	model_id = row[3]
	type = row[4]
	cate = row[5]
	brand = row[6]
	print(row)


def insert_db(user_id, sku_id, time, model_id, type, cate, brand):
	if user_id == '':
		user_id = 0
	if sku_id == '':
		sku_id = 0
	if time == '':
		time = 0
	if model_id == '':
		model_id = 0
	if type == '':
		type = 0
	if cate == '':
		cate = 0
	if brand == '':
		brand = 0
		# 数据库连接
	conn = mysql.connector.connect(user='root', password='123456', database='bms_account')