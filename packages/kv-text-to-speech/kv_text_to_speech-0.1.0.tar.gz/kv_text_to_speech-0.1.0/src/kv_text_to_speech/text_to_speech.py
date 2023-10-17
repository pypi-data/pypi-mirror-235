import os
import azure.cognitiveservices.speech as speechsdk


class SpeechService:
    """
    Azure Cognitive Speech Service Class - Azure TTS Implementation
    """

    def __init__(self):
        """
        Constructor function for hte speech service class.
        :param: None
        :return: None
        """

        self.speech_key = None
        self.region = None
        self.speech_config = None
        self.audio_config = None
        self.speaker = 'en-US-JennyNeural'  # Default voice is Jenny

    def set_azure_speech_config(self):
        """
        This function sets the speech and audio configurations for use with Azure's TTS service.
        :return: None
        """
        # TODO: get Keys from either a config file or environment variable in production.

        self.speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.region)
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    def set_speaker(self, speaker: str = None):
        """
        This function allows us to change the speaker for the TTS service.
        :param speaker: Azure Speaker Name (i.e. 'en-US-DavisNeural')
        :return: None
        """

        if speaker:
            self.speaker = speaker
            self.speech_config.speech_synthesis_voice_name = speaker  # only overwrite if speaker provided
        else:
            raise UserWarning('Speaker not provided. Please provide a valid speaker.')

    def configure_audio_output(self, file_name: str, audio_format=None):
        """
        This function configures the audio output for the TTS service, including format and filename. Other
        parameters may be added to improve audio quality in the future.

        :param file_name: The name of the audio file
        :param audio_format: The audio format to be used for the recording.
        :return: None
        """
        # TODO: Add blob storage parameters to store the audio file.
        # https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.speechsynthesisoutputformat?view=azure-python
        audio_format = speechsdk.SpeechSynthesisOutputFormat.Audio24Khz96KBitRateMonoMp3
        self.speech_config.set_speech_synthesis_output_format(audio_format)
        self.audio_config = speechsdk.audio.AudioOutputConfig(filename=file_name)

    def read_article(self, article: str):
        """
        This function performs the text to speech generation by calling hte speech synthesizer on
        Azure.
        :param article: The article text to be read.
        :return: Returns the status of the speech synthesis
        """

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config,
                                                         audio_config=self.audio_config)

        # TODO: Add response handling for errors.
        result = speech_synthesizer.speak_text_async(article).get()
        return result
