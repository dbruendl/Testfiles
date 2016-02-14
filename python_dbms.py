__author__ = 'Meins'

# base class of all declarative classes
Base = declarative_base()
# table person
class Person(Base):
 __tablename__ = 'person'
 # pk
 id = Column(Integer, primary_key=True)
 # attribute
 name = Column(String)
# table address
class Address(Base):
 __tablename__ = 'address'
 # pk
 id = Column(Integer, primary_key=True)
 # attribute
 address = Column(String)
 # attribute and foreign key
 person_id = Column(Integer, ForeignKey(Person.id))
 person = relationship(Person)
# create_engine
engine = create_engine('sqlite:///')
# create session
s = Session(engine)


Base.metadata.create_all(engine)
# create an instance of person (record in table person)
p = Person(name='mayer')
# add it to the session (SQL INSERT statement)
s.add(p)
# create an instance of address (record in table address)
a = Address(address='Baumgasse 4', person=p)
# add it to the session (SQL INSERT statement)
s.add(a)
# get the first record of table person
p = s.query(Person).one()
# print query
print ("%r, %r" % (p.id, p.name))
# 1, 'mayer'
# get the corresponding record of table address
a = s.query(Address).filter(Address.person == p).one()
print ("%r, %r" % (a.id, a.address))
# 1, 'Baumgasse 4'
# commit the current transaction
s.commit()
# close the current transaction
s.close()
