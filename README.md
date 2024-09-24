Registro de usuário: os usuários podem criar uma conta digitando seu nome, endereço de e-mail e senha. 
Os dados são armazenados em um banco de dados MongoDB.


Login do usuário: os usuários podem fazer login com seu e-mail e senha.
A autenticação verifica se as credenciais correspondem aos dados armazenados.





 Número de usuários: A aplicação possui um caminho que permite contar a quantidade de usuários cadastrados no banco de dados.
 

 Integração  Big Data: Processamento de dados em grande escala: Após cadastrar um novo usuário, inicia-se um processo que simula o processamento de grandes volumes de dados.
 

 Usando Pandas e Dask: A biblioteca Pandas é usada para criar e manipular um DataFrame, enquanto Dask é usada para operações em larga escala, permitindo ler e analisar dados além da capacidade de memória.
 


 Simulação de análise: Um arquivo CSV é gerado a partir dos dados e as operações de separarações e reuniões são realizadas com Dask, demonstrando a capacidade de processar grandes volumes de dados.
 

 Estrutura: Frontend: Usando Font Awesome para ícones sociais e design responsivo baseado em CSS. 
 

Backend: Implementado com Flask, que permite gerenciamento de rotas e integração com MongoDB para persistência de dados. 


Esta aplicação é um exemplo prático de como integrar uma interface de usuário com um backend poderoso, utilizando técnicas de big data para análise e manipulação de dados.
