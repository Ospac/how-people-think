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
    
    def get_id(self,table):
        self.cursor.execute('select count(*) from {table}'.format(table=table))
        num_data = self.cursor.fetchall()
        return num_data[0][0]+1

    def insertDB(self,table, data):
        
            if table == 'history':
                sql = " INSERT INTO {table} VALUES ({id},\'{ts}\',\'{topic}\',{prob})".format(table=table,id=data[0],ts=data[1],topic=data[2],prob=data[3])
            try:
                self.cursor.execute(sql)
                self.db.commit()
            except Exception as e :
                print(" insert DB ",e)

    def readDB(self,table,topic):
        temp = []
        if table == 'history':
            sql = " SELECT ts, prob from {table} where topic = \'{topic}\'".format(table=table,topic=topic)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            result = (" read DB err",e)
        temp.append(result[0][0])
        temp.append(result[0][1])
        return temp
