from .sr import BaseSr
import azure.cognitiveservices.speech as speechsdk

class AzureSr(BaseSr):
    def __init__(self, config):
        self.config = config
        speech_config = speechsdk.SpeechConfig(subscription=self.config["subscription"], region=self.config["region"])
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="zh-CN")

    def listen(self):
        result = self.speech_recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text 
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
        return None
