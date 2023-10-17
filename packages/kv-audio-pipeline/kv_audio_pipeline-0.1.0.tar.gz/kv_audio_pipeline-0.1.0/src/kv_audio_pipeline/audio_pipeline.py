from kv_text_processing.img_to_text import extract_text_from_article, write_text_to_file, clean_extracted_text
from kv_text_to_speech.text_to_speech import SpeechService

class AudioPipeline:

    def __init__(self,
                 img_dir: str = "",
                 article_title: str = "",
                 ):
        self.image_directory = img_dir
        self.article_title = article_title
        self.text = ""
        self.speech = None

    def perform_ocr_and_save_file(self) -> None:
        """
        Runs the extract_text_from_artcile function on the AudioPipeline's provided parameters.

        :return: None
        """
        self.text = extract_text_from_article(img_dir=self.image_directory,
                                              article_title=self.article_title,
                                              save_file=True)

        if self.text == "":
            raise UserWarning('No article was found and a blank string was returned. '
                              'Please check the image directory path and verify image(s) are present.')
        else:
            # Clean up the spacing on the text file for smoother tts recording
            self.text = clean_extracted_text(self.text)
            # Save to a text file for storage/history
            write_text_to_file(text=self.text, file_name=f'{self.article_title}.txt')

    def initialize_speech_service(self, key, region) -> None:
        """
        This function initializes an Azure Speech Service instance using the provided Key and Region
        :param key: Speech Services API Key
        :param region: Speech Services API Region (Server/Resource Region)
        :return: None
        """

        self.speech = SpeechService()

        # TODO: Get Secret Variables from ENV or Config
        self.speech.speech_key = key
        self.speech.region = region

        self.speech.set_azure_speech_config()

    def change_speaker(self, speaker: str = "en-US-JennyNeural") -> None:
        """
        This function changes the speaker to the supplied Speaker string. Strings can be found under Azure's Speech
        Services API/Documentation.

        :param speaker: Name of the speaker to be used
        :return:
        """
        self.speech.set_speaker(speaker=speaker)

    def configure_audio_output(self, file_name: str) -> None:
        """
        Adds the file name to the Azure Speech Services Audio output.
        :param file_name: The name to be used for the audio file
        :return: None
        """
        self.speech.configure_audio_output(file_name=file_name)

    def generate_audio(self) -> None:
        """
        This runs the read_article function using the AudioPipelines text
        :return: None
        """
        self.speech.read_article(article=self.text)

    def run_pipeline(self, key: str = "", region: str = "") -> None:
        """
        This function runs the full OCR and TTS pipeline in a single call.
        :return: None
        """

        #TODO: Replace key and region inputs with ENV variables
        self.perform_ocr_and_save_file()
        self.initialize_speech_service(key=key, region=region)
        self.configure_audio_output(file_name=f'{self.article_title}.mp3')
        self.change_speaker('en-US-DavisNeural')
        self.generate_audio()
