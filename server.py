
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
    value = Float()


TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE =20

server = socket(AF_INET, SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))
server.listen(5) #we are doing one connection at a time

conn, addr = server.accept()
print 'Connections address', addr

#once we are returning values from the in memory DB do away with the list data_store
data_store = []

while True:
    data = conn.recv(BUFFER_SIZE)
    if data:
        try:
            data_list=[float(x) for x in data.split(',')]
        except ValueError:
            conn.send('please input a interger, float or both datatypes seperated by a comma')

        else:
            for x in data_list:
                data_store.append(x)
                number = Number()
                number.value = x
                store.add(number)
                store.commit()
            print data_store
            value = reduce(lambda x ,y: x+y, data_store)/len(data_store)
            conn.send(str(value))


conn.close()