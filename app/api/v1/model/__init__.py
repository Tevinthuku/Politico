OFFICES = []

# def __init__(self, id, type, name):
#     self.id = id
#     self.type = type
#     self.name = name

# def save_office(self):
#     OFFICES.append(self)


class OfficesModel:

    @staticmethod
    def get_all_offices():
        return [vars(office) for office in OFFICES]
