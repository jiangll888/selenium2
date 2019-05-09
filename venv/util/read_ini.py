import configparser

class ReadIni:
    def __init__(self,filename=None):
        if filename == None:
            self.filename = "../config/elements.ini"
        else:
            self.filename = filename
        self.config = self.read_data()

    def read_data(self):
        config = configparser.ConfigParser()
        config.read(self.filename,encoding="utf-8")
        return config

    def get_value(self,key,section=None):
        if section == None:
            section = "register_element"
        try:
            element_key = self.config.get(section,key)
        except:
            print("没有这个元素")
            element_key = None
        return element_key

    def write_data(self,key,value,section=None):
        if section == None:
            section = "register_element"
            self.config.set(section,key,value)
        else:
            if section in self.config.sections():
                self.config.set(section,key,value)
            else:
                self.config.add_section(section)
                self.config.set(section,key,value)
        with open(self.filename,"w") as fp:
            self.config.write(fp)

if __name__ == "__main__":
    r = ReadIni()
    r.write_data("username1","test111","register_element1")