# PTI-ANALISE-DE-SOLUCOES-INTEGRADAS-PARA-ORGANIZACOES


SERVIÇO NACIONAL DE APRENDIZAGEM COMERCIAL
SENAC


PROJETO INTEGRADOR V: ANÁLISE DE SOLUÇÕES INTEGRADAS PARA ORGANIZAÇÕES

SalãoGestor
“Plataforma Digital para Salões de Beleza”

ABNER GABRIEL AFFONSO
ANDERSON RODRIGUES FERNANDES
ALBERTO JANEIRO DURAN FILHO
BRUNO PIRES DE CAMPOS CARVALHO
CAUE LEMOS SENA
DAVI MONTEIRO BEZERRA
EMANOEL VIDAL CERQUEIRA DE MIRANDA
WILLIAN DOS SANTOS OLIVEIRA





EAD - ENSINO À DISTÂNCIA - 2025
                      
Integrantes do grupo: 
ABNER GABRIEL AFFONSO
ANDERSON RODRIGUES FERNANDES
ALBERTO JANEIRO DURAN FILHO
BRUNO PIRES DE CAMPOS CARVALHO
CAUE LEMOS SENA
DAVI MONTEIRO BEZERRA
EMANOEL VIDAL CERQUEIRA DE MIRANDA
WILLIAN DOS SANTOS OLIVEIRA
                                                                                       

SalãoGestor
“Plataforma Digital para Salões de Beleza”



Trabalho de conclusão de módulo do curso apresentado ao Centro Universitário Senac – Santo Amaro, como exigência para aprovação na disciplina de Projeto Integrador: Análise de soluções integradas para organizações, sob orientação do Prof. Carlos Henrique Veríssimo Pereira.
.





EAD - ENSINO À DISTÂNCIA - 2025




RESUMO

GABRIEL, A. RODRIGUES, A. JANEIRO, A, PIRES, B. LEMOS, C. MONTEIRO, D. VIDAL, E. SANTOS, W.  Implementação análise de soluções integradas para organizações. Centro Universitário SENAC, 2025.

Este trabalho científico foi desenvolvido com base na proposta do Centro Universitário SENAC, com o objetivo de investigar e apresentar a evolução dos elementos técnicos da computação e seus impactos na sociedade contemporânea. A pesquisa aborda desde os fundamentos da lógica computacional e organização interna dos computadores até os conceitos de programação e desenvolvimento de algoritmos, essenciais para a construção de soluções tecnológicas eficazes.

Além disso, o estudo contempla os impactos da ciência e da tecnologia na sociedade, explorando métodos de pesquisa e comunicação científica, bem como os fundamentos da administração e da gestão de organizações modernas. Também são analisadas as transformações no mundo do trabalho e os aspectos teóricos e tecnológicos que compõem a infraestrutura dos sistemas de informação nas organizações.

A disciplina associada ao trabalho promove tanto a prática colaborativa na ideação de soluções em grupo quanto o desenvolvimento individual de competências essenciais na área de Análise e Desenvolvimento de Sistemas, por meio de treinamentos autoinstrutivos.

Palavras-chave: Arquitetura da solução de software, Implementação de webservices e descrição dos serviços, front-end baseado em padrões web, fundamentos da administração, infraestrutura e tecnologia, computação em nuvem.


ABSTRACT

GABRIEL, A. RODRIGUES, A. JANEIRO, A, PIRES, B. LEMOS, C. MONTEIRO, D. VIDAL, E. SANTOS, W.  Implementation Analysis of Integrated Solutions for Organizations. SENAC University Center, 2025.

This scientific work was developed based on a proposal from the SENAC University Center, with the objective of investigating and presenting the evolution of the technical elements of computing and their impacts on contemporary society. The research covers topics ranging from the fundamentals of computational logic and the internal organization of computers to the concepts of programming and algorithm development, essential for building practical technological solutions.

Furthermore, the study considers the impacts of science and technology on society, exploring research methods and scientific communication, as well as the fundamentals of administration and management in modern organizations. It also demonstrates the transformations in the world of work and the theoretical and technological aspects that make up the infrastructure of information systems in organizations.

The discipline associated with the work promotes both collaborative practice in the ideation of group solutions and the individual development of essential skills in the area of Systems Analysis and Development, through self-paced training.

