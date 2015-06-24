
from socket import *
from storm.locals import *


#create the DB and the table within the DB. In memory DB
database = create_database("sqlite:")
store = Store(database)
store.execute("CREATE TABLE numbers "
            "(id INTEGER PRIMARY KEY, value FLOAT)")

#create a class which maps the the Number table within the DB
class Number(object):
    __storm_table__ ='numbers'
    id = Int(primary=True)
    #Using floats instead of decimals as we do not know the level of accuracy needed
    value = Float()


TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 20 #We can set this to a larger size in the future if needed

server = socket(AF_INET, SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))
server.listen(5) #Server can deal with 5 connections at one time

conn, addr = server.accept()
print 'Connections address', addr


while True:
    data = conn.recv(BUFFER_SIZE)
    if data:
        try:
            #Data comes from the client in string format, this is then split and made into a list of floats
            data_list=[float(x) for x in data.split(',')]
        except ValueError:
            #If Data sent by the client is not in the correct format then a error message is sent back
            #This error message could be more informative and the validation checks could also be better if give more use cases
            conn.send('please input a interger, float or both datatypes seperated by a comma')

        else:
            for x in data_list:
                #store all the numbers sent by the client into the DB
                number = Number()
                number.value = x
                store.add(number)
                store.commit()

            result = store.find(Number)

            #DB query to return a list of Number.values
            sql_data_store = [number.value for number in result]

            print 'list of Number.values within DB :',  sql_data_store
            value = reduce(lambda x ,y: x+y, sql_data_store)/len(sql_data_store)
            conn.send(str(value))


conn.close()