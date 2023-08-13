def front_x(words):
  result = []
  for word in words:
    print("word: ", word)
    print(1)
    if word[0:1] == 'x':
      print('ytyiyiuy', word)
      result.append(word)
      words.remove(word)
      print("LIST OF words 2: ", words)
      
  # print("words: ", words, '\n')
  # print("result: ", result, '\n')
  # words.sort()
  # result.sort()
  # result.extend(words)
  return result

print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
# print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
# print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))