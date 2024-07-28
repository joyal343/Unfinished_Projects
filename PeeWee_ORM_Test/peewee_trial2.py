from peewee import *
from datetime import date

db = SqliteDatabase('emp1')

class BaseModel(Model):
    class Meta:
        database = db

class EmpDet(BaseModel):
    empId = AutoField()
    name = CharField()
    managerId = IntegerField()
    dateOfJoining = DateField()
    city = CharField()

class EmpSal(BaseModel):
    emp = ForeignKeyField(EmpDet, backref='employees')
    project = CharField()
    salary = IntegerField()
    var = IntegerField()

# db.create_tables([EmpDet,EmpSal])
print("SELECT STATEMENT 1")
for emp in EmpDet.select().where(EmpDet.city == "C"):
    print(emp.name)

print("SELECT STATEMENT 2")
query = (EmpDet
            .select(EmpDet,EmpSal)
            .join(EmpSal,JOIN.LEFT_OUTER))# include people without pets
for emp in query:
    if hasattr(emp,'empsal'): # tb name lower 
        print(emp.name+' '+emp.empsal.project)
    else:
        print(emp.name+' '+'no project!')

print("Employee's who joined in 2022")

query = (EmpDet
            .sele)
# x = EmpDet.create(
#     name = "JSW" ,
#     managerId = 321,
#     dateOfJoining = date(2012,1,21),
#     city='T'
# )
# y = EmpDet.create(
#     name = "WW" ,
#     managerId = 986,
#     dateOfJoining = date(2020,1,30),
#     city='C'
# )
# z = EmpDet.create(
#     name = 'KR',
#     managerId = 876,
#     dateOfJoining = date(2021,11,27),
#     city = 'ND'
# )
# w = EmpDet.create(
#     name = 'JR',
#     managerId = 876,
#     dateOfJoining = date(2022,11,21),
#     city = 'TR'
# )

# EmpSal.create(
#     emp = x,
#     project = "P1",
#     salary = 8000,
#     var = 500
# )
# EmpSal.create(
#     emp = y,
#     project = "P2",
#     salary = 10000,
#     var = 1000
# )
# EmpSal.create(
#     emp = z,
#     project = "P1",
#     salary = 12000,
#     var = 0
# )




