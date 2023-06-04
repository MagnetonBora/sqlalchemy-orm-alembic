from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from alembic import context

config = context.config
engine = engine_from_config(
    config.get_section(config.config_ini_section, {}),
    prefix="sqlalchemy.",
)

Session = sessionmaker(bind=engine)
session = Session()


def commit_on_success(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        session.commit()
        return result
    return wrapper
