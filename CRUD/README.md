Exercicio Proposto de CRUD para Treinamento SURE
https://github.com/visure/visure-training


Project Scope
#POST
    1 - receber (json)
    se recebeu algo, armazena tudo (temporariamente) e:
        2 - valida (dados)
        se dados válidos
            3 - trata dados (formatação para inserção no db)
            retorna: "dados inseridos com sucesso"
        se não, retorna erro: "dados inválidos".
    4 - executa ação (Post, inserção no db)
    se não, retorna erro: "sem dados"

#GET
    1 a partir da url, retornar % de usuarios por gênero
    2 a partir da url, retornar % de usuarios por região do Brasil
    3 a partir da url, retornar % de usuarios por estado do Brasil
    4 a partir da url, retornar % de usuarios por idade, seguindo modelo predeterminado (13-17, 18-24, 25-34, 35-44, 45-54, 55-64 e 65+)

#PUT
    A partir da url (neste caso id do usuario), ATUALIZAR dados de um usuario específico.
    /update/<document> json com dicionario com novos dados (chave/valor)

#DELETE
    1 - A partir da url (neste caso documento do usuario), APAGAR dados de um usuario específico.
    /delete/<document>
        Neste caso os dados não deverão ser apagados, apenas o valor de "use_status" deve ser alterado
        de 1 para 0, o que indica que o usuário ficará inativo no sistema, não participando assim das buscas do GET, por exemplo.

References:
https://flask.palletsprojects.com/en/1.1.x/views/
https://httpstatuses.com/