from _base_endpoint import ApiEndpoint

class WordsEndpoint(ApiEndpoint):
    location = '/words'
    from flask_restful import reqparse

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('word', type=str, required=True)

    def get(self):
        return {'words': [word.word_value for word in self.models.Word.get_all_words()]}

    def post(self):
        post_arguments = self.post_parser.parse_args()
        word_value = post_arguments['word']
        self.models.Word.add_word(word_value=word_value)
        return {'success': True}
