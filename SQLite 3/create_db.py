import sqlite3

# mengkoneksikan database, sekaligus membuat database jika file database tidak ada
conn = sqlite3.connect('data.db')

# supaya tidak ada lagi akses dari database sehingga tidak proses jalan terus menurus
conn.close()
