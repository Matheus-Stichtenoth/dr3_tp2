O PRIMEIRO PASSO É FAZER A INSTALAÇÃO DO REQUIREMENTS.TXT

Parte 1:

    Exercicio 1:

    Exercicio 2:








Parte 2:

Exercício 1:
    <br/> 1° - Executar o arquivo 'question.py' do diretório 'models'
    <br/> 2° - Executar o arquivo 'question.py' do diretório 'routers'
    <br/> 3° - Executar o arquivo 'main_2_1.py' do diretório 'parte2_1'
    <br/> Após realizar esses 3 passos, deverá rodar o seguinte código no terminal, dentro do diretório tp2: <br/>
        uvicorn src.parte2_1.main_2_1:app --reload <br/>
    O servidor irá iniciar, e após isso basta executar a requisição via terminal também: <br/>
        http POST http://127.0.0.1:8000/chat/ask/ question="Olá" <br/>
    Caso o comando acima retorne um erro de excesso de requisições nessa porta, você poderá rodar o seguinte código: <br/>
        uvicorn src.parte2_1.main_2_1:app --reload --port 8001 <br/>
    Isso irá alterar a porta, e não deverá mais gerar o erro. Como fizemos essa alteração, deveremos mudar também a requisição POST: <br/>
        http POST http://127.0.0.1:8001/chat/ask/ question="Olá" <br/>

\n Exercício 2:
    1° - Executar o arquivo 'translator.py' do diretório 'models' <br/>
    2° - Executar o arquivo 'translator_openai.py' do diretório 'routers' <br/>
    3° - Executar o arquivo 'main_2_2.py' do diretório 'parte2_2' <br/>
    Após realizar esses 3 passos, deverá rodar o seguinte código no terminal, dentro do diretório tp2: <br/>
        uvicorn src.parte2_2.main_2_2:app --reload <br/>
    O servidor irá iniciar, e após isso basta executar a requisição via terminal também: <br/>
        http POST http://127.0.0.1:8000/chat/translator_openai/ message="Hello! How are you?" <br/>
    Caso o comando acima retorne um erro de excesso de requisições nessa porta, você poderá rodar o seguinte código: <br/>
        uvicorn src.parte2_2.main_2_2:app --reload --port 8001 <br/>
    Isso irá alterar a porta, e não deverá mais gerar o erro. Como fizemos essa alteração, deveremos mudar também a requisição POST: <br/>
        http POST http://127.0.0.1:8001/chat/translator_openai/ message="Hello! How are you?" <br/>