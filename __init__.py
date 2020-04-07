from mycroft import MycroftSkill, intent_file_handler


class SetName(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('name.set.intent')
    def handle_name_set(self, message):
        self.speak_dialog('name.set')


def create_skill():
    return SetName()

