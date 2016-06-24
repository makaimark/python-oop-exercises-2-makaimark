from db import Database
from mentor import Mentor
from applicant import Applicant


def main():
    print('\n_1_list_mentors: \n', Mentor._1_list_mentors())
    print('\n_2_list_mentors_from_miskolc: \n', Mentor._2_list_mentors_from_miskolc())
    print('\n_3_greatest_favourite_number: \n', Mentor._3_greatest_favourite_number())
    print('\n_4_specific_applicant_by_first_name: \n', Applicant._4_specific_applicant_by_first_name())
    print('\n_5_specific_applicant_by_email_domain: \n', Applicant._5_specific_applicant_by_email_domain())
    print('\n_6_inserting_a_new_applicant: \n', Applicant._6_inserting_a_new_applicant())
    print('\n_7_updating_data: \n', Applicant._7_updating_data())
    print('\n_8_deleting_applicants: \n', Applicant._8_deleting_applicants())


if __name__ == '__main__':
    main()