Keywords: Software solution architecture, Web services implementation and service description, front-end based on web standards, administration fundamentals, infrastructure and technology, cloud computing.










SUMÁRIO


INTRODUÇÃO...................................................................................................................7
1. REVISÃO BIBLIOGRÁFICA.........................................................................................8
1.1 Desenvolvimento de sistemas.....................................................................................8
1.2 Sistemas distribuídos...................................................................................................8
1.3 Web standards.............................................................................................................9
2. RESUMO DAS CONDIÇÕES DO PROJETO.............................................................11
2.1 Visão de produto........................................................................................................11
2.2 Definição das partes interessadas.............................................................................13
2.3 Personas....................................................................................................................15
2.4 Jornadas do Usuário .................................................................................................16
2.5 Prototipação...............................................................................................................20
3.0 PLATAFORMA – SALÃOGESTOR.....................................................................24
3.1 Estrutura de Navegação da Plataforma Web............................................................25
4.0 ELABORAÇÃO DO MVP (PRODUTO MÍNIMO VIÁVEL) ............................26
4.1 Linguagens de programação utilizadas.................................................................25
4.2 Baco de dados..........................................................................................................26



CONSIDERAÇÕES FINAIS.............................................................................................23
REFERÊNCIA BIBLIOGRÁFICA.....................................................................................24

 

INTRODUÇÃO

Com o avanço das tecnologias digitais e a crescente demanda por soluções automatizadas no setor de serviços, torna-se essencial o desenvolvimento de plataformas que otimizem a gestão e melhorem a experiência do usuário. O segmento de beleza, em especial, apresenta desafios recorrentes relacionados ao controle de agenda, atendimento personalizado e fidelização de clientes. Diante desse cenário, este trabalho científico propõe a criação de uma plataforma digital voltada para salões de beleza, com foco na implementação de um banco de dados eficiente para o controle de agendamentos.

A proposta contempla o uso de protótipos como ferramenta de validação da navegação e da usabilidade do sistema, permitindo ajustes iterativos com base na experiência do usuário. Além disso, será desenvolvido um Produto Mínimo Viável (MVP), que representa a versão funcional inicial da plataforma, capaz de atender às necessidades básicas do público-alvo e servir como base para futuras evoluções.

Este estudo busca integrar conceitos de engenharia de software, design de interface, modelagem de dados e gestão de serviços, contribuindo para a inovação tecnológica no setor de beleza e promovendo maior eficiência operacional para os profissionais da área.









1.	REVISÃO BIBLIOGRÁFICA

1.1.	Desenvolvimento de Sistemas
A informação é algo tão valioso para as instituições quanto o produto e o serviço que oferecem e, com o avanço das tecnologias e a facilidade ao seu acesso, as empresas passaram a depender cada vez mais desses dados e dos sistemas computacionais disponíveis para acompanhar suas atividades.
Os sistemas e softwares exercem um papel muito importante nesta era tecnológica, nos dias atuais as empresas, indivíduos, governo e população em geram tem total dependência dessa tecnologia.
O Surgimento dos primeiros sistemas de software ocorreu na década de 1950; sua evolução foi densa e rápida e, desde então, seu progresso é constante, continuando a ser a tecnologia mais importante no contexto mundial (PRESSMAN, 1995; PRESSMAN, 2016).
Desde o surgimento dos primeiros sistemas de software sua evolução não parou.

1.2. Sistemas Distribuídos
Os sistemas distribuídos desempenham um papel crucial em várias aplicações modernas, como serviços em nuvem e redes sociais. 
Segundo Tanenbaum e Van Steen (2016), “um sistema distribuído é aquele em que os componentes localizados em diferentes computadores trabalham de forma coordenada para alcançar um objetivo comum”. 
Essa característica permite a divisão de tarefas e a redundância, aumentando a eficiência e a tolerância a falhas.

Entre os aspectos mais notáveis dos sistemas distribuídos é sua escalabilidade.
 Conforme Coulouris, Dollimore e Kindberg (2012), “a escalabilidade é uma das principais vantagens desses sistemas, pois a adição de novos recursos não degrada seu desempenho global”. 


