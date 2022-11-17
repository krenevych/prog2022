def func(*args, **kwargs):
    print("Позиційні: ", args)
    print("Ключові:", kwargs)

func(1, 2, 3, 14, "Hello", arg0=0, arg1=7, par2="Hello", par999="987")