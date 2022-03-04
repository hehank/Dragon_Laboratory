from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("ListTrainer")
conversation = [
    "fchart",
    "https://fchart.github.io/",
    "流程圖是什麼",
    "流程圖是一種描述演算法的工具",
    "fChart是什麼?", 
    "fChart是一套程式設計教學工具"
]
trainer = ListTrainer(chatbot)
trainer.train(conversation)
q = "fchart"
response = chatbot.get_response(q)
print("回答: ", response)
q = "fChart是什麼?"
response = chatbot.get_response(q)
print("回答: ", response)
q = "流程圖是什麼"
response = chatbot.get_response(q)
print("回答: ", response)