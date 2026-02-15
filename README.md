# Gerador de Orçamentos - Imobiliária R.M
Este projeto é uma ferramenta web desenvolvida para automatizar o cálculo de orçamentos de locação de imóveis. O sistema permite calcular o valor mensal do aluguel com base em diferentes categorias (Apartamento, Casa e Estúdio) e gerenciar o parcelamento de contratos de serviço.

# Funcionalidades
Cálculo Dinâmico: Aplica regras específicas para cada tipo de imóvel.

Gestão de Contrato: Divide o valor fixo de R$ 2.000,00 em até 5 parcelas.

Regras de Negócio Customizadas: * Desconto de 5% para apartamentos sem crianças.

Cálculo de vagas excedentes para estúdios (R$ 60,00 por vaga adicional após a 2ª).

Acréscimos por quantidade de quartos e vagas de garagem.

Exportação de Dados: Gera um arquivo .csv com a projeção das 12 parcelas do ano.

# Tecnologias Utilizadas
Linguagem: Python

Framework Web: Flask

Frontend: HTML5 e CSS3 (Design responsivo)

Persistência: CSV (Exportação de relatórios)

# Regras de Cálculo
Imóvel	Valor Base	Adicional Quarto (>=1)	Adicional Vaga	Regra Especial
Apartamento	R$ 700,00	+ R$ 200,00	+ R$ 300,00	-5% se não houver crianças
Casa	R$ 900,00	+ R$ 250,00	+ R$ 300,00	N/A
Estúdio	R$ 1.200,00	N/A	Especial	+ R$ 250 (2 vagas) + R$ 60/vaga extra

# Lógica de Desenvolvimento
O projeto foi estruturado utilizando Programação Orientada a Objetos (POO). A classe principal Orcamento encapsula toda a lógica matemática, garantindo que o código seja fácil de manter. O fluxo de decisão foi previamente planejado através de um Fluxograma, garantindo que as condicionais de cada imóvel não se sobreponham.

Desenvolvido por: Kauany Santos

Projeto Acadêmico - 2026