Característica particularmente importante em serviços como Amazon Web Services (AWS) e Google Cloud, onde a capacidade pode ser ajustada dinamicamente para atender à demanda.
A comunicação entre componentes em um sistema distribuído é geralmente realizada por meio de APIs e mensagens. 
Como explica Birman (2005), “a comunicação confiável é fundamental para o sucesso de sistemas distribuídos, especialmente em cenários de computação em tempo real”.


1.3.	Web Standards
Podemos definir Web Standards como conjunto de diretrizes e tecnologias que são definidas por organizações como o W3C (World Wide Web Consortium) e outras entidades relacionadas, e tem objetivo de garantir a consistência, acessibilidade e interoperabilidade da web. Esses padrões tem como objetivo garantir que os sites e aplicações web funcionem de maneira eficaz em diferentes navegadores, dispositivos e sistemas operacionais.
Como descrito pelo W3C (2014), “os padrões web promovem a compatibilidade entre navegadores e plataformas, assegurando que todos os usuários possam acessar conteúdo sem barreiras”.
Estes padrões e especificações para linguagens como HTML, CSS, e JavaScript, bem como práticas recomendadas para acessibilidade (como as diretrizes WCAG), estruturação de dados e protocolos da internet, como HTTP e HTTPS. O uso de Web Standards promove uma web mais aberta, confiável e inclusiva para todos
Web Standards são um conjunto de normas, recomendações e diretrizes que orientam a criação de sites acessíveis a todos.

Estes padrões web tem um papel essencial na criação de um ecossistema acessível e interoperável. Desenvolvidos pelo World Wide Web Consortium (W3C), eles 


garantem que tecnologias como HTML, CSS, JavaScript, PHP, sejam implementadas de maneira consistente. 
Além disso uma das inovações mais importantes no campo dos padrões web é o HTML5. 
De acordo com Meyer (2011), "o HTML5 simplifica a integração de elementos multimídia, eliminando a necessidade de plugins externos". Isso levou à criação de experiências mais interativas e acessíveis na web moderna.
Além disso, os padrões web reforçam a importância da acessibilidade. 
Segundo Slatin e Rush (2003), "a acessibilidade na web é um componente-chave para garantir que pessoas com deficiências possam acessar informações e serviços online". Isso reflete um compromisso com a inclusão digital, alinhado aos princípios éticos do desenvolvimento web.

Seguir estes conjuntos de diretrizes possibilitar uma aplicação de qualidade e concisa que com certeza atendera as necessidades do público-alvo.  















2.	RESUMO DAS CONDIÇÕES DO PROJETO
2.1 Visão do Produto: SalãoGestor
Criar uma solução digital completa e inteligente que transforme a gestão de salões de beleza, oferecendo controle total da agenda, organização dos serviços e equipe, e uma experiência encantadora para os clientes — tudo em uma interface moderna, intuitiva e segura.
https://miro.com/app/board/uXjVJII6agk=/
<img width="945" height="729" alt="image" src="https://github.com/user-attachments/assets/07f8a549-de84-4bb2-910c-54ba5301cdc9" />

Missão
Empoderar salões de beleza com tecnologia inteligente, oferecendo uma plataforma digital que simplifica a gestão, automatiza o agendamento e aprimora a experiência do cliente — tudo com eficiência, estilo e precisão. 

Objetivos
•	Digitalizar a gestão de salões de beleza: Eliminar processos manuais e descentralizados, oferecer uma plataforma intuitiva e acessível para todos os perfis de profissionais.
•	Automatizar o controle de agenda: Reduzir faltas e atrasos com notificações inteligentes, otimizar o tempo dos profissionais com agendamentos precisos e organizados.
•	Aumentar a produtividade da equipe: Monitorar desempenho, horários e comissões, organizar turnos, folgas e metas com clareza.
Benefícios
•	Agendamento sem complicações: Redução de erros e conflitos de horário, lembretes automáticos que diminuem faltas e atrasos, visão clara da agenda diária, semanal e mensal.
•	Gestão integrada da equipe: Distribuição inteligente de atendimentos conforme especialidades, controle de horários, folgas e produtividade dos profissionais.
•	Decisões baseadas em dados: Identificação de horários de pico e serviços mais procurados, planejamento estratégico com base em métricas reais.
•	Crescimento sustentável do negócio: Mais tempo para focar no atendimento e na expansão, redução de tarefas operacionais manuais, fortalecimento da imagem profissional do salão.

