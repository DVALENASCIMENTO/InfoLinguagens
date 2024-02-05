# linguagens_de_programacao.py

class LinguagemDeProgramacao:
    def __init__(self, nome, versao, data_criacao, criador, semantica, tipagem, paradigma,
                 compilada_interpretada, assincrona, bibliotecas_frameworks, comunidade_ativa,
                 portabilidade, desempenho, uso, aplicacoes):
        self.nome = nome
        self.versao = versao
        self.data_criacao = data_criacao
        self.criador = criador
        self.semantica = semantica
        self.tipagem = tipagem
        self.paradigma = paradigma
        self.compilada_interpretada = compilada_interpretada
        self.assincrona = assincrona
        self.bibliotecas_frameworks = bibliotecas_frameworks
        self.comunidade_ativa = comunidade_ativa
        self.portabilidade = portabilidade
        self.desempenho = desempenho
        self.uso = uso
        self.aplicacoes = aplicacoes

    def obter_informacoes(self):
        return {
            "Nome": self.nome,
            "Versão": self.versao,
            "Data de Criação": self.data_criacao,
            "Criador": self.criador,
            "Semântica": self.semantica,
            "Tipagem": self.tipagem,
            "Paradigma": self.paradigma,
            "Compilada ou Interpretada": "Compilada" if self.compilada_interpretada else "Interpretada",
            "Assíncrona": "Sim" if self.assincrona else "Não",
            "Bibliotecas/Frameworks": self.bibliotecas_frameworks,
            "Comunidade Ativa": "Sim" if self.comunidade_ativa else "Não",
            "Portabilidade": self.portabilidade,
            "Desempenho": self.desempenho,
            "Uso": self.uso,
            "Aplicações": self.aplicacoes
        }

