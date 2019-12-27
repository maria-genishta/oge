def generate_oge_task10(mode='no test') -> (str, str):
    assert(mode == 'test' or mode == 'no test')
    if mode == 'test':
        pass  # напишите код сами
    else:
        question = random.choice(['максимальное', 'минимальное'])
        q = random.randint(3, 8)
        binary_num, oct_num, six_num = '1', str(random.randint(1, 7)), str(random.randint(1,9))
        for i in range(q):
            binary_num += str(random.randint(0,1))
        v = random.randint(1,2)
        for i in range(v):
            oct_num +=str(random.randint(0,7))
        for i in range(1):
            six_num += str(random.randint(0,9))
        binary_num_10 = int(binary_num, 2)
        oct_num_10 = int(oct_num, 8)
        six_num_10 = int(six_num, 16)
        if question == 'максимальное':
            ans = max(binary_num_10, oct_num_10, six_num_10)
        else:
            ans = min(binary_num_10, oct_num_10, six_num_10)
        
    task_text = ('Среди приведённых ниже трёх чисел, записанных в различных системах счисления, найдите {} и запишите его в ответе в десятичной системе счисления.'.format(question)+
    '\n' + 'В ответе запишите только число, основание системы счисления указывать не нужно.'+'\n'+'\t'+str(six_num) + '₁₆, '+str(oct_num)+'₈, '+str(binary_num)+'₂, ')
    return str(ans), task_text


def generate_oge_task5_improved(mode='no test') -> (str, str):
    assert(mode == 'test' or mode == 'no test')
    if mode == 'test':
        robot_name = 'Альфа'
        start_number = 47
        add_number = 2
        algorithm = '12111'
        divide_number = 7
    else:
        robot_name = random.choice(['Альфа', 'Бета', 'Омега'])
        start_number = random.randint(1, 10)
        add_number = random.randint(1, 10)
        algorithm = list('11111')
        index = random.randint(0, len(algorithm) - 1)
        algorithm[index] = '2'
        a = start_number+index*add_number
        b = []
        for i in range(1, a+1):
            if a%i == 0:
                b.append(i)
        divide_number = random.choice(b)
    end_number = start_number
    for i in algorithm:
        if i == '1':
            end_number += add_number
        else:
            end_number //= divide_number
    task_text = ('У исполнителя {} две команды, которым присвоены номера:'.format(robot_name)+'\n'+'\t'+'1. прибавь {};'.format(add_number) + '\n' +'\t'+'2. раздели на b' + '\n' + '\t' + '(b — неизвестное натуральное число; b ≥ 2).' + '\n' + 'Выполняя первую из них, {} увеличивает число на экране на {}, а выполняя вторую, делит это число на b.'.format(robot_name, add_number)
    +'\n' + 'Программа для исполнителя {} — это последовательность номеров команд.'.format(robot_name) + '\n' + 'Известно, что программа {} переводит число {} в число {}.'.format(''.join(algorithm), start_number, end_number) + '\n' + '\n' + 'Определите значение b.' + '\n')
    return  task_text, str(divide_number)

def generate_oge_task5(mode='no test') -> (str, str):
    assert(mode == 'test' or mode == 'no test')
    # В дальнейшем тестирующий режим вы будете реализовывать самостоятельно.
    # В данном случае это сделано за вас, чтобы вы примерно поняли идею.
    if mode == 'test':
        robot_name = 'Альфа'
        start_number = 6
        add_number = 1
        multiply_number = 10
        algorithm = '11211'

    else:
        robot_name = random.choice(['Альфа', 'Бета', 'Омега']) # можете добавить ещё букв
        start_number = random.randint(1, 10)
        add_number = random.randint(1, 10)
        multiply_number = random.randint(2, 20)
        algorithm = list('11111')
        algorithm[random.randint(0, len(algorithm) - 1)] = '2'
        algorithm = ''.join(algorithm)
    end_number = start_number
    for i in range(len(algorithm)):
        if algorithm[i] == '1':
            end_number += add_number
        else:
            end_number *= multiply_number   
    task_text = ('У исполнителя ' + str(robot_name) + ' две команды, которым присвоены номера:' + '\n'+'\t' + '1. Прибавь ' + str(add_number)+';' + '\n'+'\t' + '2. Умножь на b'  + '\n' + '\t'+'(b — неизвестное натуральное число; b ≥ 2).' + 
                     '\n'+'Выполняя первую из них, ' + str(robot_name) + ' увеличивает число на экране на ' + str(add_number) + ', а выполняя вторую, умножает это число на b.' +
                     '\n' + 'Программа для исполнителя ' + str(robot_name) +' — это последовательность номеров команд.' +'\n' + 'Известно, что программа ' + str(algorithm) +
                     ' переводит число ' + str(start_number) + ' в число ' + str(end_number)) + '.'+ '\n' + '\n' + 'Определите значение b.' + '\n'
    return task_text, str(multiply_number)

