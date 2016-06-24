class Database():
    mentors_data = [
        [1, 'Attila', 'Molnár', 'Atesz', '003670/630-0539', 'attila.molnar@codecool.com', 'Miskolc', 23],
        [2, 'Pál', 'Monoczki', 'Pali', '003630/327-2663', 'pal.monoczki@codecool.com', 'Miskolc', None],
        [3, 'Sándor', 'Szodoray', 'Szodi', '003620/519-9152', 'sandor.szodoray@codecool.com', 'Miskolc', 7],
        [4, 'Dániel', 'Salamon', 'Dani', '003620/508-0706', 'daniel.salamon@codecool.com', 'Budapest', 4],
        [5, 'Miklós', 'Beöthy', 'Miki', '003630/256-8118', 'miklos.beothy@codecool.com', 'Budapest', 42],
        [6, 'Tamás', 'Tompa', 'Tomi', '003630/370-0748', 'tamas.tompa@codecool.com', 'Budapest', 42],
        [7, 'Mateusz', 'Ostafil', 'Mateusz', '003648/518-664-923', 'mateusz.ostafil@codecool.com', 'Krakow', 13]
    ]

    applicants_data = [
        [1, 'Dominique', 'Williams', '003630/734-4926', 'dolor@laoreet.co.uk', 61823],
        [2, 'Jemima', 'Foreman', '003620/834-6898', 'magna@etultrices.net', 58324],
        [3, 'Zeph', 'Massey', '003630/216-5351', 'a.feugiat.tellus@montesnasceturridiculus.co.uk', 61349],
        [4, 'Joseph', 'Crawford', '003670/923-2669', 'lacinia.mattis@arcu.co.uk', 12916],
        [5, 'Ifeoma', 'Bird', '003630/465-8994', 'diam.duis.mi@orcitinciduntadipiscing.com', 65603],
        [6, 'Arsenio', 'Matthews', '003620/804-1652', 'semper.pretium.neque@mauriseu.net', 39220],
        [7, 'Jemima', 'Cantu', '003620/423-4261', 'et.risus.quisque@mollis.co.uk', 10384],
        [8, 'Carol', 'Arnold', '003630/179-1827', 'dapibus.rutrum@litoratorquent.com', 70730],
        [9, 'Jane', 'Forbes', '003670/653-5392', 'janiebaby@adipiscingenimmi.edu', 56882],
        [10, 'Ursa', 'William', '003620/496-7064', 'malesuada@mauriseu.net', 91220]
    ]

    @classmethod
    def get_mentors(cls):
        from mentor import Mentor
        return [Mentor(raw_mentor) for raw_mentor in cls.mentors_data]

    @classmethod
    def get_applicants(cls):
        from applicant import Applicant
        return [Applicant(raw_applicant) for raw_applicant in cls.applicants_data]
