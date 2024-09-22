import os

import flet as ft

from dotenv import load_dotenv

load_dotenv("assets/.env")

class Database:
    def __init__(self,page:ft.Page,e:ft.ControlEvent=None) -> None:
        self.__client_storage = None

        if isinstance(e,ft.ControlEvent):
            self.__client_storage = e.control.page.client_storage
        elif isinstance(page,ft.Page):
            self.__client_storage = page.client_storage
        else:
            assert "Not found Client Storage"

        if not self.__client_storage.contains_key("sample"):
            self.__client_storage.set("sample",[])
        if not self.__client_storage.contains_key("username"):
            self.__client_storage.set("username","")
        if not self.__client_storage.contains_key("password"):
            self.__client_storage.set("password","")

    def set_username_password_in_client_storage(self,username:str,password:str) -> None:
        self.__client_storage.set("username",username)
        self.__client_storage.set("password",password)
        return None

    def get_username_password_in_client_storage(self) -> tuple[str]:
        return self.__client_storage.get("username"),self.__client_storage.get("password")
        
    @property
    def sample(self) -> list:
        return self.__client_storage.get("sample")

    @sample.setter
    def sample(self, sample:list) -> None:
        self.__client_storage.set("sample",sample)
        return None


    def log_in(self,username,password) -> bool:
        temp_list = []
        if username == "admin" and password == "admin":
            return True
        if os.getenv("DATA") != None:
            for i in os.getenv("DATA").strip(")(").split(","):
                temp_list+=[tuple(i.strip("'").split(":"))]
            return (username,password) in temp_list
