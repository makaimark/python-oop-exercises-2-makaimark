class Mentor():
    def __init__(self, raw_data):
        self.id = raw_data[0]
        self.first_name = raw_data[1]
        self.last_name = raw_data[2]
        self.nick_name = raw_data[3]
        self.phone_number = raw_data[4]
        self.email = raw_data[5]
        self.city = raw_data[6]
        self.favourite_number = raw_data[7]

    @staticmethod
    def get_all():
        from db import Database
        return Database.get_mentors()

    # Return the 2 name property of all the mentors
    # returns: list of dictionaries
    # example: [{
    #    first_name: 'Bill',
    #    last_name: 'Wilkinson'
    # }, ...]
    @classmethod
    def _1_list_mentors(cls):
        from db import Database
        mentors = Database.get_mentors()
        return_list = []
        temp_dict = {}
        for i in mentors:
            temp_dict["first_name"] = i.first_name
            temp_dict["last_name"] = i.last_name
            return_list.append(temp_dict)
            temp_dict = {}
        return return_list

    # Return the nick_name property of all the mentors located in Miskolc
    # returns: list of dictionaries
    # example: [{
    #    nick_name: 'Billy'
    # }, ...]
    @classmethod
    def _2_list_mentors_from_miskolc(cls):
        from db import Database
        mentors = Database.get_mentors()
        return_list = []
        temp_dict = {}
        city = "Miskolc"
        for i in mentors:
            if i.city == city:
                temp_dict["nick_name"] = i.nick_name
                return_list.append(temp_dict)
                temp_dict = {}
        return return_list

    # Return the highest favourite number of all mentors
    # returns: integer
    # example: 927
    @classmethod
    def _3_greatest_favourite_number(cls):
        from db import Database
        mentors = Database.get_mentors()
        return_number = 0
        for i in mentors:
            if i.favourite_number is not None:
                if int(i.favourite_number) > return_number:
                    return_number = int(i.favourite_number)
        return return_number
