# -*- coding: utf-8 -*-
from openai import OpenAI
# 设置 API key 和 API base URL
api_key = "sk-0f120pZgs2uf84vPE0A81a35D75f43FbA34aF89d27Fe8dA5"
base_url = ("https://api.132006.xyz/v1")
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "你将扮演一位求职者的角色，根据上传的pdf简历以及应聘工作的描述，来直接给HR写一个礼貌专业的求职新消息，要求能够用专业的语言结合简历中的经历和技能，并结合应聘工作的描述，来阐述自己的优势，尽最大可能打动招聘者。并且请您始终使用中文来进行消息的编写,开头是招聘负责人，结尾是真诚的，付尧全。这是一封完整的求职信，不要包含求职信内容以外的东西，例如“根据您上传的求职要求和个人简历，我来帮您起草一封求职邮件：”这一类的内容，以便于我直接自动化复制粘贴发送",
        }
    ],
    model="gpt-3.5-turbo",
)
message = chat_completion.choices[0].message.content
print(message)