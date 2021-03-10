from sqlalchemy.orm.session import sessionmaker
from base import Base

def sess(function): # creates a session and shares that session with the function in call.
                                # ensures a clean transaction
    def wrapper():
        Session = sessionmaker(bind=Base.engine)
        session = Session()
        try:
            function(session)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return wrapper

    return wrapper
