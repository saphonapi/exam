def isBalanced(exp):
  
    # Initialising Variables
    flag = True
    count = 0

    newexp = []
    for i in exp1:
        if i == '(':
            newexp.append(i)
        
        elif i == ')':
            newexp.append(i)
    exp = ''.join(newexp)   
  
    
    for i in range(len(exp)):
        if (exp[i] == '('):
            count += 1
        else:           
            count -= 1
  
        if (count < 0):          
            flag = False
            break
  
    if (count != 0):
        flag = False
  
    return flag
  
# Driver code
if __name__ == '__main__':
      
  
    print("Please enter a string has valid nesting of brackets:") 
    x = input()
    exp1 = x
  
    if (isBalanced(exp1)):
        print("true")
    else:
        print("false")
  
