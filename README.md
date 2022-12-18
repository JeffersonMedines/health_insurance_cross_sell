![insurance-producer_16](https://user-images.githubusercontent.com/93053350/208117801-629cf869-7d39-461d-b6e9-e41d12e59504.jpg)


# Rankeamento dos Clientes Pela Propenção de Compra de um Segundo Seguro (Cross-Sell)



<h1> Índice </h1>

<h3>

• [Problemas de Negócio](https://github.com/JeffersonMedines/health_insurance_cross_sell#-problemas-de-neg%C3%B3cio-)

• [Premissas do Negócio](https://github.com/JeffersonMedines/health_insurance_cross_sell#-premissas-do-neg%C3%B3cio-)

• [Planejamento da Solução](https://github.com/JeffersonMedines/health_insurance_cross_sell#-planejamento-da-solu%C3%A7%C3%A3o-)

• [Machine Learning e Métricas de Performance](https://github.com/JeffersonMedines/health_insurance_cross_sell#-machine-learning-e-m%C3%A9tricas-de-performance-)

• [Resultados Financeiros para o Negócio](https://github.com/JeffersonMedines/health_insurance_cross_sell#-resultados-financeiros-para-o-neg%C3%B3cio-)

• [Deploy do Modelo em Produção](https://github.com/JeffersonMedines/health_insurance_cross_sell#-deploy-do-modelo-em-produ%C3%A7%C3%A3o-)

• [Próximos Passos](https://github.com/JeffersonMedines/health_insurance_cross_sell#-deploy-do-modelo-em-produ%C3%A7%C3%A3o-)
 
 </h3>

<h1> Problemas de Negócio </h1>

<p> A Dafa Insurance é uma empresa que oferece o serviço de segura de vida para seus clientes e a equipe de produtos está analisando a possibilidade de oferecer aos seus segurados um novo produto, o seguro de carro. </p>

<p> Assim como no seguro de saúde, os clientes desse novo seguro de carro devem pagar um valor anual à Dafa Insurance para poder receber um valor segurado pela empresa caso o segurado venha a sofrer algum tipo acidente ou dano no veículo. Por exemplo, um segurado que pague R$ 5.000,00 ao ano para ter o seguro de saúde que tem uma cobertura de R$ 100.000,00, caso tenha a infeicidade de ser hospitalizado por algum motivo, terá suas despezas pagas pela segurado até o valor de R$ 100.000,00 desde que esteja em dia com sua obrigação de pagar o valor anual de R$ 5.000,00 paga a seguradora. </p>

<p> A Dafa Insurance realizou uma pesquisa com aproximadamente 380.000 clientes que consomem seu serviço de plano de saúde para saber seu interesse em adquirir um novo seguro de carro. As informações sobre cada cliente foram armazenadas em um banco de dados juntamente com a resposta em relação ao seu interesse ao novo produto. </p>

<p> A equipe de produtos selecionou 132 mil novos clientes que não responderam a pesquisa sobre o interesse ao novo produto para participarem a uma campanha que será ofertado esse novo produto de seguro de carro. O contato aos clintes será feito através de ligações telefônicas feitas pelo time de vendas. </p>

<p> Porém, dada a capacidade de ligações diárias e o período em que a campanha será aplicada, o time de vendas conseguirá realizar apenas 20 mil ligações ofertando o novo produto durante essa campanha. Dessa forma, é necessário criar um modelo preditivo que classifique quais clientes estarão interessados em adquirir esse novo seguro de carro para que a equipe de vendas contate o maior número de interessados possível. </p>

<h1> Premissas do Negócio </h1>

<p> Policy Sales Channel: Essa variável indica qual a forma que o cliente deseja ser contatado, tendo mais de 160 valores diferentes, não é passado nenhuma informação se cada valor expressa cada meio de contato ou se existem grupos e valores que expressam o mesmo meio de contato mas que de alguma forma se diferencie. Por isso, será assumido que cada valor expressa um meio de contato diferente. </p>

<p> Como não é informado o valor do preço do seguro de carro e nem o custo de ligação para o cliente, para fins de tradução do desempenho do modelo para retorno financeiro para o negócio, será assumido que a média anual do preço do seguro de carro ofertado seja de R$ 2.000,00 e que o custo de ligação para entrar em contato com o cliente oferecendo o produto seja de R$ 100,00. </p>


<h1> Planejamento da Solução </h1>

<p> Este projeto será desenvolvido com base no Processo Padrão Inter-Indústrias para Mineração de Dados (CRISP-DM). Uma metodologia padronizada de projetos de ciência de dados com etapas bem definidas e ordenadas: entendimento do negócio, entendimento dos dados, prepração dos dados, modelagem, avaliação e implementação. Dessa forma, quando utilizamos a metodologia CRIPS-DM, o projeto de ciência de dados passa a ter um ciclo de vida circular. Mesmo quando o projeto chega na etapa de implementação, o projeto pode ser novamente iniciado pela etapa de entendimento do negócio. </p>

<p> O intuito desa metodologia é que o cientista passe inicialmente por todos os passos do projeto da forma mais rápida possível. Mas como isso pode ajudar no desenvolvimento do projeto e na agregação de valor para a empresa? Ao passar por todas as etapas do projeto de maneira rápida já é possível identificar qualquer problema que impeça o projeto de ser desenvolvido, reduzindo custos no caso de construir um projeto excelente já na primeira entrega o que demandaria mais tempo e investimento para no final descobrir o problema que impede o desenvolvimento do projeto. Ao desenvolver uma solucção inicial rápida, a empresa já está sendo beneficiada financeiramente ainda que pouco nessa primeira versão do projeto em quanto uma solução mais robusta é construída em uma próxima iteração do CRISP-DM. </p>

<p> Assim, o objetivo é que se faça quantas iteraões forem necessárias do CRISP-DM até que se apresente uma solução condizente com as expectativas da empresa. Além disso, o  CRISP-DM pode até ser considerada uma metodologia ágil já que possibilita ao cientista um desenvolvimento de projeto e agregação de valor para a empresa de forma mais eficiente e inteligente. </p>

![crisp dm](https://user-images.githubusercontent.com/93053350/208129563-6f933191-f522-4603-bf98-06b3f0db9937.jpg)


<h1> Machine Learning e Métricas de Performance </h1>

<p> Para avaliar o desempenho dos algoritmos de machine learning, foram selecionadas duas métricas, Precision@K e Racall@K. A métrica precision mede o desempenho do modelo apenas em relação as previsões que o modelo fez, ou seja, uma precision de 0.25 nos diz que a cada 4 previsões que o modelo fizer dizendo que o cliente tem interesse, ele irá acertar 1 onde o cliente de fato tinha interesse. Já a métrica recall nos mostra o desempenho do modelo em relação a todos os dados, tanto aqueles que o algoritmo classificou, tanto aqueles que ele não classificou, logo, uma recall de 0.25 nos diz que de todos os clientes interessados nessa base de dados, o nosso modelo conseguiu prever 25% deles. </p>

<p> Porém, essas são métricas utilizadas para problemas clássicos de classificação, onde o ponto central do projeto, é de fato classificar. O problema que tratamos nesse projeto é na verdade de learn to rank. Como o número de ligações que o setor de vendas pode efetuar é limitado, o time não poderá entrar em contato com toda a base de clientes que o algoritmo classificar como interessado, serão apenas 20 mil ligações, dessa forma, o que precisamos fazer é ordenar os clientes pela sua propensão de interesse em comprar o novo seguro de carro, assim o time de vendas utilizará essas 20 mil ligações da melhor maneira possível ligando apenas para os com maior chance de ter interesse. </p>

<p> Então, para esse tipo de problema devemos utilizar as métricas Precision@K e Recall@K, onde iremos medir a precision e recall apenas de uma parcela dos dados (a parcela que nos interessa). Nesse caso, a percela de dados que nos interessa são os 20 mil primeiros clientes (o @K do nome significa "at k", ou "até k", no nosso caso até 20 mil), pois são os que iremos conseguir entrar em contato durante a campanha. </p>

<p> Os modelos utilizados foram os K-nearest Neighbors (KNN), Logistic Regression, Random Forest e XGBoost. O modelo baseline representa o desempenho de não se utilizar nenhum modelo, representa a situação aonde a equipe de vendas entra em contato com os clientes de forma aleatória. A tabela a seguir mostra o desempenho dos modelos aplicados aos dados de teste. </p>

<h3> Single Result </h3>

| Model Name  |  Precision@K  |  Recall@K  |
| ------------------- | ------------------- | ------------------- |
|  XGBoost |  0.3296 |  0.7003 |
|  Random Forest |  0.3070	 |  0.6524 |
|  KNN |  0.2937 |  0.6241 |
|  Logistic Regression |  0.2888 |  0.6136 |
|  Baseline |  0.1258 |  0.2674 |

<p> Dentre os modelos aplicados, o XGBoost foi o que obteve disparado o melhor desempenho tanto em precision quanto em recall. Porém, esses valores não expressam de fato o desempenho dos modelos de forma fiel, pois a base de dados foi separada em 2 partes, os dados de treino para os modelos aprenderem, e os dados de testes o qual o modelos fizeram as previsões e obtiveram esse desempenho, e dessa forma existe a possibilidade dos dados de testes serem por coincidência um bom conjuto de dados que inflou artificialmente o desempenho dos modelos ou um mau conjunto de dados que reduziu o desempenho. </p>

<p> Dessa forma devemos aplicar a validação cruzada, uma maneira de medr o desempenho dos modelos dividindo o dataset em partes, aonde uma parte é utilizada para teste e as demais para treino e a cada iteração uma parte diferente é utilizada como teste, assim o modelo é teste utilizando diversos tipos diferentes de dados e o desempenho final é a média do desempenho obtido em todas as iterações. Na tabela a seguir encontramos o desempenho dos modelos após o cross-validation. </p>

<h3> Cross-Validation Result </h3>

| Model Name  |  Precision@K CV  |  Recall@K CV  |
| ------------------- | ------------------- | ------------------- |
| XGBoost | 0.3106 +/- 0.004 | 0.8327 +/- 0.0059 |
| Random Forest | 0.3082 +/- 0.0341 | 0.8261 +/- 0.087 |
| KNN | 0.2911 +/- 0.0347 | 0.7801 +/- 0.0889 |
| Logistic Regression | 0.2761 +/- 0.0021 | 0.7402 +/- 0.0076 |
| Baseline | 0.1258 | 0.2674 |

<p> Após a aplicação do cross-validation, o desempenho dos algoritmos XBoost e Random Forest se aproximaram ainda que o XGBoost ainda tenha se mantido maior, levando em consideração que o custo computacional do algoritmo Random Forest é bem maior que o do XGBoost, iremos seguir com o XGBoost já que esse custo de processamento pode fazer uma boa diferença no valor agregado a empresa quando o modelo for colocado em produção. </p>

<p> A próxima etapa é o hyperparameter fine tuning, uma etapa aonde tentamos encontrar o conjunto de valores para os atributos do algoritmo que maximizem o desempenho do modelo, por exemplo, o modelo XGBoost possui um atributo que é o max_depth, que indica qual é a profundida máxima da árvore de decisão que o algoritmo pode alcançar, se treinarmos o modelo duas vezes, uma vez passando max_depth = 3 e na segunda max_depth = 5 e o modelo obteve um desempenho maior quando utilizamos 5, então queremos utilizar 5 e não 3 por que o modelo melhora seu desempenho. </p>

<p> Existem algumas técnicas de se realizar o fine tuning, e a que utilizaremos nesse projeto é o random search, que consiste em passar uma lista com valores possíveis de cada atributo, escolhemos uma quantidade de vezes que queremos testar, e então o modelo é treinado o número de vezes que queremos testar e em cada vez, será escolhido um valor aleatório para cada atributo dentro da lista de valores que passamos, após isso escolhemos a combinação que obteve o melhor desempenho. Na tabela a seguir podemos ver o desempenho do algoritmo XGBoost após o fine tuning e utilizando o cross-validation. </p>

<h3> Cross-Validation Result After Fine Tuning </h3>

| Model Name  |  Precision@K CV  |  Recall@K CV  |
| ------------------- | ------------------- | ------------------- |
|  XGBoost Tunned |  0.3117 +/- 0.0058 |  0.8358 +/- 0.0111 |

<p> Após utilizar o conjunto de valores obtidos no random search, o modelo teve uma pequena melhora. </p>


<h1> Resultados Financeiros para o Negócio </h1>

<h3> Total Performance </h3>

<p> Aqui, iremos assumir que o preço médio do seguro de carro comercializado pela Dafa Insurance seja de R$ 2.000,00 e que o custo de ligação para entrar em contato com o cliente seja de R$ 100,00. Primeiro foi calculado qual o retorno financeiro se a empresa tivesse o objetivo de entrar em contato com todos os cliente interessados dessa base de dados. No gráfico a seguir o eixo x expressa a quantidade de clientes da base de dados, e o eixo y o retorno financeiro que empresa terá. </p>

![grafico1](https://user-images.githubusercontent.com/93053350/208209085-d9d7c36f-d057-4466-8c41-ef160f05c105.jpg)

<p> Entrando em contato com todos os interessados da base de dados com o modelo baseline, a empresa obteria um retorno financeiro de R$ 9.694.900,00, enquanto que com o modelo XGBoost o retorno seria de R$ 11.940900,00, um retorno 18,80% maior. </p>

<h3> Maximize Profit Efficiency </h3>

<p> Agora, iremos encontrar o ponto no gráfico aonde o retorno financeiro seja maximizado ao utilizar o modelo XGBoost e comparar com o baseline nesse mesmo ponto. </p>

![grafio2](https://user-images.githubusercontent.com/93053350/208209217-cc905394-87ce-456f-95ff-1dd7279f6955.jpg)

<p> Para atingir o ponto onde o retorno financeiro é maximizado, precisaríamos entrar em contato com 36.145 clientes. Nesse ponto o modelo baseline expressa um retorno de R$ 5.069.500,00, enquanto que o modelo XGBoost obtém um retorno de R$ 14.921.500,00, ou seja, um retorno 66,02% maior. </p>

<h3> Profit By Campaign Calls Capacity </h3>

<p> Agora iremos calcular o retorno financeiro dado o limite de ligações que serão possíveis efetuar durante a campanha. </p>

![grafico3](https://user-images.githubusercontent.com/93053350/208209263-d37ce2f6-93c7-4cdc-a58e-91bef9bc2572.jpg)

<p> Dada as circunstâncias da campanha de poder entrar em contato com apenas 20 mil clientes, o retorno financeiro do modelo baseline é de R$ 2.814.000,00, enquanto que o retorno do modelo XGBoost fica em R$ 11.698.000,00, um retorno 75,94% maior. </p>

<h1> Deploy do Modelo em Produção </h1>

<p> O modelo foi colocado em produção utilizando o Google Sheets. O aplicativo de planilhas do google funciona como o Excel e já é muito utilizado por diversas empresas para lidar com os dados. Nele é possível criar scripts para personalizar diversas características das planilhas, por meio do script criei um botão chamado "Propensity Score" que ao clicar abre um menu para outros botões que executam comandos, quando clicamos no botão "Get Prediction" do menu, automaticamente o script pega os dados que estão na planilha, e envia em formato json para a API onde o modelo está hospedado e faz uma requisição, então a API que devolve a previsão para esses dados, e então é criada uma nova coluna na planilha chamada "Score" com a propensão de interesse no novo seguro de carro de cada cliente, ao ordernar os clientes pelos valores mais altos na coluna Score, obtemos a lista que a equipe de vendas deve utilizar.  </p>

<p> Dessa forma, a utilização da solução pela equipe de vendas da empresa se torna super prática e inclusiva já que não será necessário fazer algum tipo de requisição a API ou banco de dados, possibilitando também fazer diversas análises diretamente aonde a equipe de venda trabalha com os dados (planilha do Google Sheets). No vídeo a seguir, tem um exemplo de como ficou o resultado final do modelo em produção utilizando o script. </p>


https://user-images.githubusercontent.com/93053350/208271969-898c2e16-25da-457e-8e39-8f07036f9010.mp4


<h1> Próximos Passos </h1>

<p> Procurar artigos específicos sobre o problema de learn to rank para aplicar novos algoritmos de machine learning que desempenhem e aprender novas técnicas de modelagem aplicáveis a esse tipo de problema. Obter uma melhora de 15% na Precision@K do atual modelo é uma meta para uma próxima iteração do CRISP-DM. </p>
