from mycroft import MycroftSkill, intent_file_handler
#from set_name.py import set_name(name)

class SetName(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('name.set.intent')
    def handle_name_set(self, message):
        self.speak_dialog('name.set')
        subprocess.Popen("python3", "set_name.py", "Bryan")
        #set_name.set_name("Bryan")


def create_skill():
    return SetName()

