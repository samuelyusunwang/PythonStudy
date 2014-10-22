# eval_loop

def eval_loop():
    print('Input the command and evaluate')
    
    while True:
        line = input('> ')
        if line == 'done':
            break
        else:
            print(eval(line))
            

# test code
eval_loop()