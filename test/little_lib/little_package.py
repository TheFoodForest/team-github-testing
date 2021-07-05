from typing import Type


class little_class():
    def __init__(self, name:str): 
        self.name = self._check_name(name)
    #check name for string not new lines
    def _check_name(self, name:str) -> str:
        # make sure name is string
        if not isinstance(name, str):
            raise TypeError("The name argument must be a string, provided type: {}".format(type(name)))
        # make sure name doesn't contain new lines 
        if "\n" in name:
            name = name.replace("\n", " ")
        return name

    def identify(self):
        return print('My name is {}'.format(self.name))

    def newthing(self):
        # add something here
        pass




if __name__ == "__main__":
    a = little_class("graham\npenrose")
    a.identify()