from flask            import Flask, jsonify, request
from psycopg2         import Error as PGError
from teamhack_db.sql  import drop_row_hostname_recordtype, drop_row_hostname, drop_row_ip, insert, select_hostname_recordtype, select_hostname, select_ip
from teamhack_db.util import get_name, get_record_type

def dispatch(data, hostname_recordtype_cb, hostname_cb, ip_cb):
  if 'host' in data and 'type' in data:
    host = data['host']
    host = get_name(host)
    rt   = data['type']
    rt   = get_record_type(rt)
    assert rt is not None
    assert rt != ''
    assert rt
    print(f"hostname_recordtype_cb(host={host}, type={data['type']} ({rt}))")
    ret  = hostname_recordtype_cb(conn, host, rt)
    return ret
  if 'host' in data and 'type' not in data:
    host = data['host']
    host = get_name(host)
    print(f'hostname_cb(host={host})')
    ret  = hostname_cb(conn, host)
    return ret
  if 'inet' in data:
    addr = data['inet']
    print(f'ip_cb(addr={addr})')
    ret  = ip_cb(conn, addr)
    return ret
  return '', 404

def create_app(conn):
  app = Flask(__name__)
  #api = Api(app)

  @app.route('/create', methods=['POST'])
  def add():
    data = request.get_json(force=True)
    if 'host' not in data: return '', 404
    host = data['host']
    host = get_name(host)
    print(f"add(host={host})")
    if 'type' not in data: return '', 404
    rt   = data['type']
    print(f"add(type={rt})")
    rt   = get_record_type(rt)
    assert rt
    if 'inet' not in data: return '', 404
    addr = data['inet']
    print(f"insert(host={host}, type={data['type']}, addr={addr})")
    try:
      ret = insert(conn, host, rt, addr)
      conn.commit()
      #return ret
      return ''
    except PGError as e:
      print(f"Error: {e}")
      conn.rollback()
      return 'DB Error', 204

  @app.route('/retrieve', methods=['POST'])
  def retrieve():
    data = request.get_json(force=True)
    return dispatch(data, select_hostname_recordtype, select_hostname, select_ip)

  @app.route('/update', methods=['POST'])
  def update():
    # TODO
    return 'Not Implemented', 404

  @app.route('/delete', methods=['POST'])
  def delete():
    data  = request.get_json(force=True)
    try:
      ret = dispatch(data, drop_row_hostname_recordtype, drop_row_hostname, drop_row_ip)
      conn.commit()
      return ''
    except PGError as e:
      print(f"Error: {e}")
      conn.rollback()
      return 'DB Error', 204

  return app

def start_server(conn, host="0.0.0.0", port=5001, *args, **kwargs):
  app = create_app(conn)
  app.run(debug=True, host=host, port=port, *args, **kwargs)

