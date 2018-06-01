import csv
import sqlite3


conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS ratings
             (movieId text, userId text, rating real, timestamp timestamp)''')

with open('./ml-20m/ratings.csv') as csvfile:
    #fieldnames = ['UserID', 'MovieID', 'Rating', 'Timestamps']
    reader = csv.DictReader(csvfile)
    for row in reader:
        #import pdb; pdb.set_trace()
        print('importing rows {}'.format(row))
        c.execute("INSERT INTO ratings VALUES ({})".format(','.join(row.values())))
        conn.commit()