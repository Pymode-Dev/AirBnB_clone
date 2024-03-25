from models.base_model import BaseModel

class City(BaseModel):
    """ DOC DOC DOC """
    state_id = ""
    name = ""
    another_variable = ""

    # If you still want to keep the __init__ method, you can uncomment it
    # def __init__(self, state_id):
    #     City.state_id = state_id
