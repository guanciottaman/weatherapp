from dotenv import get_key

import requests
from tkinter import messagebox
from customtkinter import *

from languages import *


class App(CTk):

    def __init__(self):
        super().__init__()
        self.title('Weather')
        self.geometry('420x320')
        set_appearance_mode('dark')
        set_default_color_theme('dark-blue')
        self.grid_propagate(False)

        self.lang_code = 'en'
        self.city_frames = []

        self.title = CTkLabel(self, text=English.title, font=('Segoe UI', 24, 'bold'))
        self.title.grid(row=0, column=0, padx=20, pady=20)
        self.searchentry = CTkEntry(self, width=150, height=30, placeholder_text='Search for a city...',
                                    font=('Segoe UI', 16, 'bold'))
        self.searchentry.grid(row=1, column=0, padx=20, pady=20)
        self.search = CTkButton(self, text='Search', font=('Segoe UI', 16), command=self.search_city)
        self.search.grid(row=1, column=1)
        self.setlang = CTkOptionMenu(self, width=150, height=30,
                                     values=['English', 'Italian', 'German', 'French', 'Spanish'],
                                     font=('Segoe UI', 16), dropdown_font=('Segoe UI', 16),
                                     command=self.change_lang)
        self.setlang.grid(row=0, column=1, padx=20, pady=20)

    def search_city(self):
        try:
            for frame in self.city_frames:
                frame.destroy()
            self.grid_propagate(False)
            city = self.searchentry.get().lower()
            api_key = get_key('.env', 'API_KEY')
            request = requests.get('http://api.weatherapi.com/v1/current.json',
                                   params={'key': api_key, 'q': city, 'lang': self.lang_code})
            json = request.json()
            current_temp = json['current']['temp_c']
            condition_text = json['current']['condition']['text']
            new_frame = CTkFrame(self, width=500, height=300)
            new_frame.grid(row=2, column=0, padx=20, pady=10)
            new_frame.grid_propagate(False)
            cityw = CTkLabel(new_frame, font=('Segoe UI', 16, 'bold'),
                             text=f'{json["location"]["name"]}, {json["location"]["region"] if json["location"]["region"] != json["location"]["name"] and json["location"]["region"] else ""}, {json["location"]["country"]}\n {json["location"]["localtime"]}')
            cityw.grid(row=0, column=0, padx=20, pady=10)
            condition_t = CTkLabel(new_frame, font=('Segoe UI', 16, 'bold'), text=condition_text)
            condition_t.grid(row=1, column=0, padx=20, pady=10)
            curr_temp = CTkLabel(new_frame, font=('Segoe UI', 16, 'bold'), text=f'{current_temp}° C')
            curr_temp.grid(row=2, column=0, padx=20, pady=10)
            self.geometry('440x340')
            new_frame.grid_propagate(True)
            self.grid_propagate(True)
            print(json)
            self.city_frames.append(new_frame)
        except KeyError:
            messagebox.showerror('Error', 'City not found. \nTry again')

    def change_lang(self, choice):
        if choice == 'English':
            self.lang_code = English.lang_code
            self.title.configure(text=English.title)
            self.search.configure(text=English.search)
            self.searchentry.configure(placeholder_text=English.search_entry)
        if choice == 'Italian':
            self.geometry('410x320')
            self.lang_code = Italian.lang_code
            self.title.configure(text=Italian.title)
            self.search.configure(text=Italian.search)
            self.searchentry.configure(placeholder_text=Italian.search_entry)
        if choice == 'French':
            self.geometry('410x320')
            self.lang_code = French.lang_code
            self.title.configure(text=French.title)
            self.search.configure(text=French.search)
            self.searchentry.configure(placeholder_text=French.search_entry)
        if choice == 'German':
            self.geometry('450x320')
            self.lang_code = German.lang_code
            self.title.configure(text=German.title)
            self.search.configure(text=German.search)
            self.searchentry.configure(placeholder_text=German.search_entry)
        if choice == 'Spanish':
            self.geometry('490x320')
            self.lang_code = Spanish.lang_code
            self.title.configure(text=Spanish.title)
            self.search.configure(text=Spanish.search)
            self.searchentry.configure(placeholder_text=Spanish.search_entry)


if __name__ == '__main__':
    app = App()
    app.mainloop()
