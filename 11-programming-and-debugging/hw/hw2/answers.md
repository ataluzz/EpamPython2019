## Ответы
##### 1. Какой системный вызов будет использоваться чаще всего?
Самый частый syscall - stat (291)
Получено с помощью strace:

    sudo strace -c -o syscall.txt python3 shacheck.py dir_path hash_line
   
##### 2. Какой участок кода "самый горячий"? (профилирование)
Больше всего времени потребовала функция {built-in method _imp.create_dynamic}
Получено с помощью cProfile:

    python3 -m cProfile -o output.txt shacheck.py dir_path hash_line
  
В интерпретаторе python3:

    import pstats
    p = pstats.Stats("output.txt")
    p.strip_dirs().sort_stats("tottime").print_stats()
    
##### 3. Какой системный вызов потребил больше всего времени?
read
