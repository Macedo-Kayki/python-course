import json
from pathlib import Path
from typing import List, Dict
from student import Student

class Manage():
    def __init__(self, name, grade):
        super().__init__(name, grade)

    def create_student(self, way):
        data = {
            "name": self.name,
            "grade": self.grade
        }

        try:
            with open(way, 'a', encoding='utf-8') as archive:
                json.dump(data, archive, indent=4, ensure_ascii=False)
            print("\nThe student was raised correctly")
        except (PermissionError) as e:
            print(f"\nYou don't have permission for this., {e}")
        except (ValueError, IndexError) as e:
            print(f"\nAn error occurred in the value., {e}")
    
    def read_students(self, way):
        try:
            with open(way, 'r', encoding='utf=8') as archive:
                data = json.load(archive)
                print(data)
            print("\nThe archive was read with success")
        except Exception as e:
            print(f"\nAn unexpected error occurred. {e}")

    def update_student(self, way):
        try:
            with open(way, 'r', encoding='utf-8') as archive:
                data = json.load(archive)

            option = input("\nWhich student's grade do you want to change?")
            if data['name'] == option:
                new_grade = float(input(f"Type the new grade for {option}"))
                
                print("\nBefore modifying:", data)

                data['grade'] = float(new_grade)

                with open(data, 'w', encoding='utf-8') as archive:
                    json.dump(data, archive, indent=4, ensure_ascii=False)

                modified_json = json.dumps(data)
                
                print("\nAfter modifying:", modified_json)
        except (ValueError, IndexError) as e:
            print(f"\nAn error occurred in the value., {e}")
    
    def delete_student(self, way):
        try:
            with open(way, 'r', encoding='utf-8') as archive:
                data = json.load(archive)
            name_formated = self.name.strip().title()
        except (ValueError, IndexError) as e:
            print(f"\nAn error occurred in the value., {e}")     