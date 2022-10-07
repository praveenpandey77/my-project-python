from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://whv0mps52tdik0qyx5la:pscale_pw_3pd3RMotmgKLrFhfx40Y7UhUVvchWevXFINxk0S98CK@ap-south.connect.psdb.cloud/its-my-project?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())

result_dict = []
for row in result.all():
    result_dict.append(dict(row))
print(result_dict)
