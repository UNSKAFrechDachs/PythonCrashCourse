class AnonymousSurvey:
    """Collect anonymous survey answers."""
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, response):
        """Store a response to the survey."""
        self.responses.append(response)

    def show_results(self):
        """Show all the results of the survey."""
        print("Survey results:")
        for response in self.responses:
            print(f"\t- {response}")