Frase de Efeito
"Organize com inteligência. Encante com beleza."

Com o SalãoGestor, cada salão se transforma em um centro de beleza inteligente e organizado. Seja você um profissional autônomo ou gestor de equipe, nossa plataforma coloca o controle da agenda, dos serviços e da experiência do cliente na palma da sua mão — para que cada atendimento seja impecável, e cada dia mais produtivo.

2.2 Definição das Partes Interessadas
A identificação e análise das partes interessadas é uma etapa fundamental no desenvolvimento de sistemas, pois permite compreender os diferentes perfis de usuários e entidades que influenciam ou são impactados pelo produto de software. No contexto da plataforma SalãoGestor, voltada à gestão de salões de beleza, foram definidos os indivíduos, grupos e organizações com interesse direto ou indireto no sistema, considerando seu nível de envolvimento, expectativas e necessidades específicas.
2.2.1 Identificação e Classificação
As partes interessadas foram organizadas em categorias conforme sua natureza e relação com o projeto:
<img width="888" height="314" alt="image" src="https://github.com/user-attachments/assets/fe078b38-2c80-44c6-89cb-a80d12044506" />


2.2.2 Interesses, Necessidades e Expectativas
Cada parte interessada possui demandas específicas em relação ao produto de software, que devem ser consideradas no processo de análise de requisitos e tomada de decisão:
•	Equipe de Desenvolvimento: espera clareza nos requisitos, viabilidade técnica e escalabilidade da solução.
•	Gestores do Projeto: buscam cumprimento de prazos, qualidade do produto e alinhamento com os objetivos estratégicos.
•	Gestores de Salões: necessitam de uma interface intuitiva, controle eficiente da agenda e relatórios gerenciais.
•	Profissionais Autônomos: desejam praticidade no agendamento, visibilidade dos serviços e fidelização de clientes.
•	Recepcionistas: demandam agilidade no atendimento, redução de erros e organização da rotina.
•	Clientes Finais: esperam facilidade de agendamento, lembretes automáticos e atendimento personalizado.
•	Investidores: têm interesse em retorno financeiro, escalabilidade e potencial de mercado.
•	Fornecedores de Tecnologia: requerem integração estável, documentação clara e suporte técnico.
•	Instituições Reguladoras: exigem conformidade legal, segurança de dados e transparência no uso das informações.

2.2.3 Priorização das Partes Interessadas
A priorização foi realizada com base no nível de influência e interesse de cada parte interessada, conforme a tabela a seguir:

<img width="945" height="255" alt="image" src="https://github.com/user-attachments/assets/b26a348b-44d0-4876-82b2-48e2f2040a87" />

A análise das partes interessadas permite alinhar o desenvolvimento do SalãoGestor às reais necessidades dos usuários e agentes envolvidos, promovendo maior assertividade na definição de requisitos, priorização de funcionalidades e estratégias de comunicação. Ao compreender os diferentes níveis de envolvimento e expectativas, o projeto se fortalece em termos de usabilidade, aderência ao mercado e conformidade legal, contribuindo para o sucesso e sustentabilidade da solução.




2.3 Desenvolvimento de personas
Maria Silva
Idade: 28 anos
Ocupação: Analista de Marketing
Preferências: Agendamentos rápidos, notificações de lembrete, histórico de serviços.
Objetivos: Manter o cabelo bem cuidado sem perder tempo ligando para o salão.
Desafios: Agenda cheia e pouco tempo livre.
Comportamentos: Prefere aplicativos com interface simples, usa redes sociais para recomendações.
João Pereira
Idade: 35 anos
Ocupação: Cabeleireiro autônomo
Preferências: Ferramenta fácil para gerenciar horários, perfil profissional para atrair clientes.
Objetivos: Aumentar a clientela e ter controle total da agenda.
Desafios: Evitar conflitos de horários e cancelamentos de última hora.
Comportamentos: Acessa o aplicativo várias vezes ao dia, valoriza avaliações dos clientes.
Carla Souza
Idade: 42 anos
Ocupação: Advogada
Preferências: Opção de pagamento online, sugestões de novos serviços.
Objetivos: Encontrar horários flexíveis e serviços de qualidade.
Desafios: Conciliar agenda profissional e pessoal.
Comportamentos: Faz agendamentos com antecedência, busca praticidade.
Lucas Andrade
Idade: 23 anos
Ocupação: Estudante
Preferências: Promoções e descontos, fácil cancelamento.
Objetivos: Cuidar do visual sem gastar muito.
Desafios: Orçamento limitado.
Comportamentos: Verifica preços antes de marcar, usa muito o celular para tudo.
Rogerio Santana
Idade: 43 anos
Ocupação: Gestor de Salão
Preferências: Fácil agendamento, controle de clientes e horários, fácil navegação entre as informações de clientes agendados
Objetivo: Organizar todos os clientes agendados para facilitar o atendimento pelos profissionais
Desafios: Manejar quantidade de clientes com disponibilidade de horários
Comportamentos: Sempre entra no aplicativo para gerenciar os clientes e os horários, gosta de uma interface intuitiva.

