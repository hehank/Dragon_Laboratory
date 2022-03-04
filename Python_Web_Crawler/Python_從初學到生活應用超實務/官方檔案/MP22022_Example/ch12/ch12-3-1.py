from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Trainer_cht")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.tchinese")
