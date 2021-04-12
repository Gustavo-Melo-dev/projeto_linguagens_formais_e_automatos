from automata.base.automaton import Automaton
from automata.fa.fa import FA
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

resultado = input("Qual o valor: ")
if(resultado == '1'):

  #IMPLEMENTAÇÃO DO DFA
  # O algoritmo tem como objetivo verificar se existe uma sequencia ímpar de 1's.

  dfa = DFA(
      states={'q0', 'q1', 'q2'}, #Quantidade de estados que desejar.
      input_symbols={'0', '1'}, #Quais os símbolos do alfabeto deseja usar.
      transitions={ #Transições: 1 - Estado, 2 - Valor a verificar, 3 - Estado que deve permanecer ou mudar, 4 = 2 e 5 = 3.
          'q0': {'0': 'q0', '1': 'q1'},
          'q1': {'0': 'q0', '1': 'q2'},
          'q2': {'0': 'q2', '1': 'q1'}
      },
      initial_state='q0', #Indicar o estado inicial.
      final_states={'q1'} #Indicar o estado final.
  )

  print('Resultado do DFA: ')
  if dfa.accepts_input('111111101110111'): #Coloque uma sequência binária que deseja testar.
      print('accepted')
  else:
      print('rejected')



elif (resultado == '2' ):

  #IMPLEMENTAÇÃO DO NFA
  # O algoritmo tem como objetivo verificar palavras começando com a e terminando com a e que não tenham duas letras b consecutivas.

  nfa = NFA(
      states={'q0', 'q1', 'q2'}, #Quantidade de estados que desejar.
      input_symbols={'a', 'b'}, #Quais os símbolos do alfabeto deseja usar.
      transitions={ #Transições: 1 - Estado, 2 - Valor a verificar, 3 - Estado que deve permanecer ou mudar, 4 = 2 e 5 = 3.
          'q0': {'a': {'q1'}},
          'q1': {'a': {'q1'}, '': {'q2'}}, #Utilizar '' para transições vazias.
          'q2': {'b': {'q0'}}
      },
      initial_state='q0',
      final_states={'q1'}
      
  )

  dfa = DFA.from_nfa(nfa) #Conversão do NFA em DFA e printando o resultado.

  print('Resultado do NFA: ')
  if nfa.accepts_input('ababab'):
      print('accepted')
  else:
      print('rejected')