2.4 Jornadas do usuário
Maria Silva
Ponto de Contato: Reagendamento Rápido de Serviço Persona: Maria Silva (Analista de Marketing com agenda cheia)
Etapas:
•	Pesquisa: Maria percebe que a raiz do cabelo precisa de um retoque. Em vez de pesquisar um novo serviço, ela acessa diretamente o histórico do aplicativo para encontrar o último serviço realizado.
•	Comparação: Não há comparação, pois Maria já é cliente fiel e quer repetir o mesmo serviço ("Retoque de Luzes") com o mesmo profissional. Sua prioridade é a velocidade do agendamento.
•	Decisão de Agendamento: Maria decide agendar o quanto antes. Ela clica na opção "Agendar Novamente" diretamente do seu histórico de serviços para otimizar o tempo.
•	Agendamento: A plataforma a leva diretamente para a agenda do seu profissional preferido. Ela visualiza as datas disponíveis, seleciona o próximo sábado pela manhã e escolhe o horário.
•	Confirmação: Maria confirma o agendamento em poucos cliques. Imediatamente, recebe uma confirmação por notificação no celular e um e-mail. Um lembrete automático é agendado para o dia anterior.
•	Dia do Compromisso: Maria chega ao salão na hora marcada. A recepcionista já tem todos os detalhes do seu agendamento, e o profissional sabe exatamente o serviço a ser realizado, proporcionando um atendimento rápido e eficiente.

João Pereira
Ponto de Contato: Gestão da Agenda e Atração de Clientes Persona: João Pereira (Cabeleireiro autônomo)
Etapas:
•	Pesquisa: João inicia o dia abrindo o aplicativo para "pesquisar" sua própria agenda. Ele verifica todos os clientes e serviços agendados para organizar suas ferramentas e tempo.
•	Comparação: João "compara" os horários vagos com os horários de pico. Ele percebe um espaço livre à tarde e decide postar uma foto de seu último trabalho no portfólio para tentar atrair um novo cliente para aquele horário.
•	Decisão de Agendamento: Um cliente em potencial vê o portfólio atualizado de João e se impressiona. O cliente decide agendar um serviço justamente no horário que João tinha disponível.
•	Agendamento: João recebe uma notificação instantânea sobre o novo agendamento. O horário em sua agenda é preenchido automaticamente, evitando qualquer conflito.
•	Confirmação: O sistema confirma o agendamento para o cliente e para João. O cabeleireiro revisa os detalhes do novo serviço (um corte específico) para se preparar mentalmente para o atendimento.
•	Dia do Compromisso: João recebe o novo cliente no horário. Ele menciona que viu a foto postada no perfil, confirmando que a plataforma funciona como uma ferramenta eficaz para gerenciar e atrair clientes.


Lucas Andrade
Ponto de Contato: Busca e Agendamento de Serviço com Desconto Persona: Lucas Andrade (Estudante com orçamento limitado)
Etapas:
•	Pesquisa: Lucas precisa cortar o cabelo, mas quer garantir que encontrará o melhor preço possível. Ele abre o aplicativo focado em encontrar promoções ativas.
•	Comparação: Lucas acessa a seção de "Promoções" e encontra uma oferta de "Corte com 20% de desconto às terças-feiras". Ele compara o preço final com o valor cobrado por outros profissionais no aplicativo para validar que é a opção mais econômica.
•	Decisão de Agendamento: Lucas decide aproveitar a promoção, pois o desconto torna o serviço ideal para seu orçamento. Ele planeja agendar para a próxima terça-feira.
•	Agendamento: Lucas acessa a página da promoção e seleciona a opção para agendar. Ele visualiza os horários disponíveis para terça-feira e escolhe um no final da tarde, após sua aula. O sistema já mostra o valor com o desconto aplicado.
•	Confirmação: Após selecionar o horário, Lucas confirma o agendamento. Ele recebe uma notificação no aplicativo e um e-mail com os detalhes do serviço, incluindo o valor promocional.
•	Dia do Compromisso: Lucas chega ao salão no horário agendado. Ele menciona na recepção que agendou o serviço com desconto pelo aplicativo e é encaminhado ao profissional para o atendimento.

