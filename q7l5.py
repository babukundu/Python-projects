def long_enough(strings, min_length):
   result_string = []
   for word in strings:
      if len(word) >= min_length:
         result_string.append(word)
   return result_string