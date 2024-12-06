from API_Data.create_apt_caract import dataframe_accomodation
from Database.database import get_db,Base,engine
from Database.commit_to_db import commit_data_on_db

def main():
    Base.metadata.create_all(engine)
    commit_data_on_db(dataframe_accomodation(),db = get_db())

main()