# 1. Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.
class usuario:
    def __init__(self, nome:str, email:str):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"O usuário {self.nome} tem o seguinte email: {self.email}" )

    def saudacao(self):
        print("Olá, usuário!")

class cliente(usuario):
    
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo
    
    def saudacao(self):
        return f"Olá, cliente! seu saldo é {self.saldo}"
    

    
helmer = cliente("Felix","hfelixmsouza@gmail.com",100)


print(helmer.nome)
print(helmer.email)
print(helmer.saldo)


# 2. Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.
print(helmer.exibir_informacoes())

# 3. Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.
print(helmer.saudacao())

# 4. Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().
# está na classe!

# 5. Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.
class funcionario(usuario):
    pass

class gerente(funcionario):
    pass

joao = gerente("joau", "joazin@123.com")

print(joao.email)


# 6. Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?
class autenticacao:
    def login(self, usuario, senha):
        if usuario == "helmer" and senha == "caju123":
            return "Login bem-sucedido!"
        else:
            return "Usuário ou senha incorretos."
        
    def status(self):
        return f"status 1"    

class permissao():
    def verificar_permissao(self, nivel):
        if nivel == "admin":
            return "Permissão concedida."
        else:
            return "Permissão negada."
    
    def status(self):
        return f"status 2"

class administrador(autenticacao,permissao):
    pass

adm = administrador()

print(adm.login("helmer","caju123"))
print(adm.verificar_permissao("admin"))

# 7. Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.
print(adm.status())
print(administrador.__mro__)

#o motivo que ele prioriza o metodo status da classe autenticação é que eu defini ela como 'prioridade' na herança da classe administrador,