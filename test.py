import unittest
from db import Database
from mentor import Mentor
from applicant import Applicant


mentors = Database.get_mentors()
applicants = Database.get_applicants()


class application_process_test_case(unittest.TestCase):
    def test_1_list_mentors_list_type_returned(self):
        result = Mentor._1_list_mentors()
        self.assertEqual(type(result).__name__, "list")

    def test_1_list_mentors_length(self):
        result = Mentor._1_list_mentors()
        self.assertEqual(len(result), 7)

    def test_1_list_mentors_has_dictionaries(self):
        result = Mentor._1_list_mentors()
        for mentor in result:
            self.assertEqual(type(mentor).__name__, "dict")

    def test_1_list_mentors_values(self):
        result = Mentor._1_list_mentors()
        self.assertEqual(result[0], {'first_name': 'Attila', 'last_name': 'Molnár'})
        self.assertEqual(result[4], {'first_name': 'Miklós', 'last_name': 'Beöthy'})
        self.assertEqual(result[6], {'first_name': 'Mateusz', 'last_name': 'Ostafil'})

    def test_2_list_mentors_from_miskolc_list_type_returned(self):
        result = Mentor._2_list_mentors_from_miskolc()
        self.assertEqual(type(result).__name__, "list")

    def test_2_list_mentors_from_miskolc_length(self):
        result = Mentor._2_list_mentors_from_miskolc()
        self.assertEqual(len(result), 3)

    def test_2_list_mentors_from_miskolc_has_dictionaries(self):
        result = Mentor._2_list_mentors_from_miskolc()
        for mentor in result:
            self.assertEqual(type(mentor).__name__, "dict")

    def test_2_list_mentors_from_miskolc_values(self):
        result = Mentor._2_list_mentors_from_miskolc()
        self.assertEqual(result[0], {'nick_name': 'Atesz'})
        self.assertEqual(result[1], {'nick_name': 'Pali'})
        self.assertEqual(result[2], {'nick_name': 'Szodi'})

    def test_3_greatest_favourite_number_integer_type_returned(self):
        result = Mentor._3_greatest_favourite_number()
        self.assertEqual(type(result).__name__, "int")

    def test_3_greatest_favourite_number_value(self):
        result = Mentor._3_greatest_favourite_number()
        self.assertEqual(result, 42)

    def test_3_greatest_favourite_number_different_value(self):
        original_favourite_number_of_first_mentor = Database.mentors_data[0][-1]
        Database.mentors_data[0][-1] = 927
        result = Mentor._3_greatest_favourite_number()
        self.assertEqual(result, 927)
        Database.mentors_data[0][-1] = original_favourite_number_of_first_mentor

    def test_4_specific_applicant_by_first_name_list_type_returned(self):
        result = Applicant._4_specific_applicant_by_first_name()
        self.assertEqual(type(result).__name__, "list")

    def test_4_specific_applicant_by_first_name_length(self):
        result = Applicant._4_specific_applicant_by_first_name()
        self.assertEqual(len(result), 1)

    def test_4_specific_applicant_by_first_name_has_dictionaries(self):
        result = Applicant._4_specific_applicant_by_first_name()
        for applicant in result:
            self.assertEqual(type(applicant).__name__, "dict")

    def test_4_specific_applicant_by_first_name_values(self):
        result = Applicant._4_specific_applicant_by_first_name()
        self.assertEqual(result[0], {'full_name': 'Carol Arnold'})

    def test_5_specific_applicant_by_email_domain_list_type_returned(self):
        result = Applicant._5_specific_applicant_by_email_domain()
        self.assertEqual(type(result).__name__, "list")

    def test_5_specific_applicant_by_email_domain_length(self):
        result = Applicant._5_specific_applicant_by_email_domain()
        self.assertEqual(len(result), 1)

    def test_5_specific_applicant_by_email_domain_has_dictionaries(self):
        result = Applicant._5_specific_applicant_by_email_domain()
        for applicant in result:
            self.assertEqual(type(applicant).__name__, "dict")

    def test_5_specific_applicant_by_email_domain_values(self):
        result = Applicant._5_specific_applicant_by_email_domain()
        self.assertEqual(result[0], {'full_name': 'Jane Forbes'})

    def test_6_inserting_a_new_applicant(self):
        result = Applicant._6_inserting_a_new_applicant()
        self.assertEqual(type(result).__name__, "list")
        self.assertEqual(len(result), 1)
        for applicant in result:
            self.assertEqual(type(applicant).__name__, "dict")
        self.assertEqual(result[0], {
            'id': 11,
            'first_name': 'Markus',
            'last_name': 'Schaffarzyk',
            'phone_number': '003620/725-2666',
            'email': 'djnovus@groovecoverage.com',
            'application_code': 54823
        })

    def test_7_updating_data(self):
        result = Applicant._7_updating_data()
        self.assertEqual(type(result).__name__, "list")
        self.assertEqual(len(result), 1)
        for applicant in result:
            self.assertEqual(type(applicant).__name__, "dict")
        self.assertEqual(result[0], {
            'phone_number': '003670/223-7459'
        })

    def test_8_deleting_applicants(self):
        result = Applicant._8_deleting_applicants()
        self.assertEqual(type(result).__name__, "int")
        self.assertEqual(result, 0)


def test_main():
    unittest.main()


if __name__ == '__main__':
    test_main()
