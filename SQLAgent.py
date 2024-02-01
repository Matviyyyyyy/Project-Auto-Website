import sqlite3

class SQLAgent:
    def __init__(self, name_db):
        self.db = sqlite3.connect(name_db)
        self.create_tables()
        self.create_tables_2()
        self.create_tables_3()
        self.create_tables_4()


    def create_tables(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS LogoCars (        
            id_logo INTEGER PRIMARY KEY,
            name_logo TEXT,
            name_page_a TEXT,
            href_car_a TEXT,
            img_logo_name TEXT
            )
            
        ''')

    def create_tables_2(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS BrandCars (        
            id_car INTEGER PRIMARY KEY,
            car_brand TEXT,  
            type_brand TEXT,
            car_price TEXT,
            img_car TEXT,
            main_description TEXT,
            kyzov_type TEXT,
            engine_volume INTEGER,
            type_engine TEXT,
            engine_power TEXT,
            torque TEXT,
            transmission_type TEXT,
            pruvid_system TEXT,
            pidviska_front TEXT,
            pidviska_back TEXT,
            max_speed INTEGER,
            improve_speed TEXT,
            fuel_use_city TEXT,
            fuel_use_nocity TEXT,
            fuel_use_mix TEXT,
            volume_tank INTEGER,
            spor_masa INTEGER,
            max_masa INTEGER,
            length INTEGER,
            width INTEGER,
            height INTEGER,
            kolisna_base INTEGER,
            min_klirens INTEGER,
            trunk_volume INTEGER,
            img_up_car TEXT,
            year INTEGER,
            img_one_gallery TEXT,
            img_two_gallery TEXT,
            img_three_gallery TEXT,
            img_four_gallery TEXT
            )
        ''')

    def create_tables_4(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (        
            id_user INTEGER PRIMARY KEY,
            name_user TEXT,
            sub_name TEXT,
            tel_user TEXT,
            email_user TEXT,
            password_user TEXT
            )
        ''')

    def create_tables_3(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS NewsCards (        
            id_new INTEGER PRIMARY KEY,
            txt_new TEXT,
            date_new TEXT,
            img_new TEXT
            )

        ''')
        self.db.commit()

    def add_brand_car(self, car_brand, type_brand, car_price, img_car, main_description, kyzov_type, engine_volume, type_engine, engine_power, torque,transmission_type, pruvid_system, pidviska_front, pidviska_back, max_speed, improve_speed, fuel_use_city, fuel_use_nocity, fuel_use_mix, volume_tank, spor_masa, max_masa, length, width, height, kolisna_base, min_klirens, trunk_volume, img_up_car, year, img_one_gallery, img_two_gallery, img_three_gallery, img_four_gallery):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO  BrandCars(car_brand, type_brand, car_price, img_car, main_description, kyzov_type, engine_volume, type_engine, engine_power, torque,transmission_type, pruvid_system, pidviska_front, pidviska_back, max_speed, improve_speed, fuel_use_city, fuel_use_nocity, fuel_use_mix, volume_tank, spor_masa, max_masa, length, width, height, kolisna_base, min_klirens, trunk_volume, img_up_car, year, img_one_gallery, img_two_gallery, img_three_gallery, img_four_gallery) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [car_brand, type_brand, car_price, img_car, main_description, kyzov_type, engine_volume, type_engine, engine_power, torque,transmission_type, pruvid_system, pidviska_front, pidviska_back, max_speed, improve_speed, fuel_use_city, fuel_use_nocity, fuel_use_mix, volume_tank, spor_masa, max_masa, length, width, height, kolisna_base, min_klirens, trunk_volume, img_up_car, year, img_one_gallery, img_two_gallery, img_three_gallery, img_four_gallery])
        cursor.close()
        self.db.commit()


    def add_logo(self, name_logo, name_page_a, href_car_a, img_logo_name):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO  LogoCars(name_logo, name_page_a, href_car_a, img_logo_name) VALUES(?, ?, ?, ?)', [name_logo, name_page_a, href_car_a, img_logo_name])
        cursor.close()
        self.db.commit()
    def get_all(self):
        cursor = self.db.cursor()
        query = "SELECT * FROM LogoCars"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result


    def get_all_cars(self):
        cursor = self.db.cursor()
        get_cars = "SELECT * FROM BrandCars"
        cursor.execute(get_cars)
        result2 = cursor.fetchall()
        cursor.close()
        return result2

    def add_new(self, txt_new, date_new, img_new):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO  NewsCards(txt_new, date_new, img_new) VALUES(?, ?, ?)', [txt_new, date_new, img_new])
        cursor.close()
        self.db.commit()
    def get_news(self):
        cursor = self.db.cursor()
        get_news = "SELECT * FROM NewsCards"
        cursor.execute(get_news)
        result3 = cursor.fetchall()
        cursor.close()
        return result3

    def get_filtred_cars_year(self, year):
        cursor = self.db.cursor()
        query = "SELECT * FROM BrandCars  WHERE year = ?"
        cursor.execute(query, [year])
        result4 = cursor.fetchall()
        cursor.close()
        return result4

    def get_filtred_cars_drive_type(self, kyzov_type):
        cursor = self.db.cursor()
        query = "SELECT * FROM BrandCars WHERE kyzov_type = ?"
        cursor.execute(query, [kyzov_type])
        result7 = cursor.fetchall()
        cursor.close()
        return result7


    def add_user(self, name_user, sub_user, tel_user, email_user, password_user):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO  Users(name_user, sub_name, tel_user, email_user, password_user) VALUES(?, ?, ?, ?, ?)', [name_user, sub_user, tel_user, email_user, password_user])
        cursor.close()
        self.db.commit()

    def get_correct_user(self, name_user, email_user, password_user):
        cursor = self.db.cursor()
        query = "SELECT * FROM Users  WHERE name_user = ? AND email_user = ? AND password_user = ?"
        cursor.execute(query, [name_user, email_user, password_user])
        result = cursor.fetchone()
        cursor.close()
        if len(result) > 1:
            return result
    def get_uncorrect_user(self, name_user, email_user, password_user):
        cursor = self.db.cursor()
        query = "SELECT * FROM Users  WHERE name_user = ? AND email_user = ? AND password_user = ?"
        cursor.execute(query, [name_user, email_user, password_user])
        result = cursor.fetchone()
        cursor.close()
        if len(result) == None:
            return result

    def get_user_dani(self, name_user, email_user, password_user):
        cursor = self.db.cursor()
        query = "SELECT * FROM Users WHERE name_user = ? AND email_user = ? AND password_user = ?"
        cursor.execute(query, [name_user, email_user, password_user])
        result5 = cursor.fetchone()
        cursor.close()
        return result5

    def get_user_columns(self):
        return ['id_user', 'name_user', 'sub_name', 'tel_user', 'email_user', 'password_user']



