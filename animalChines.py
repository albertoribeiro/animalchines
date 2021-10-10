from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        print("> LaunchRequestHandler-can_handle")
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        print("> LaunchRequestHandler-handle")
        handler_input.response_builder.speak("Bem vindo à skill do animal chinês").set_should_end_session(False)
        return handler_input.response_builder.response

class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        print("> CatchAllExceptionHandler-can_handle")
        return True

    def handle(self, handler_input, exception):
        print("> CatchAllExceptionHandler-handle")
        handler_input.response_builder.speak("Desculpe, ocorreu um problema. Por favor tente outra vez!! ").set_should_end_session(False)
        return handler_input.response_builder.response 

class AnimalChinesIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        print("> AnimalChinesIntentHandler-can_handle")
        return is_intent_name("AnimalChinesIntent")(handler_input)

    def handle(self, handler_input, exception):
        print("> AnimalChinesIntentHandler-handle")
        print(exception)
        ano = handler_input.request_envelope.request.intent.slots['ano'].value
        speech_text = "o ano que vc disse foi "
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response 

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())
sb.add_request_handler(AnimalChinesIntentHandler())

def handler(event, context):
    print("> handler")
    return sb.lambda_handler()(event, context)