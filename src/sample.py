def say_hello(name=None):
    if name:
        return 'Hello mr {} !'.format(name)
    else:
        raise Exception('Can not greet to invisible !')


if __name__ == '__main__':
    greet = say_hello('niamath')
    print(greet)