# Dicionário com informações de diferentes linguagens de programação
linguagens = {
    "JavaScript": LinguagemDeProgramacao(
        "JavaScript", "ES6", "Dezembro de 1995", "Netscape", "Dinâmica", "Fraca e Dinâmica",
        "Multiparadigma (Orientada a Objetos, Imperativa, Funcional)", True, True,
        ["React", "Angular", "Node.js"], True, "Multiplataforma", "Variável", "Web development",
        ["Desenvolvimento web", "Desenvolvimento de aplicações cliente-servidor"]
    ),
    "Python": LinguagemDeProgramacao(
        "Python", "3.9", "Dezembro de 1989", "Guido van Rossum", "Dinâmica", "Dinâmica",
        "Multiparadigma (Orientada a Objetos, Imperativa, Funcional)", False, True,
        ["Django", "Flask"], True, "Multiplataforma", "Interpretada", "Web development, Data Science",
        ["Desenvolvimento web", "Ciência de dados", "Automatização de tarefas"]
    ),
    "Java": LinguagemDeProgramacao(
        "Java", "15", "1995", "Sun Microsystems", "Estática", "Fortemente Tipada",
        "Orientada a Objetos", True, False, ["Spring", "Hibernate"], True, "Multiplataforma",
        "Compilada", "Desenvolvimento de aplicações empresariais",
        ["Desenvolvimento de aplicações empresariais", "Desenvolvimento Android"]
    ),
    "C#": LinguagemDeProgramacao(
        "C#", "9.0", "2000", "Microsoft", "Estática", "Estática",
        "Multiparadigma (Orientada a Objetos, Imperativa)", "Compilada", False, [".NET Core", "ASP.NET Core"],
        True, "Multiplataforma (com .NET Core)", "Alto", "Desenvolvimento de aplicativos Windows",
        ["Desenvolvimento de aplicativos empresariais"]
    ),
    "C++": LinguagemDeProgramacao(
        "C++", "ISO/IEC 14882:2020", "1983", "Bjarne Stroustrup", "Estática", "Estática",
        "Multiparadigma (Orientada a Objetos, Imperativa, Genérica)", "Compilada", False, ["STL"],
        True, "Multiplataforma", "Alto", "Sistemas embarcados, Jogos", ["Desenvolvimento de sistemas críticos"]
    ),
    "TypeScript": LinguagemDeProgramacao(
        "TypeScript", "4.4", "Outubro de 2012", "Microsoft", "Estática", "Estática",
        "Multiparadigma (Orientada a Objetos, Imperativa)", "Compilada", False, ["React", "Angular"],
        True, "Multiplataforma", "Alto", "Desenvolvimento web", ["Desenvolvimento web moderno"]
    ),
    "PHP": LinguagemDeProgramacao(
        "PHP", "8.0", "1995", "Rasmus Lerdorf", "Dinâmica", "Fraca e Dinâmica",
        "Imperativa", "Interpretada", False, ["Laravel", "Symfony"], True, "Multiplataforma", "Variável",
        "Desenvolvimento web", ["Desenvolvimento de sites dinâmicos"]
    ),
    "C": LinguagemDeProgramacao(
        "C", "ISO/IEC 9899:2018", "1972", "Dennis Ritchie", "Estática", "Estática",
        "Imperativa", "Compilada", False, [], True, "Multiplataforma", "Alto",
        "Desenvolvimento de sistemas operacionais",
        ["Desenvolvimento de sistemas embarcados"]
    ),
    "Swift": LinguagemDeProgramacao(
        "Swift", "5.5", "Junho de 2014", "Apple", "Estática", "Estática",
        "Multiparadigma (Orientada a Objetos, Funcional)", "Compilada", False, ["UIKit", "SwiftUI"],
        True, "Multiplataforma (Apple)", "Alto", "Desenvolvimento iOS", ["Desenvolvimento de aplicativos iOS"]
    ),
    "Objective-C": LinguagemDeProgramacao(
        "Objective-C", "1984", "Início dos anos 1980", "Brad Cox, Tom Love", "Estática e Dinâmica", "Estática e Dinâmica",
        "Multiparadigma (Orientada a Objetos, Imperativa)", "Compilada", False, ["Cocoa", "Cocoa Touch"],
        True, "MacOS, iOS", "Moderado", "Desenvolvimento de aplicativos para MacOS e iOS",
        ["Desenvolvimento de aplicativos para MacOS e iOS"]
    ),
    "Ruby": LinguagemDeProgramacao(
        "Ruby", "3.0.3", "1995", "Yukihiro Matsumoto", "Dinâmica", "Dinâmica",
        "Orientada a Objetos", "Interpretada", False, ["Ruby on Rails"], True, "Multiplataforma", "Moderado",
        "Desenvolvimento web, Automação de tarefas", ["Desenvolvimento web", "Automação de tarefas"]
    ),
    "Go": LinguagemDeProgramacao(
        "Go", "1.17", "2009", "Google", "Estática", "Estática", "Concorrente, Imperativa", "Compilada",
        True, ["Standard Library"], True, "Multiplataforma", "Alto", "Desenvolvimento de sistemas distribuídos",
        ["Desenvolvimento de servidores", "Sistemas distribuídos"]
    ),
    "Rust": LinguagemDeProgramacao(
        "Rust", "1.56.1", "Julho de 2010", "Mozilla", "Estática", "Estática",
        "Multiparadigma (Concorrente, Funcional, Imperativa)", "Compilada", True, ["Tokio"],
        True, "Multiplataforma", "Alto", "Desenvolvimento de sistemas de baixo nível",
        ["Desenvolvimento de sistemas operacionais", "Desenvolvimento de linguagens de sistemas"]
    ),
    "Kotlin": LinguagemDeProgramacao(
        "Kotlin", "1.5.30", "Julho de 2011", "JetBrains", "Estática", "Estática",
        "Multiparadigma (Orientada a Objetos, Funcional)", "Compilada", True, ["Ktor"],
        True, "Multiplataforma", "Moderado", "Desenvolvimento Android, Web", ["Desenvolvimento Android"]
    ),
    "Shell Script": LinguagemDeProgramacao(
        "Shell Script", "Varia", "1970s", "Stephen R. Bourne", "Dinâmica", "Dinâmica",
        "Imperativa", "Interpretada", True, [], True, "Varia", "Baixo",
        "Automatização de tarefas do sistema operacional", ["Automatização de tarefas do sistema operacional"]
    ),
    "Scala": LinguagemDeProgramacao(
        "Scala", "3", "2003", "Martin Odersky", "Estática", "Estática",
        "Multiparadigma (Orientada a Objetos, Funcional)", "Compilada", True, ["Akka"],
        True, "Multiplataforma", "Alto", "Desenvolvimento de sistemas distribuídos",
        ["Desenvolvimento web", "Processamento de dados em larga escala"]
    ),
    "SQL": LinguagemDeProgramacao(
        "SQL", "Varia", "Anos 1970", "IBM", "Varia", "Varia",
        "Declarativa", "Interpretada (em bancos de dados)", True, ["MySQL", "PostgreSQL"],
        True, "Varia", "Varia", "Manipulação de dados em bancos de dados", ["Desenvolvimento de bancos de dados"]
    ),
    "MATLAB": LinguagemDeProgramacao(
        "MATLAB", "R2021b", "1984", "MathWorks", "Dinâmica", "Fraca e Dinâmica",
        "Multiparadigma (Orientada a Matrizes, Funcional)", "Interpretada", True, ["Simulink"],
        True, "Multiplataforma", "Moderado", "Computação numérica, Simulações", ["Engenharia, Ciência"]
    ),
    "R": LinguagemDeProgramacao(
        "R", "4.1.1", "1993", "Ross Ihaka, Robert Gentleman", "Dinâmica", "Fraca e Dinâmica",
        "Multiparadigma (Orientada a Objetos, Funcional)", "Interpretada", True, ["ggplot2"],
        True, "Multiplataforma", "Moderado", "Estatística, Análise de dados", ["Estatística"]
    ),
    "UML": LinguagemDeProgramacao(
        "UML", "2.5.1", "Novembro de 1997", "Grady Booch, James Rumbaugh, Ivar Jacobson", "Não aplicável", "Não aplicável",
        "Modelagem", "Não aplicável", False, [], True, "Não aplicável", "Não aplicável",
        "Modelagem de software", ["Documentação de software", "Análise de sistemas"]
    ),
    # Adicione mais informações conforme necessário
}
