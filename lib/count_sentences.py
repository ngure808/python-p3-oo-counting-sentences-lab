#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
        self._value = value if isinstance(value, str) else ""
    
  @property
  def value(self):
        return self._value
    
  @value.setter
  def value(self, new_value):
    if not isinstance(new_value, str):
      print("The value must be a string.")
    else:
      self._value = new_value
    
  def is_sentence(self):
     return self._value.endswith(".")
    
  def is_question(self):
     return self._value.endswith("?")
    
  def is_exclamation(self):
     return self._value.endswith("!")
    
  def count_sentences(self):
    if not self._value:
      return 0
        
    import re
    sentences = re.split(r'[.!?]', self._value)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return len(sentences)
