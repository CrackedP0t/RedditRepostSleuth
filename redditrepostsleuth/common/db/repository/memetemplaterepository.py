from typing import List

from redditrepostsleuth.common.model.db.databasemodels import MemeTemplate


class MemeTemplateRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def add(self, item):
        self.db_session.add(item)

    def get_all(self) -> List[MemeTemplate]:
        return self.db_session.query(MemeTemplate).all()