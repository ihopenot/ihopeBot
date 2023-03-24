from .tts import BaseTTS
import azure.cognitiveservices.speech as speechsdk

def build_ssml(text, pitch=100, rate=100, volume=100):
    pitch = pitch - 100
    rate = rate - 100
    volume = volume - 100
    ssml = f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" xml:lang="zh-CN"><voice name="zh-CN-XiaochenNeural"><prosody rate="+{rate}.00%" volume="+{volume}.00%" pitch="+{pitch}.00%">{text}</prosody></voice></speak>'
    return ssml

class AzureTTS(BaseTTS):
    def __init__(self, config):
        self.config = config
        speech_config = speechsdk.SpeechConfig(subscription=self.config["subscription"], region=self.config["region"])
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    def speak(self, text):
        ssml = build_ssml(text, pitch=120, rate=110, volume=110)
        result = self.speech_synthesizer.speak_ssml_async(ssml).get()

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

