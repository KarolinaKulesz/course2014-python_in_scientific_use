# -*- coding: utf-8 -*-

import pickle
import pathlib


def load_animals(large_dataset=False):
    """

    :param bool large_dataset: Jeśli wartość to True zwraca 1E6 zwierząt, w
                               przeciwnym razie 1E5. Test będzie odbywał się
                               przy 1E6 zwierząt.

    :return: Lista zwierząt
    """
    file_name = 'animals-small.bin' if not large_dataset else 'animals.bin'
    file = pathlib.Path(__file__).parent / file_name
    with open(str(file), 'rb') as f:
        return pickle.load(f)


def filter_animals(animal_list):
    """
    Jesteś informatykiem w firmie Noe Shipping And Handling. Firma ta zajmuje
    się międzykontynentalnym przewozem zwierząt.

    Dostałeś listę zwierząt które są dostępne w pobliskim zoo do transportu.

    Mususz z tej listy wybrać listę zwierząt które zostaną spakowane na statek,

    Lista ta musi spełniać następujące warunki:

    * Docelowa lista zawiera obiekty reprezentujące zwierzęta (tak jak animal_list)
    * Z każdego gatunku zwierząt (z tej listy) musisz wybrać dokładnie dwa
      egzemplarze.
    * Jeden egzemplarz musi być samicą a drugi samcem.
    * Spośród samic i samców wybierasz te o najmniejszej masie.
    * Dane w liście są posortowane względem gatunku a następnie nazwy zwierzęcia

    Wymaganie dla osób aspirujących na ocenę 5:

    * Ilość pamięci zajmowanej przez program musi być stała względem
      ilości elementów w liście zwierząt.
    * Ilość pamięci może rosnąć liniowo z ilością gatunków.

    Nie podaje schematu obiektów w tej liście, musicie radzić sobie sami
    (można podejrzeć zawartość listy w interaktywnej sesji interpretera).

    Do załadowania danych z listy możesz użyć metody `load_animals`.

    :param animal_list:
    """
    keys=[]
    dict={}
    #dict_item = {' ':[None,None]}
    # dict['genus']=(male,female) - animal['genus'] to klucz słownika dict, a (None,None) to krotka przyjmująca dwa słowniki
    
    for animal in animal_list:
        if animal['genus'] in dict:
            
            if animal['sex']=='male':
                if (dict[animal['genus']][0] is None) or ( mass(animal['mass']) < mass(dict[animal['genus']][0]['mass']) ):
                    dict[animal['genus']][0] = animal
            
            elif animal['sex']=='female':
                if (dict[animal['genus']][1] is None) or ( mass(animal['mass']) < mass(dict[animal['genus']][1]['mass']) ):
                    dict[animal['genus']][1] = animal
        #
        else:
            keys.append(animal['genus'])
            dict[animal['genus']]=[None,None]
            if animal['sex']=='male':
                dict[animal['genus']][0]=animal
            elif animal['sex']=='female':
                dict[animal['genus']][1]=animal
        #
    keys.sort(key=str.lower)
    print(keys)
    for key in keys:
      print(key)
      print(dict[key][0])
      print(dict[key][1])
    return dict

def mass(m):
   """
    zwraca masę w gramch
   """
   mass = m[0]
   if m[0]=="mg":
            mass*=1/1000
   elif m[1]=="kg":
            mass*=1000
   elif m[1]=="Mg":
            mass*=1000000
   return mass

if __name__ == "__main__":
    animals = load_animals(large_dataset=True)
    dict = filter_animals(animals)
    #print(dict)