Rogerio Santana
Ponto de Contato: Gerenciamento do Fluxo de Clientes na Recepção Persona: Rogério Santana (Gestor de Salão)
Etapas:
•	Pesquisa: Rogério inicia o expediente "pesquisando" a agenda geral do dia no painel de gestão. Ele identifica os horários de maior movimento e a distribuição dos clientes entre os profissionais.
•	Comparação: Um cliente chega. Rogério compara o nome do cliente com a lista de agendamentos na tela. Ele rapidamente localiza o horário, o serviço e o profissional responsável.
•	Decisão de Agendamento: Um cliente fiel telefona pedindo um "encaixe". Rogério analisa a agenda visualmente e identifica um pequeno intervalo. Ele decide criar um novo agendamento manualmente para não perder o cliente.
•	Agendamento: Rogério clica no horário vago, preenche os dados do cliente e do serviço e atribui a um profissional que estará livre. A agenda de todos é atualizada em tempo real.
•	Confirmação: Rogério confirma verbalmente o encaixe com o cliente ao telefone. Internamente, o profissional designado recebe uma notificação sobre o novo serviço em sua agenda.
•	Dia do Compromisso: Quando os clientes (tanto os agendados online quanto os de encaixe) chegam, Rogério gerencia o fluxo, encaminhando cada um ao seu profissional com base nas informações centralizadas e sempre atualizadas do sistema.














2.5 Prototipação - SalãoGestor
https://www.figma.com/design/jXtivnlWztpo3yeC7xcHFR/Sal%C3%A3oGestor?node-id=0-1&p=f&t=MNy3YgTevRAMzkV7-0

<img width="806" height="585" alt="image" src="https://github.com/user-attachments/assets/3e59c449-f984-4d7b-9133-031d11d7f684" />
<img width="806" height="601" alt="image" src="https://github.com/user-attachments/assets/72320276-152a-482c-b943-2c6301481681" />
<img width="850" height="624" alt="image" src="https://github.com/user-attachments/assets/b466d2ed-2c88-48c1-a2c9-f9abf9032147" />
<img width="848" height="631" alt="image" src="https://github.com/user-attachments/assets/4e53a404-3e4f-44e0-a7a8-972dcf8a033b" />
<img width="852" height="627" alt="image" src="https://github.com/user-attachments/assets/cfce1e28-9908-4e84-ae24-0e28917044ce" />
<img width="856" height="618" alt="image" src="https://github.com/user-attachments/assets/694f3f44-793b-4d99-8a73-8cbea1416494" />


3.0 Plataforma Digital para Salões de Beleza – SalãoGestor
A aplicação desenvolvida no projeto SalãoGestor será apresentada ao público por meio de uma plataforma web, concebida com as tecnologias HTML, CSS e Python. Essa plataforma tem como objetivo principal divulgar as funcionalidades do sistema, facilitar o contato com os usuários e promover a adesão ao serviço por meio de uma interface acessível e responsiva.
O site foi estruturado com foco na usabilidade e na comunicação eficiente, incorporando formulários interativos que permitem:
•	Envio de e-mails: para dúvidas, sugestões ou suporte técnico.
•	Solicitação de acesso: possibilitando que novos usuários se cadastrem ou solicitem demonstrações da aplicação.
•	Consulta de preços: oferecendo transparência e praticidade na apresentação dos planos e serviços disponíveis.
A integração dos formulários com scripts em Python garante o processamento seguro e automatizado das informações enviadas pelos usuários, além de permitir escalabilidade futura para funcionalidades mais complexas, como autenticação, geração de relatórios ou integração com bancos de dados.
A plataforma também cumpre papel estratégico na comunicação visual do projeto, apresentando o conceito do SalãoGestor, seus diferenciais e os benefícios para salões de beleza. O design moderno, aliado à navegação intuitiva, reforça a proposta de inovação e profissionalismo, contribuindo para a credibilidade da solução junto ao público-alvo.
Link de acesso a plataforma:  https://emanoel2511.github.io/Sal-oGestor_2025/

