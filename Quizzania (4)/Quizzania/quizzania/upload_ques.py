from sqlalchemy import *
from datetime import datetime
engine = create_engine('mysql://root:@localhost/quizzania_db')


meta = MetaData()
ques = Table(
    'ques', meta,
    Column('SNo', Integer, primary_key=True),
    Column('ques', String(100)),
    Column('opt1', String(30)),
    Column('opt2', String(30)),
    Column('opt3', String(30)),
    Column('opt4', String(30)),
    Column('Correct', String(30)),
    Column('datetime', DateTime)
)
meta.create_all(engine)


def ques_upload():
    val = []
    with open("questions.txt", "rt") as my_file:
        counter = 1
        for line in my_file:
            if counter % 7 == 0:
                counter = 1
                val.clear()
                continue
            val.append(line)
            if counter % 6 == 0:
                ins = ques.insert().values(ques=val[counter-6], opt1=val[counter-5], opt2=val[counter-4], opt3=val[counter-3], opt4=val[counter-2], Correct=val[counter-1], datetime=datetime.now())
                conn = engine.connect()
                conn.execute(ins)
            counter += 1


ques_upload()
