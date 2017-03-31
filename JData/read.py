import csv
import pymysql
from JData.logger import Logger

file = open('data/JData_Action_201604.csv', encoding='utf-8')
csv_reader = csv.reader(file)

runLog = Logger('logs/run.log')
errorLog = Logger('logs/error.log')

# print(user_id, sku_id, time, mode_id, type, cate, brand)
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="jd_data", charset="utf8")
cur = conn.cursor()


def insert_db(user_id, sku_id, time, mode_id, type, cate, brand):
	if user_id == '':
		user_id = 0
	if sku_id == '':
		sku_id = 0
	if time == '':
		time = 0
	if mode_id == '':
		mode_id = 0
	if type == '':
		type = 0
	if cate == '':
		cate = 0
	if brand == '':
		brand = 0
	# 数据库连接
	sql = "insert into `jd_action` (user_id,sku_id,time,mode_id,type,cate,brand)" \
	      "VALUES (%s, %s, %s, %s, %s, %s, %s)"

	cur.execute(sql, (int(user_id), int(sku_id), time, int(mode_id), int(type), int(cate), int(brand)))
	conn.commit()

if __name__ == '__main__':
	number = 0
	for row in csv_reader:
		number += 1
		if number == 1:
			continue
		try:
			insert_db(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
		except Exception as e:
			errorLog.error('line ' + str(number) + ' data error: ' + e)

	conn.close()