<img width="945" height="634" alt="image" src="https://github.com/user-attachments/assets/452c8a24-d621-4873-8136-28cb046f5a4b" />

A plataforma web do projeto SalãoGestor incorpora uma seção dedicada às visualizações da aplicação, com o objetivo de apresentar ao usuário as principais funcionalidades do sistema de forma prática e interativa. Essa área é composta por hiperlinks que redirecionam para telas específicas da aplicação, permitindo uma navegação fluida entre os módulos e facilitando o entendimento da proposta tecnológica.
<img width="945" height="492" alt="image" src="https://github.com/user-attachments/assets/f6427a59-3739-4896-a059-636110673d7e" />
<img width="945" height="741" alt="image" src="https://github.com/user-attachments/assets/3c9c2e51-4a8a-4d1d-b5c5-a615ec572879" />

3.1 Estrutura de Navegação da Plataforma Web


A plataforma web desenvolvida para divulgação da aplicação SalãoGestor apresenta uma estrutura de navegação clara e funcional, com foco na experiência do usuário e na facilidade de acesso às informações. A aba principal do site é composta por itens estrategicamente organizados, cada um com hiperlinks que direcionam o visitante para seções específicas da página ou para canais externos de comunicação. Essa abordagem visa otimizar a usabilidade e garantir que os usuários encontrem rapidamente os conteúdos de seu interesse.
Os itens da aba principal são:
•	Início: redireciona para a seção principal da página, onde são apresentados as funcionalidades e os diferenciais da aplicação.
•	Teste Grátis: conduz o usuário a um formulário de solicitação de acesso gratuito à plataforma, incentivando a experimentação do sistema.
•	Preços: apresenta os planos disponíveis, com informações detalhadas sobre valores, recursos inclusos e formas de contratação.
•	Sobre o SalãoGestor: seção dedicada à missão, visão e objetivos do projeto, contextualizando sua proposta de valor.
•	Contato: disponibiliza um formulário para envio de mensagens, dúvidas ou sugestões, além de informações institucionais.
•	Blog: direciona para uma área com conteúdo informativos e atualizações sobre o setor de beleza e gestão de salões.
•	WhatsApp: link externo que abre uma conversa direta com a equipe de atendimento via aplicativo WhatsApp, facilitando o suporte em tempo real.
•	Telefone: exibe o número de contato do salão ou da equipe responsável pela aplicação, com possibilidade de discagem direta em dispositivos móveis.
Essa organização visa proporcionar uma navegação fluida e intuitiva, reforçando a credibilidade da solução e promovendo o engajamento dos usuários com a marca SalãoGestor.

4.0 Elaboração do MVP (Produto Mínimo Viável)
Produto mínimo viável (MVP) - O Salão Gestor foi desenvolvido utilizando Python em conjunto com o framework Flask, com o objetivo de criar uma aplicação web leve, modular e de fácil manutenção para o gerenciamento de salões de beleza.
A escolha do Python se deve à sua clareza sintática, produtividade e ampla disponibilidade de bibliotecas, que facilitam a implementação de funcionalidades como manipulação de dados, autenticação e geração de relatórios.
O Flask foi adotado como framework principal do backend por sua flexibilidade e simplicidade. Ele fornece os recursos essenciais para criação de rotas, tratamento de requisições HTTP, controle de sessões e integração com o banco de dados, sem impor estruturas rígidas de desenvolvimento.
A arquitetura do sistema segue o padrão Model–View–Template (MVT), que separa a aplicação em três camadas principais. O Model define as entidades e realiza o mapeamento objeto-relacional via SQLAlchemy. A View processa as regras de negócio e retorna respostas às requisições. Já o Template, implementado com Jinja2, é responsável pela renderização dinâmica das páginas HTML. Essa estrutura garante uma aplicação organizada, escalável e de fácil manutenção.
Também foram utilizadas extensões complementares, como Flask-Login (para autenticação e controle de usuários) e Flask-SQLAlchemy (para gerenciamento de banco de dados). Essa combinação de tecnologias oferece ao Salão Gestor uma base sólida, segura e preparada para expansão futura.
Link do projeto hospedado: 
https://github.com/vv1ll14n/PTI-ANALISE-DE-SOLUCOES-INTEGRADAS-PARA-ORGANIZACOES/tree/main/salaogestor/templates


