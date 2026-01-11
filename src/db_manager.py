import pymysql
from datetime import date

class DiaryDB:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='1191',
            db='my_diary_db',
            charset='utf8mb4'
        )
        self.curs = self.conn.cursor()

    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS entries(
                id INT AUTO_INCREMENT PRIMARY KEY,
                date DATE NOT NULL,
                content TEXT NOT NULL,
                created_at DATETIME DEFAULT NOW()
            )
        """

        self.curs.execute(sql)
        self.conn.commit()
    
    def add_entry(self, content): 
        today = date.today()
        sql = "INSERT INTO entries (date, content, created_at) VALUES (%s, %s, NOW())"
        self.curs.execute(sql, (today, content))
        self.conn.commit()
    
    def get_all_entries(self):
        sql = "SELECT id, date, content FROM entries ORDER BY date DESC"
        self.curs.execute(sql)
        return self.curs.fetchall()
    
    def update_entry(self, entry_id, new_content):
        sql = "UPDATE entries SET content = %s WHERE id = %s"
        self.curs.execute(sql, (new_content, entry_id))
        self.conn.commit()
        return self.curs.rowcount > 0 
    
    def delete_entry(self, entry_id):
        sql = "DELETE FROM entries WHERE id = %s"
        self.curs.execute(sql, (entry_id,))
        self.conn.commit()
        return self.curs.rowcount > 0
    
    def close(self):
        self.conn.close()