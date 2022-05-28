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
            sql = " INSERT INTO HISTORY VALUES ({id},\'{ts}\',\'{topic}\',{prob})".format(id=data['id'],ts=data['ts'],topic=data['topic'],prob=data['prob'])
            self.execute(sql)
            
            # step2 : insert data into 'keywords' table
            for key in keywords:
                for word in keywords[key]:
                    sql = "INSERT INTO KEYWORDS VALUES ({id},\'{type}\',\'{word}\')".format(id=data['id'],type=key,word=word)
                    self.execute(sql)

    def get_history(self,topic):
        ts = []
        prob = []
        sql = " SELECT ts, prob from history where topic = \'{topic}\'".format(topic=topic)
        self.execute(sql)
        result = self.cursor.fetchall()
        print(result)
        for i in result:
            ts.append(i[0])
            prob.append(i[1])
        dict={'ts':ts, 'prob':prob}
        return dict

    def get_keywords(self,topic, ts):
        pos=[]
        neg=[]
        neu=[]
        self.cursor.execute(" SELECT id from history where topic = \'{topic}\' and ts= \'{ts}\'".format(topic=topic, ts = ts))
        result = self.cursor.fetchall()
        id = result[0][0]

        sql = " SELECT type, word from keywords where id = \'{id}\'".format(id=id)
        self.execute(sql)
        result = self.cursor.fetchall()
        for i in result:
            if i[0]=='positive':
                pos.append(i[1])
            elif i[0]=='negative':
                neg.append(i[1])
            else:
                neu.append(i[1])
        dict={'positive':pos,'negative':neg,'neutral':neu}
        return dict
