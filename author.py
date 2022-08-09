

class AuthorSQL:
    def __init__(self, cursor_param):
        self.cursor = cursor_param

    def create_table_author(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS author (
        id int not null primary key auto_increment,
        name varchar(100) not null,
        surname varchar(100) not null,
        bio varchar(255) not null
        );
        """
        self.cursor.execute(query)

    def add_new_author(self, name, surname, bio):
        query = f"""
        INSERT INTO author( name, surname, bio)
        VALUES ('{name}', '{surname}', '{bio}');
        """
        self.cursor.execute(query)

    def get_all_author(self):
        query = f"""
        SELECT * FROM author;
        """
        self.cursor.execute(query)
        print(self.cursor.fetchall())

    def delete_user_by_id(self, id):
        query = f"""
        Delete from user where id={id};
        """
        self.cursor.execute(query)
        print(f"User with id:{id} deleted!")

    # изменение данных пользователя
    def update_author_name(self, id, new_value):
        query = f"""
        UPDATE user SET name='{new_value}' where id={id};
        """
        self.cursor.execute(query)
        print(f"author by id: {id} updated!")

    def update_author_surname(self, id, new_value):
        query = f"""
        update user set email='{new_value}' where id={id};
        """
        self.cursor.execute(query)
        print(f"User by id: {id} updated!")

    def update_author_bi(self, id, new_value):
        query = f"""
        update user set password='{new_value}' where id={id};
        """
        self.cursor.execute(query)
        print(f"user id {id} password updated!")



