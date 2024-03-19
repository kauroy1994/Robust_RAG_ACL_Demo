from openai import OpenAI
from Solver import resolve

client = OpenAI()

class RRAG(object):

  @staticmethod
  def chunk_format(chunk_text):
    text = chunk_text
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      response_format={ "type": "json_object" },
      messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "f{Convert the following into yes-or-no question-answer sets by resolving all ambiguous references \n \n {text}}?"}
      ]
    )
    return response.choices[0].message.content
    
  @staticmethod
  def question_decompose(question_text):
    text = question_text
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      response_format={ "type": "json_object" },
      messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "f{Convert the following into yes-or-no question-answer sets by resolving all ambiguous references \n \n {text}}?"}
      ]
    )
    return response.choices[0].message.content

@staticmethod
def resolve(question_list):
  return Solver.resolve(question_list)
