import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://@LAPTOP-54M8BGDQ\\AMJ/land_db?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
