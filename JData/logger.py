"""
logger 封装
@author panchao
"""
import logging


class Logger:

	def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):

		self.logger = logging.getLogger(path)
		self.logger.setLevel(logging.DEBUG)
		fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

		# CMD日志
		sh = logging.StreamHandler()
		sh.setFormatter(fmt)
		sh.setLevel(clevel)

		# 文件日志
		fh = logging.FileHandler(path,  encoding="UTF-8")
		fh.setFormatter(fmt)
		fh.setLevel(Flevel)
		self.logger.addHandler(sh)
		self.logger.addHandler(fh)

	def debug(self, message):
		self.logger.debug(message)

	def info(self, message):
		self.logger.info(message)

	def war(self, message):
		self.logger.warn(message)

	def error(self, message):
		self.logger.error(message)
