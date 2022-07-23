import os
from turtle import clear

from click import prompt
import config
import openai

openai.api_key = config.OPENAI_API_KEY

blogIdeas = openai.Completion.create(
    engine = "davinci-instruct-beta-v3",
    prompt = "Blog idea on best ues of AI",
    temperature = 0.7,
    max_tokens = 100,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0,
)

blogContent = openai.Completion.create(
    engine = "davinci-instruct-beta-v3",
    prompt = "write blog on AI",
    temperature = 0.7,
    max_tokens = 200,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0,
)