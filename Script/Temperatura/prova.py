

class prova:
    def __call__(self, ciao, *args, **kwargs):
        print("ciao"+str(ciao))

f=prova()
f(10)