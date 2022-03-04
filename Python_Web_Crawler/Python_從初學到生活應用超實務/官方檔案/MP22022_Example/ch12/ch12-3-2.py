from chatterbot import ChatBot

chatbot = ChatBot(
  'TestBot_cht',
  logic_adapters=[
    {
      "import_path": "chatterbot.logic.BestMatch",
      "default_response": "對不起! 我不了解你的問題?"
    }
  ]
)
q = "你好!"
response = chatbot.get_response(q)
print("問題: ", q)
print("回答: ", response)
q = "謝謝!"
response = chatbot.get_response(q)
print("問題: ", q)
print("回答: ", response)
q = "天氣好嗎!"
response = chatbot.get_response(q)
print("問題: ", q)
print("回答: ", response)