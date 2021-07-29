from mycroft import MycroftSkill, intent_file_handler


class AppointmentCreator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('creator.appointment.intent')
    def handle_creator_appointment(self, message):
        day = message.data.get('day')
        name = message.data.get('name')
        time = message.data.get('time')

        self.speak_dialog('creator.appointment', data={
            'time': time,
            'name': name,
            'day': day
        })


def create_skill():
    return AppointmentCreator()

