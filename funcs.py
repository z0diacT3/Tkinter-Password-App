import sqlite3
from tkinter import *

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS sites
            (site_name text,
            site_url text,
            site_email text,
            site_username,
            site_password,
            site_notes
            )""")
        self.conn.commit()

    def s_all(self):
        self.c.execute("SELECT oid, * FROM sites")
        rows = self.c.fetchall()
        return rows
        
    def a_site(self, name, url, email, username, password, notes):
        self.c.execute("INSERT INTO sites VALUES (?,?,?,?,?,?)",
            (name, url, email, username, password, notes)
            )
        self.conn.commit()

    def u_site(self, id, name, url, email, username, password, notes):
        self.c.execute("""UPDATE sites SET
            site_name = :name,
            site_url = :url,
            site_email = :email,
            site_username = :username,
            site_password = :password, 
            site_notes = :notes
            WHERE oid = :id""",{
                "name": name,
                "url": url,
                "email": email,
                "username": username,
                "password": password,
                "notes": notes,
                "id": id})
        self.conn.commit()
    
    def d_site(self, id):
        self.c.execute("DELETE FROM sites WHERE oid=?", (id,))
        #print(f"Received ID {id}")
        self.conn.commit()

    def __del__(self):
        self.conn.close()
