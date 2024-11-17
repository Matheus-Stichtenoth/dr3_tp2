O PRIMEIRO PASSO É FAZER A INSTALAÇÃO DO REQUIREMENTS.TXT

\n Parte 1:

\n Exercicio 1:

\n Exercicio 2:








\n Parte 2:

\n Exercício 1:
    1° - Executar o arquivo 'question.py' do diretório 'models' \n
    2° - Executar o arquivo 'question.py' do diretório 'routers' \n
    3° - Executar o arquivo 'main_2_1.py' do diretório 'parte2_1' \n
    Após realizar esses 3 passos, deverá rodar o seguinte código no terminal, dentro do diretório tp2: \n
        uvicorn src.parte2_1.main_2_1:app --reload \n
    O servidor irá iniciar, e após isso basta executar a requisição via terminal também: \n
        http POST http://127.0.0.1:8000/chat/ask/ question="Olá" \n
    Caso o comando acima retorne um erro de excesso de requisições nessa porta, você poderá rodar o seguinte código: \n
        uvicorn src.parte2_1.main_2_1:app --reload --port 8001 \n
    Isso irá alterar a porta, e não deverá mais gerar o erro. Como fizemos essa alteração, deveremos mudar também a requisição POST: \n
        http POST http://127.0.0.1:8001/chat/ask/ question="Olá" \n

\n Exercício 2:
    1° - Executar o arquivo 'translator.py' do diretório 'models' \n
    2° - Executar o arquivo 'translator_openai.py' do diretório 'routers' \n
    3° - Executar o arquivo 'main_2_2.py' do diretório 'parte2_2' \n
    Após realizar esses 3 passos, deverá rodar o seguinte código no terminal, dentro do diretório tp2: \n
        uvicorn src.parte2_2.main_2_2:app --reload \n
    O servidor irá iniciar, e após isso basta executar a requisição via terminal também: \n
        http POST http://127.0.0.1:8000/chat/translator_openai/ message="Hello! How are you?" \n
    Caso o comando acima retorne um erro de excesso de requisições nessa porta, você poderá rodar o seguinte código: \n
        uvicorn src.parte2_2.main_2_2:app --reload --port 8001 \n
    Isso irá alterar a porta, e não deverá mais gerar o erro. Como fizemos essa alteração, deveremos mudar também a requisição POST: \n
        http POST http://127.0.0.1:8001/chat/translator_openai/ message="Hello! How are you?" \n