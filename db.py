from operator import truediv
from time import time
import psycopg2

class DB:
    def __init__(self):
        #connection to postgresql DB
        self.db = psycopg2.connect(host = 'localhost',
                            dbname = 'team6',
                            user='team6',
                            password = 'team6',
                            port='5432')

        #create cursor to execute query
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def commit(self):
        self.cursor.commit()


    def get_timestamp(self):
        self.cursor.execute("""SELECT CURRENT_TIMESTAMP""")
        ts = self.cursor.fetchall()
        
        return str(ts[0][0])[:16]
    def execute(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print(" insert DB ",e)

    def get_id(self,table):
        self.cursor.execute('select count(*) from {table}'.format(table=table))
        num_data = self.cursor.fetchall()
        return num_data[0][0]+1

    def insertDB(self,data,keywords):
            # step1 : insert data into 'HISTORY' table
            sql = " INSERT INTO HISTORY VALUES ({id},\'{ts}\',\'{topic}\',{pos_prob},{neg_prob},{neu_prob})".format(id=data['id'],ts=data['ts'],
                                    topic=data['topic'],pos_prob=data['pos_prob'],neg_prob=data['neg_prob'],neu_prob=data['neu_prob'])
            self.execute(sql)
            
            # step2 : insert data into 'keywords' table
            for word in keywords:
                    sql = "INSERT INTO KEYWORDS VALUES ({id},\'{word}\')".format(id=data['id'],word=word)
                    self.execute(sql)

    def history_exist(self,topic):
        timestamps = self.get_history(topic)['ts']
        if len(timestamps)!=0:
            for ts in timestamps:
                date = ts[:10]
                sql = "select (current_date - to_date(\'{date}\',\'yyyy-mm-dd\'))".format(date=date)
                self.execute(sql)
                temp = self.cursor.fetchall()
                for t in temp:
                    if t[0]<=7: return True
        return False
     


    def get_history(self,topic):
        ts = []
        pos_prob = []
        neg_prob=[]
        neu_prob=[]
        sql = " SELECT ts, pos_prob, neg_prob, neu_prob from history where topic = \'{topic}\'".format(topic=topic)
        self.execute(sql)
        result = self.cursor.fetchall()
        for i in result:
            ts.append(i[0])
            pos_prob.append(i[1])
            neg_prob.append(i[2])
            neu_prob.append(i[3])
        dict={'ts':ts, 'pos_prob':pos_prob,'neg_prob':neg_prob,'neu_prob':neu_prob}
        return dict

    def get_keywords(self,topic, ts):
        temp=[]
        self.cursor.execute(" SELECT id from history where topic = \'{topic}\' and ts= \'{ts}\'".format(topic=topic, ts = ts))
        result = self.cursor.fetchall()
        id = result[0][0]

        sql = " SELECT word from keywords where id = \'{id}\'".format(id=id)
        self.execute(sql)
        result = self.cursor.fetchall()
        for i in result:
            temp.append(i[0])
        
        return temp
