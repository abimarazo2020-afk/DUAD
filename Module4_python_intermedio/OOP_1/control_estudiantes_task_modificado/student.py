class Student:
    def __init__(self, name, section, spanish_note, scient_note, social_note, english_note):
        self.name = name
        self.section = section
        self.spanish_note = spanish_note
        self.scient_note = scient_note
        self.social_note = social_note
        self.english_note = english_note
        
    def to_dict(self):
        return {
            'student_name': self.name,
            'student_section': self.section,
            'spanish_note': self.spanish_note,
            'english_note': self.english_note,
            'scient_note': self.scient_note,
            'social_note': self.social_note
        }