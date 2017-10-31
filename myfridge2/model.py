
#def connect_db():
#    rv = sqlite3.connect(app.config['DATABASE'])
#    rv.row_factory = sqlite3.Row
#    return rv
#
#def get_db():
#    if not hasattr(g, 'sqlite_db'):
#        g.sqlite_db = connect_db()
#    return g.sqlite_db
#
#@app.teardown_appcontest
#def close_db(error):
#    if hasattr(g, 'sqlite_db'):
#        g.sqlite_db.close()
#
#def init_db():
#    db = get_db()
#    with app.open_resource('schema.sql', mode='r') as f:
#        db.cursor().executescript(f.read())
#
#    db.commit()
#
#@app.cli.command('initdb')
#def initdb_command():
#    init_db()
#    print('Database initialized')
