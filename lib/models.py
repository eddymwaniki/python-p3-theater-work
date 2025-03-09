from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///auditions_role.db")

Session = sessionmaker(bind=engine)
session = Session()

class Audition(Base):
    __tablename__ = "auditions"

    id = Column(Integer(), primary_key = True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean(), default = False)

    role_id = Column(Integer(), ForeignKey("roles.id"))
    role = relationship("Role", back_populates = "auditions")

    def call_back(self) :
        self.hired = True
        session.add(self)
        session.commit()
    def __repr__(self):
        return f"ACTOR : {self.id} : {self.actor} PHONE : {self.phone}"

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer(), primary_key = True)
    character_name = Column(String())

    auditions = relationship("Audition", back_populates = "role")

    @property
    def actors(self):
        return [audition.actor for audition in self.auditions]  

    @property
    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self) :
        hired_auditions = [audition for audition in self.auditions if audition.hired == True]  
        return hired_auditions[0] if hired_auditions else "no actor has been hired for this role."

    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired == True]
        return hired_auditions[1] if len(hired_auditions) > 1 else "no actor has been hired for understudy for this role."          

    def __repr__(self) :
        return f"CHARACTER : {self.character_name}"       

Base.metadata.create_all(engine)        





