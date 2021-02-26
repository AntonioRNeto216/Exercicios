using System;
using System.Collections.Generic;

namespace C_ {
    class Program {
        static void Main() { // usado para chamar a função do exercício
            
        }

        /* 
            MigratoryBirds: https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=profile
        */
        static int MigratoryBirds(List<int> arr) 
        {
            Dictionary<int,int> dicFinal = new Dictionary<int, int>(); // key: ID , value: frequency
            foreach(int conteudoPosicao in arr)
            {
                if(dicFinal.Count == 0 || !dicFinal.ContainsKey(conteudoPosicao))
                    dicFinal.Add(conteudoPosicao, 1);
                else
                    dicFinal[conteudoPosicao] += 1;
            }
            int idRetorno = 0; // precisa ter um valor inicial
            bool first = true;
            foreach(KeyValuePair<int,int> pair in dicFinal)
            {
                if(first)
                {
                    idRetorno = pair.Key;
                    first = false;
                } else
                {
                    if(dicFinal[idRetorno] == pair.Value)
                    {
                        idRetorno = idRetorno < pair.Key ? idRetorno : pair.Key;
                    } else if(dicFinal[idRetorno] < pair.Value)
                    {
                        idRetorno = pair.Key;
                    }
                }
            }
            return idRetorno;
        }
        ////
    }
}