4.1 Banco de dados.
O banco de dados escolhido para o projeto SalãoGestor foi o PostgreSQL, uma solução robusta, gratuita e de código aberto, amplamente reconhecida por sua confiabilidade e desempenho em ambientes corporativos e acadêmicos. Ele oferece suporte avançado a operações relacionais, além de recursos como controle de concorrência, integridade transacional e extensibilidade.
Entre os principais motivos para sua adoção estão:
•	Compatibilidade com Python: integração eficiente com frameworks como Flask, facilitando o desenvolvimento da aplicação.
•	Segurança e escalabilidade: ideal para aplicações que exigem crescimento contínuo e proteção dos dados dos usuários.
•	Suporte a SQL padrão: permite consultas complexas e manipulação de dados com alto desempenho.
•	Comunidade ativa: oferece ampla documentação e suporte técnico por meio de fóruns e atualizações constantes.
O PostgreSQL foi utilizado para armazenar informações como cadastros de clientes, agendamentos, serviços, equipe e registros administrativos, garantindo consistência e integridade dos dados ao longo do uso da aplicação.








CONSIDERAÇÕES FINAIS
Ao desenvolver o projeto SalãoGestor, concluímos que ele representa um avanço essencial na modernização da gestão de salões de beleza. A proposta de uma plataforma digital voltada ao controle de agenda, organização de serviços e melhoria da experiência do cliente se mostrou estratégica para atender às demandas reais do setor.
Ao priorizar tecnologias móveis e soluções web, conseguimos ampliar o alcance da plataforma, tornando-a acessível tanto para gestores de salões quanto para profissionais autônomos e clientes finais. Essa abordagem garante versatilidade, praticidade e adaptação ao estilo de vida conectado dos usuários modernos.
A integração entre dispositivos móveis, banco de dados em nuvem e interface intuitiva permite que o sistema seja escalável, flexível e continuamente aprimorado — sem necessidade de grandes mudanças estruturais. Além disso, a segurança das informações, especialmente dados sensíveis de clientes e profissionais, permanece como prioridade central no desenvolvimento da solução.
Em síntese, o SalãoGestor não é apenas uma ferramenta de agendamento, mas uma plataforma inteligente que transforma a rotina dos salões, potencializa a produtividade da equipe e fortalece o relacionamento com os clientes. Ao unir boas práticas de desenvolvimento com foco em inovação e experiência do usuário, este projeto se consolida como uma solução tecnológica relevante, eficiente e preparada para os desafios do mercado da beleza.











REFERÊNCIAS
TANENBAUM, Andrew S.; VAN STEEN, Maarten. Sistemas Distribuídos: Princípios e Paradigmas. 2. ed. Pearson Education, 2016.

COULOURIS, George; DOLLIMORE, Jean; KINDBERG, Tim. Distributed Systems: Concepts and Design. 5. ed. Boston: Addison-Wesley, 2012.

BIRMAN, Kenneth P. Sistemas Distribuídos Confiáveis: Tecnologias, Serviços Web e Aplicações. Nova York: Springer, 2005.

WORLD WIDE WEB CONSORTIUM. Web standards: compatibility across platforms and browsers. 2014. Disponível em: <http://www.w3.org/standards/>. Acesso em: 09 de agosto. 2025.

MEYER, Eric A. HTML5 for Web Designers. 1. ed. New York: A Book Apart, 2011. 86 p. 
SLATIN, John M.; RUSH, Sharron. Maximum Accessibility: Making Your Web Site More Usable for Everyone. Boston: Addison-Wesley, 2003. 352 p

LEITE, Jair C. Engenharia de software: ciclos de vida. Universidade do Rio Grande do Norte, 2006.

SOMMERVILLE, Ian. Engenharia de software. 8. ed. São Paulo: Pearson Addison-Wesley, 2007.









