def arithmetic_arranger(problems, solutions=False):
  arranged_problems = ""

  if (len(problems) > 5):
    return "Error: Too many problems."

  top = []
  bottom = []
  operator = []
  results = []
  problem_len = []

  for i in range(len(problems)):
    problem = problems[i].split()
    

    #parse each individual problem and sort into top and bottom
    # have operation in seperate list
    # go thru each list to find the sum or difference
    if(problem[0].isdigit()):
      top.append(int(problem[0]))
    else: 
      return 'Error: Numbers must only contain digits.'
      
    operator.append(problem[1])
    if(problem[2].isdigit()):
      bottom.append(int(problem[2]))
    else:
      return 'Error: Numbers must only contain digits.'
    
    if ((max(len(str(top[i])), len(str(bottom[i])))) < 5):
      problem_len.append(max(len(str(top[i])), len(str(bottom[i]))))
    else:
      return 'Error: Numbers cannot be more than four digits.'

  for i in range(len(problems)):
    if (operator[i] == '+'):
      results.append(top[i] + bottom[i])
    elif (operator[i] == '-'):
      results.append(top[i] - bottom[i])
    else:
      return "Error: Operator must be '+' or '-'."

  #print(problem)
  #print(results)

  #format the top strings
  for i in range(len(problems)):
    num_space = problem_len[i] - len(str(top[i])) + 2

    arranged_problems += " " * num_space

    arranged_problems += str(top[i])
    if( i != len(problems) - 1):
      arranged_problems += " " * 4
  
  arranged_problems += '\n'
  #format the bottom strings
  for i in range(len(problems)):
    arranged_problems += operator[i]
    num_space = problem_len[i] - len(str(bottom[i])) + 1
    arranged_problems += " " * num_space

    arranged_problems += str(bottom[i])
    if( i != len(problems) - 1):
      arranged_problems += " " * 4

  arranged_problems += '\n'

  for i in range(len(problems)):
    arranged_problems += '-' * (problem_len[i] + 2)
    if( i != len(problems) - 1):
      arranged_problems += " " * 4

  if(solutions):
    arranged_problems += '\n'
    for i in range(len(problems)):
      
      num_space = problem_len[i] - len(str(results[i])) + 2
      arranged_problems += " " * num_space
      arranged_problems += str(results[i])
      if( i != len(problems) - 1):
        arranged_problems += " " * 4
      
    
    

  return arranged_problems
