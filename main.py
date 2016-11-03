from database.mongodb.mongodb import mongodb_connect
from database.mongodb.mongo_collections import create_collections
from database.redis.redis import redis_connection
from database.sql.sql_connection import sql_connection
from database.sql.sql_tables import sql_create_tables
from serviceA.service_A import serviceA
from serviceB.service_B import serviceB
from serviceC.service_C import serviceC
from serviceB.serviceE.service_E import serviceE
from serviceA.serviceD.service_D import serviceD
from serviceA.serviceD.serviceF.service_F import serviceF




mongodb_connect()
create_collections()
redis_connection()
sql_connection()
sql_create_tables()
serviceA()
serviceB()
serviceC()
serviceD()
serviceE()
serviceF()