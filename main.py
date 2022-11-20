from pkg.sub_pkg1.mod1 import API_to_CSV
from pkg.sub_pkg2.mod2 import API_to_JSON
from pkg.sub_pkg3.mod3 import API_to_TXT
import requests
import os


class search_all_about_music:
    type_search = ""
    limit_information = ""
    url_for_search = ""
    __file_type = ""
    input_type_file = ""

    def __init__(self, type_search, url_for_search, limit_information):
        self.type_search = type_search
        self.url_for_search = url_for_search
        self.limit_information = limit_information

    def __new_search(self):
        querystring = {"q": "<REQUIRED>", "type": self.type_search, "offset": "0", "limit": self.limit_information, "numberOfTopResults": "5"}
        headers = {
            "X-RapidAPI-Key": "c7ed42f270msh2b98682b4faeb13p1e14bejsn8c390fda51d3",
            "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
        }
        req = requests.get(self.url_for_search, headers=headers, params=querystring)
        output = req.json()
        return output

    def file_output(self):
        self.__file_type = self.input_type_file
        if self.__file_type == "TXT":
            API_to_TXT(self.__new_search())
        elif self.__file_type == "JSON":
            API_to_JSON(self.__new_search())
        elif self.__file_type == "CSV":
            API_to_CSV(self.__new_search())

class spotify(search_all_about_music):
    def file_save_in_directory(self):
        try:
            os.mkdir('file_directory')
            os.chdir(r"file_directory")
            self.file_output()
            os.chdir(r'../')
        except:
            os.chdir(r"file_directory")
            self.file_output()
            os.chdir(r'../')

first_search = search_all_about_music(input("Введіть інформацію що Ви шукаєте для першого екземпляру: "), "https://spotify23.p.rapidapi.com/search/", "10")
first_search.input_type_file = input("Введіть тип файлу для виводу інформації: ")
first_search.file_output()
print("\n")

second_search = search_all_about_music(input("Введіть інформацію що Ви шукаєте для другого єкземпляру: "), "https://spotify23.p.rapidapi.com/search/", "20")
second_search.input_type_file = input("Введіть тип файлу для виводу інформації: ")
second_search.file_output()
print("\n")

third_search = spotify(input("Введіть інформацію що Ви шукаєте для третього єкземпляру: "), "https://spotify23.p.rapidapi.com/search/", "5")
third_search.input_type_file = input("Введіть тип файлу для виводу інформації: ")
third_search.file_save_in_directory()
print("\n")

fourth_search = spotify(input("Введіть інформацію що Ви шукаєте для третього єкземпляру: "), "https://spotify23.p.rapidapi.com/search/", "5")
fourth_search.input_type_file = input("Введіть тип файлу для виводу інформації: ")
fourth_search.file_output()
