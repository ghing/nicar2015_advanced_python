from pycar_advanced.db import get_default_db
from pycar_advanced.decorators import run_query

db = get_default_db()     

@run_query(db)
def candidates():
    # TODO: Implement this
    return ""
