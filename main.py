from datetime import date
from re import S
from xml.dom import NoModificationAllowedErr
import inquirer
import csv

res  = True


while res == True:

    first_name =  input("Entrer le nom :").upper()
    last_name = input("Entrer le nom :").upper()
    poste = input("Entrer à quel poste vous avez embouché:").upper()
    year = ""
    month = ""
    day = ""
    
    while  len(year) < 4:
        print("Veuillez entrer l'année en 4 chiffres")
        year = input("Entrer l'année d'entrer à l'entreprise : ")
        print(year)
    year =int(year)

    month = 0
    while  month > 12 or month < 1:
        print("Veuillez entrer un nombre pour le mois")
        month = int(input("Entrer le mois d'entrer à l'entreprise : "))
    day = 0
    ''' demande le jour d'integration dans l'entreprise '''
    while  day > 31 or day < 1:
        print("Veuillez entrer un nombre pour le jour")
        day = int(input("Entrer le jour d'entrer à l'entreprise : "))
    print(day)
    
    d = date(year, month, day)
    print(last_name,first_name,poste,d)
    questions = [
        inquirer.Confirm("confirm", message="Voulez vous entrer une employé?",
                         default=True),
    ]
    
    answers = inquirer.prompt(questions)
    if answers["confirm"] == False:
        res = False

    field_names = ['first_name', 'last_name', 'date', 'poste']

    to_csv_save = {
        "first_name": first_name,
        "last_name": last_name,
        "date": d,
        "poste": poste
        }

    with open('tableur.csv', 'a') as f_object:
                # Pass the file object and a list
                # of column names to DictWriter()
                # You will get a object of DictWriter
                dictwriter_object = csv.DictWriter(f_object, fieldnames=field_names)
                # Pass the dictionary as an argument to the Writerow()
                dictwriter_object.writerow(to_csv_save)
                # Close the file object
                f_object.close()
