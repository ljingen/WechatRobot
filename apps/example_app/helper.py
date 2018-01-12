# -*- coding: utf-8 -*-

from chatterbot import ChatBot

# momo_chat = ChatBot(
#     'momo',
#     # 指定存储方式
#     # 指定logic adpater 我们这里指定三个
#     logic_adapters=[
#         "chatterbot.logic.BestMatch",
#         "chatterbot.logic.MathematicalEvaluation",  # 数学模块
#         "chatterbot.logic.TimeLogicAdapter",  # 时间模块
#     ],
#     input_adapter="chatterbot.input.VariableInputTypeAdapter",
#     output_adapter="chatterbot.output.OutputAdapter",
#     database="chatterbot",
#     read_only=True
# )
momo_chat = ChatBot('mmo', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
momo_chat.train("chatterbot.corpus.chinese")


def get_momo_answer(content):
    #  获取机器人返回结果函数
    response = momo_chat.get_response(content)
    if isinstance(response, str):
        return response
    return response.text