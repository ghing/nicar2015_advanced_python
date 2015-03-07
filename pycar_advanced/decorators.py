from __future__ import print_function

def run_query(fn, db):
    """
    Decorator that decorates a function that returns a SQL string and
    executes the query using dataset's db.query() method
    """
    # TODO: Implement this function
    def inner(show_sql=False, dry_run=False):
        sql = fn()
        if show_sql:
            print(sql)
        
        if not dry_run:
            db.query(sql)

    return inner
