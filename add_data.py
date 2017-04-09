from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, UserAccounts, UserProfiles, Teams, Lists, ListItems, Messages, TeamMembers, Events, Comments

engine = create_engine('sqlite:///event_database.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

user=UserAccounts(username="skb1129", password="29nov1997", acc_type="master")

session.add(user)
session.commit()

userprof=UserProfiles(f_name="Surya Kant", l_name="Bansal", dob="29/11/1997", mobile="9814068029", gender="M", rollno="1510991666", email="skb1129@yahoo.com", user_accounts=user)

session.add(userprof)
session.commit()

event1=Events(title="Sample Event", type="ongoing", starts="21/04/2017", ends="23/04/2017", description="it is a good event. you will enjoy it.", contact="me", club="dexter's", post_date="28/03/2017")

session.add(event1)
session.commit()

team1=Teams(name="avengers", user_accounts=user)

session.add(team1)
session.commit()

list1=Lists(title="items", events=event1, teams=team1)

session.add(list1)
session.commit()

listitem1=ListItems(item="car", lists=list1)

session.add(listitem1)
session.commit()

message1=Messages(title="first message", message="you piece of shit", events=event1, teams=team1)

session.add(message1)
session.commit()

print "all done"
