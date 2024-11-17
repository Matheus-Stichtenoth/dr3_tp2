O PRIMEIRO PASSO É FAZER A INSTALAÇÃO DO REQUIREMENTS.TXT <br/>

Parte 1:

    Exercicio 1:

    Exercicio 2:








Parte 2:

Exercício 1:

     1° - Executar o arquivo 'question.py' do diretório 'models'
     2° - Executar o arquivo 'question.py' do diretório 'routers'
     3° - Executar o arquivo 'main_2_1.py' do diretório 'parte2_1'
     Após realizar esses 3 passos, deverá rodar o seguinte código no terminal, dentro do diretório tp2: 
        uvicorn src.parte2_1.main_2_1:app --reload 
    O servidor irá iniciar, e após isso basta executar a requisição via terminal também: 
        http POST http://127.0.0.1:8000/chat/ask/ question="Olá" 
    Caso o comando acima retorne um erro de excesso de requisições nessa porta, você poderá rodar o seguinte código: 
        uvicorn src.parte2_1.main_2_1:app --reload --port 8001 
    Isso irá alterar a porta, e não deverá mais gerar o erro. Como fizemos essa alteração, deveremos mudar também a requisição POST: 
        http POST http://127.0.0.1:8001/chat/ask/ question="Olá" 

Exercício 2:

    1° - Executar o arquivo 'translator.py' do diretório 'models' 
    2° - Executar o arquivo 'translator_openai.py' do diretório 'routers' 
    3° - Executar o arquivo 'main_2_2.py' do diretório 'parte2_2' 
    Após realizar esses 3 passos, deverá rodar o seguinte código no terminal, dentro do diretório tp2: 
        uvicorn src.parte2_2.main_2_2:app --reload 
    O servidor irá iniciar, e após isso basta executar a requisição via terminal também: 
        http POST http://127.0.0.1:8000/chat/translator_openai/ message="Hello! How are you?" 
    Caso o comando acima retorne um erro de excesso de requisições nessa porta, você poderá rodar o seguinte código: 
        uvicorn src.parte2_2.main_2_2:app --reload --port 8001 
    Isso irá alterar a porta, e não deverá mais gerar o erro. Como fizemos essa alteração, deveremos mudar também a requisição POST: 
        http POST http://127.0.0.1:8001/chat/translator_openai/ message="Hello! How are you?" 

Exercício 3:

    1° - Executar o arquivo 'translator_germany.py' do diretório 'models' 
    2° - Executar o arquivo 'translator_germany.py' do diretório 'routers' 
    3° - Executar o arquivo 'main_2_3.py' do diretório 'parte2_3' 
    Após realizar esses 3 passos, deverá rodar o seguinte código no terminal, dentro do diretório tp2: 
        uvicorn src.parte2_3.main_2_3:app --reload 
    O servidor irá iniciar, e após isso basta executar a requisição via terminal também: 
        http POST http://127.0.0.1:8000/chat/translator_germany/ message="Hello! How are you?" 
    Caso o comando acima retorne um erro de excesso de requisições nessa porta, você poderá rodar o seguinte código: 
        uvicorn src.parte2_3.main_2_3:app --reload --port 8001 
    Isso irá alterar a porta, e não deverá mais gerar o erro. Como fizemos essa alteração, deveremos mudar também a requisição POST: 
        http POST http://127.0.0.1:8001/chat/translator_germany/ message="Hello! How are you?"