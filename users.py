import sqlite3

class User():
	def __init__(self):
		self.conn = sqlite3.connect('thenewwall.db')
		self.cursor = self.conn.cursor()


	def new(self, username, password):
		query = "INSERT INTO user(username,password) VALUES(?,?)"
		data = (username,password)
		self.cursor.execute(query, data)
		self.conn.commit()
		self.conn.close()

	def login(self, username, password):
		query = "SELECT * FROM user where username = ? " 
		self.cursor.execute(query, (username,))
		result = self.cursor.fetchone()
		self.conn.close()
		if password == result[1]:
			return True
		else:
			return False
