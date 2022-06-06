import sqlite3
# creating database
connection=sqlite3.connect('web_services.db')
print("database loaded successfully") # just to be sure that database is in operation
cursor=connection.cursor()
#table providers
cursor.execute(''' CREATE TABLE if not exists providers
                (provider_id integer PRIMARY KEY,
                comp_name text NOT NULL,
                address text NOT NULL,
                country text NOT NULL,
                pwd text NOT NULL);''')
print("providers loaded successfully")
#table customer
cursor.execute('''create table if not exists customer
                (mobile_no integer PRIMARY KEY,
                pwd text NOT NULL,
                name text NOT NULL,
                email text NOT NULL,
                cust_plan text CHECK(cust_plan IN ('basic','premium','blacklisted')) DEFAULT'basic' ); ''')
print("customers loaded successfully")
#table contents
cursor.execute('''create table if not exists contents
                ( content_id integer PRIMARY KEY,
                title text NOT NULL,
                details text NOT NULL,
                rating real NOT NULL,
                url text NOT NULL,
                status text CHECK(status IN ('ACTIVE','INACTIVE')) DEFAULT'ACTIVE',
                provider_id integer,
                ac_detail text NOT NULL,
                price_per_unit real NOT NULL,
                FOREIGN KEY(provider_id) REFERENCES providers(provider_id))''')
print("content loaded successfully")
#table orders
cursor.execute('''create table if not exists orders
               (mobile_no integer,
               order_id integer PRIMARY KEY autoincrement,
               content_id integer,
               quantity integer default 1,
               comment text default"none",
               FOREIGN KEY(mobile_no) REFERENCES customer(mobile_no),
               FOREIGN KEY(content_id) REFERENCES content(content_id));''')
print("orders loaded successfully")
cursor.execute('''insert into providers
               values(112210,"AMAZON","13 SILICON VALLEY","USA","1234"),
               (124510,"SPOTIFY","14 SILICON VALLEY","USA","5678"),
               (989151,"NETFLIX","15 SILICON VALLEY","USA","9632"),
               (745892,"MICROSOFT","16 SILICON VALLEY","USA","7412"),
               (814332,"ADOBE","17 SILICON VALLEY","USA","1589"),
               (100000,"OWN","HERE","IND","0151")''')
print("provider_data retrived successfully")
cursor.execute("""insert into contents values(11200,"AMAZON PRIME","1 YR AMAZON PRIME",4.5,"SW123CD","ACTIVE",112210,"QAZ3429",8.52),
                (11300,"AMAZON VMS","1 YR AMAZON VMS",5,"SM321CV","ACTIVE",112210,"QAZ3492",12.34),
               (11003,"SPOTIFY 1MONTH","SPOTIFY 1 MON",3,"QS221GB","INACTIVE",124510,"QAZ8339",1.22),
               (11004,"SPOTIFY 3 MON","SPOTIFY 3 MON",4,"ZS665VN","ACTIVE",124510,"QAZ9333",3.14),
               (11005,"SPOTIFY 1 YR","SPOTIFY 1 YR",5,"MN554HB","ACTIVE",124510,"QAZ1029",5.14),
               (12100,"NETFLIX 3 MON","NETFLIX 3 MON",4.25,"BB733JN","ACTIVE",989151,"QAZ1392",4.78),
               (12101,"NETFLIX 1 YR","NETFLIX 1 YR",5,"VV767MN","ACTIVE",989151,"QAZ4355",9.98),
               (13554,"MICROSOFT OFF","MICROSOFT 365 1YR",5,"HH664BG","ACTIVE",745892,"QAZ1233",5.11),
               (13555,"WIN 10","WIN 10 PRO",5,"VG277MN","ACTIVE",745892,"QAZ8339",28.44),
               (14221,"CREATIVE CLOUD","CREATIVE CLOUD 1 YR",3.5,"CV772BH","ACTIVE",814332,"QAZ2233",9.11),
               (14222,"STUDENT","STUDENT EDITION 1YR",4,"FD773FF","ACTIVE",814332,"QAZ1344",3.14),
               (10000,"EPIC","CREATIVE CLOUD,WIN 10,NETFLIX 1YR,OFFICE 365,SPOTIFY 1YR,AMAZON AWS, PRIME ",5,"ED2323DD","ACTIVE",100000,"QAZ0001",54.35);""")
print("content_data retrived successfully")
cursor.execute("""insert into customer
               values(909,'xyz','alan','ljf@gj.com','basic'),
               (998,"abc","smith","wwe@fi.com","blacklisted"),
               (458,"ooe","john","wie@jds.com","premium"),
               (453,"kwj","effiel","jee@djd.com","basic"),
               (755,"kwe","jonathan","ef@kdf.com","basic");""")
print('customer data retrived successfully')
cursor.execute("""insert into orders(mobile_no,content_id,quantity,comment)
                values(909,11005,1,null),
                (909,12100,1,'SIGN IN PROBLEM'),
                (998,14222,2,'2ND ID @ D2@JDS.COM'),
                (755,13555,1,NULL),
                (755,14222,1,NULL),
                (998,10000,1,NULL);""")
print("orders data retrived successfully")
connection.commit()
