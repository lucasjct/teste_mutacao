# teste_mutacao
Avaliando a qualidade dos teste unitários
***  

O teste de mutação verificam a qualidade dos testes unitários ou de componentes. Cada componente recebe um mutante, esse mutante pode alterar o código (só durante a execução do teste). Por exemplo, alterar os operadores lógicos e operadores aritiméticos de cada função e verificar se seu teste unitário atua para prevenir/cobrir este comportamento. Caso não, o mutante sobrevive e significa que seu teste unitário não cobre todos os cenários ainda. O log do teste exibirá as alterações e sugestões.


### Para Rodar:

`mut.py --target calculator.py --unit-test tests.py -m --report-html relatorio`

### Dependências:

- Mutpy

### Site do Projeto

[MutPy](https://pypi.org/project/MutPy/)  
Multpy possui suporte também para Pytest    

### Para mais informações: 
[Live De Python - Dunossauro](https://www.youtube.com/watch?v=wczL0iDtmuw&t=2267s)
