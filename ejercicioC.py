#Exercice: getting the length, or iterating 

from Bio.Seq import Seq
my_seq = Seq("GATCG")
for index, letter in enumerate(my_seq):
     print("%i %s" % (index, letter))
    
    # print(my_seq[0]) Imprime la primera letra
     #print(my_seq[1])
      # print(my_seq[2])
