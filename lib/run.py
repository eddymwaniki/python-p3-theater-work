from models import session, Role, Audition

#Creating role
role2 = Role("Tyler Durden")
session.add(role2)
session.commit()

#Creating auditions
audition6 = Audition(actor= "Leonardo DiCaprio",location = "LA", phone = 678247386482, hired=False, role= role2)
audition7 = Audition(actor= "Brad Pitt", location = "LA", phone = 99798698676, hired=False, role =role2)
audition8 = Audition(actor = "Christian Bale", location = "LA", phone = 886756564657, hired = False ,role = role2)
session.add(audition6)
session.add(audition7)
session.add(audition8)
session.commit()

#Hire an actor
audition7.call_back()
audition8.call_back()

#Check lead
print(role2.lead())

#Check understudy
print(role2.understudy())
